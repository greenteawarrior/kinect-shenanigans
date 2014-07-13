from kinect_skel import Kinect, Person
from openni import *
from pprint import pprint

class KinectCLI(Kinect):

    def new_user(self, src, id):
        print "1/4 User {} detected.".format(id)
        self.pose_cap.start_detection(self.pose_to_use, id)
        self.people[id] = Person(id)

    def calibration_complete(self, src, id, status):
        if status == CALIBRATION_STATUS_OK:
            print "4/4 User {} calibrated successfully! Starting to track." .format(id)
            self.skel_cap.start_tracking(id)
            self.current_person = self.people[id]
            self.refresh()
            self.prompt_user()
        else:
            print "ERR User {} failed to calibrate. Restarting process." .format(id)
            self.new_user(self.user, id)

    def capture_data(self, pose):

        data = {'torso': None, 'right_hand': None, 'left_hand': None}

        for id, person in self.people.items():
            for k in data:
                node = getattr(person, k)
                print id, k, node.point, node.confidence
                data[k] = (node.point, node.confidence)

        pprint(data)
        print "Capture complete"

    def prompt_user(self):
        pose = raw_input("Enter the current pose: ").strip()
        if len(pose) != 1:
            print "\nPlease enter a single character."
            self.prompt_user()
        else:
            self.capture_data(pose)

def run():
    k = KinectCLI()
    while True:
        k.refresh()

if __name__ == "__main__":
    run()
