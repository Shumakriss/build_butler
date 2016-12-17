Update
===========
I have moved all my hacky mostly-borrowed scripts to the sample_code directory. Borrowing some ideas from game AI design, I realized that a basic finite state machine would be adequate for the essential job of the bot and have implemented a simple FSM in the build_butler package. I intend to clean up and optimize my POC scripts and move them into their respective subpackages.

I have introduced a fun but non-portable detail which is that the textToSpeech module uses the "say" command available on OSX. I will eventually need to update this to be more portable but in the meantime, please replace any calls to tts.say() with print().

Some Next Steps:
* Cleanup modules/States - Especially recognition
* Rewrite FSM to avoid stack overflow
* Rewrite FSM to pass data more cleanly, perhaps some global info for States
* Update PCA library
* Update Carbon Component Manager library
* Replace ID with usernames
* Use a real Jenkins POST body
* Create remote sensor/control API on RPi
* Purchase and mount iRobot Create
* Implement the pathfinding module and integrate into State
* Migrate the text to speech module to something cross-platform
* Purchase and integrate speakers to RPi

Description
===========
Build Butler is a robot that finds whoever broke the build. 

Credit
----------
This repo is largely full of example code that has been borrowed and cobbled together like a bunch of Legos. I still need to list some references so assume that most of the code is not mine. The idea, collection, and integration of the examples is mine, however, and the code was all obtained freely from open source projects.

For Speech recognition: [https://github.com/Uberi/speech_recognition](https://github.com/Uberi/speech_recognition)  

For Face Detection: [https://realpython.com](https://realpython.com)

For classifier training: [http://coding-robin.de/2013/07/22/train-your-own-opencv-haar-classifier.html](http://coding-robin.de/2013/07/22/train-your-own-opencv-haar-classifier.html)

For face recognition: [https://github.com/joshliu/ScandIn-Flask](https://github.com/joshliu/ScandIn-Flask). 

Project Details
===============

While there might be some trivial ways to map an office, I wanted build butler to be a little more personable so build bot can also learn and recognize faces and names. 

I will likely make the first prototype using an iRobot Create 2, Raspberry Pi 2, and a webcam. I have not selected a webcam yet but one with simple programmable servos is preferred (recommendations welcome). 

Currently I am tackling the more challenging software bits like face recognition and Jenkins/Git integration and collecting them as proof of concept code in the repo. Afterward, I will glue them together haphazardly and then clean up my code. To that point, this is a robotics project, not a framework. 

Clean code is not yet my priority but if there is a segment of interest, I would be happy to try to finalize it for you so we may collaborate.

Existing Proof of Concept Features
--------------------------
* Detecting faces on the webcam
* Selecting a best-match for the detected face
* Capturing new faces
* Speech to text for capturing new names
* Receiving Jenkins notifications
* Looking up commit author by commit hash using Github API

Needed Features
---------------
* iRobot Create wandering algorithms - Unfortunately, the iRobot Create has no knowledge of rooms/areas. The robot needs a way to remember where a person sits or to wander about.
* Need to integrate Jenkins notification receiver with facial recognition code

Desired Features
----------------
* Quadcopter support - This is no longer an open question. I have gone with the Parrot AR for it's SDK and community. I would like to find something more suitable for small, indoor spaces. Currently, I am anticipating making some simple algorithms to have the quadcopter track over/near the iRobot Create while providing the head-level video feed.
* Quadcopter hardware - While the iRobot has a way to return to its dock and recharge, I have not seen this feature on a quadcopter yet. This would be ideal for an "always ready" robot.
* Detecting unrecognized faces - Right now, the face matching is done with Euclidean arithmetic (please don't ask me what that means). The current code can pick the best match out of a list of subjects and provides a Euclidean distance which for all intents and purposes can serve as a confidence metric. This means that there is no way to know if the face is simply recognizable. My best guess now is to consider any face with an abnormally high Euclidean distance as a new face.
* Text to speech - Build butler needs a lot of pictures from a lot of people in order to get to know the team. It would be good if build butler could ask for these things on its own.
* Name - Build butler needs a names. Probably something like Hudson, Jenkins, or Jeeves. But not Travis, that would be confusing.
* Optimization - Perhaps finding people/humans prior to searching for faces

Alternatives analysis
=====================

Create2 Pros:
* Obstacle avoidance built-in
* Return-to-base pathfinding
* Charging dock
* Carrying capacity
* Lowest known cost

Create2 Cons:
* Limited to floor, requires special camera
* Existing code is closed-source, not reusable

Quadcopter Pros:
* Cooler
* Can name it BuildBug
* Very mobile
* Controlling the camera is just a matter of steering the device (no separate logic)
* Can reuse logic for household security project (something named like GuardDog, GuardianEagle, SentryBot)
* Could be swarm capable (multiple notifications, distributed weight/responsibilities, faster searching, intimidation?)

Quadcopter Cons:
* Serious weight restrictions
* No charging docks
* No obstacle detection
* Fan blades are more dangerous than Roomba wheels
* No return-to-dock built in
* Variable cost (lots of work for cheap models, potentially costly misses for expensive models )
