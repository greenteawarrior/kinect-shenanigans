kinect-shenanigans
==================

[summer 2014] ReadML curriculum development with the kinect (basically all the CV shenanigans)

####Learning the math
- we should learn/know it for fun/knowledge
- however don't overwhelm the new members who haven't taken the math classes yet to understand everything easily...
- mention some of the black boxes, and if people want to learn more, please talk to us :DDD

some comments from friends:
- make nice pictures/diagrams
- perhaps give an equation of what we're trying to solve and then explain the math in an intuitive way

####Hardware setup
- please make this as painless as possible...............
- debugging and things
- maybe write a script that does the installs/setup
- make sure to test the hardware setup with some initial testers before kinect module day

Follow guidelines on http://www.20papercups.net/programming/kinect-on-ubuntu-with-openni/ to the letter, up until the NITE installation guide.

NITE binaries aren't 100% necessary, but may come in useful later.
Download SimpleOpenNI NITE binaries (where NITE is packaged): 
```bash
wget https://simple-openni.googlecode.com/files/OpenNI_NITE_Installer-Linux64-0.27.zip
unzip OpenNI_NITE_Installer-Linux64-0.27.zip
cd OpenNI_NITE_Installer-Linux64-0.27/NITE-Bin-Dev-Linux-x64-v1.5.2.21
sudo ./install.sh
```


####Ideation! kinect in ReadML curriculum
- Learning how to OpenNI: exposure to the API (so...maybe going through some example code?), plot some raw output
- single point tracking (so, maybe a doodle app or something pretty like silk)
- people recognition - fun, easily applicable to other projects
- talking about what problems are well suited for the kinect
- segue to a fun ideation session with the ReadML members :P
- show how the machine learning techniques are generally applicable

####Potential projects 
-object recognition with depth sensor
-audiomotion! polishing our music therapy hack project
-simon says - pick a simon, detect when the person says "simon says" (audio?? or some other way to distinguish simon), see if the other people did the action...
-semaphore - will the kinect handle this well if it's flags when it's usually used for people?
-some photography things, not necessarily ML related: -add depth of field (photo effects) - not the most ML-y but it's good for getting familiar with the included sensor data
-replicating just dance - choreograph, tell program to give directions on how to dance, then see if the person did it correctly/had good timing

