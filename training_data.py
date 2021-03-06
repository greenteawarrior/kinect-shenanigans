from kinect_skel import Kinect, Person
from openni import *
from pprint import pprint
from sklearn.externals import joblib
import json

def append_to_csv(filename, string):
    fd = open(filename,'a')
    fd.write(string)
    fd.close()

class KinectCLI(Kinect):

    def __init__(self, filename='data.csv'):
        Kinect.__init__(self)
        self.filename = filename
        self.collect_data = False

    def refresh(self):
        # Update to next frame
        self.ctx.wait_and_update_all()

        # Extract head position of each tracked user
        for id in self.user.users:
            if self.skel_cap.is_tracking(id):

                # Point , Confidence
                joint = self.skel_cap.get_joint_position(id, SKEL_HEAD)
                self.people[id].head = joint

                joint = self.skel_cap.get_joint_position(id, SKEL_LEFT_HAND)
                self.people[id].right_hand = joint

                joint = self.skel_cap.get_joint_position(id, SKEL_RIGHT_HAND)
                self.people[id].left_hand = joint

                # adding torso for the sake of semaphore
                joint = self.skel_cap.get_joint_position(id, SKEL_TORSO)
                self.people[id].torso = joint

                if self.collect_data:
                    # For semaphore data collection
                    # self.collect_data is set by the prompt_user method

                    data = {'torso': None, 'right_hand': None, 'left_hand': None}

                    for k in data:
                        node = getattr(self.people[id], k)
                        data[k] = (node.point, node.confidence)
                    data['pose'] = self.pose

                    # for data logging
                    append_to_csv(self.filename, json.dumps(data))
                    self.collect_data = False

    def calibration_complete(self, src, id, status):
        if status == CALIBRATION_STATUS_OK:
            print "4/4 User {} calibrated successfully! Starting to track." .format(id)
            self.skel_cap.start_tracking(id)
            # prompt user to collect data
            self.prompt_user()
        else:
            print "ERR User {} failed to calibrate. Restarting process." .format(id)
            self.new_user(self.user, id)

    def prompt_user(self):
        # pause data collection until test subject is ready
        pose = raw_input("Enter the current pose: ").strip()
        if len(pose) != 1:
            print "\nPlease enter a single character."
            self.prompt_user()
        else:
            # set flags to be read by self.refresh, called in the main program loop
            self.collect_data = True
            self.pose = pose

def run():
    k = KinectCLI()
    while True:
        k.refresh()

if __name__ == "__main__":
    run()
