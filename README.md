Build Butler is a robot that finds whoever broke the build. 

*Disclaimer*
This repo is largely full of example code that has been borrowed and cobbled together like a bunch of Legos. I still need to list some references so assume that most of the code is not mine. The idea, collection, and integration of the examples is mine, however, and the code was all obtained freely from open source projects.

While there might be some trivial ways to map an office, I wanted build butler to be a little more personable so build bot can also learn and recognize faces and names. 

I will likely make the first prototype using an iRobot Create 2, Raspberry Pi 2, and a webcam. I have not selected a webcam yet but one with simple programmable servos is preferred (recommendations welcome). 

Currently I am tackling the more challenging software bits like face recognition and Jenkins/Git integration and collecting them as proof of concept code in the repo. Afterward, I will glue them together haphazardly and then clean up my code. To that point, this is a robotics project, not a framework. 

Clean code is not yet my priority but if there is a segment of interest, I would be happy to try to finalize it for you so we may collaborate.

Proof of Concept Features:
* Detecting faces on the webcam
* Selecting a best-match for the detected face
* Capturing new faces
* Speech to text for capturing new names
* Receiving Jenkins notifications
* Looking up commit author by commit hash using Github API

Needed Features:
* iRobot Create wandering algorithms - Unfortunately, the iRobot Create has no knowledge of rooms/areas. The robot needs a way to remember where a person sits or to wander about.
* Need to integrate Jenkins notification receiver with facial recognition code

Desired Features:
* Quadcopter support - I need to select the right device. I am looking for hacker-friendly models. There was a kickstarter for this to create something like the iRobot Create but as a quadcopter but it failed to reach its funding target. There are a couple popular alternatives like the CrazyFlie and Parrot AR drone which are basically the low-cost but very minimal and high-cost but low effort approaches, respectively. Recommendations welcome!
* Detecting unrecognized faces - Right now, the face matching is done with Euclidean arithmetic (please don't ask me what that means). The current code can pick the best match out of a list of subjects and provides a Euclidean distance which for all intents and purposes can serve as a confidence metric. This means that there is no way to know if the face is simply recognizable. My best guess now is to consider any face with an abnormally high Euclidean distance as a new face.
* Text to speech - Build butler needs a lot of pictures from a lot of people in order to get to know the team. It would be good if build butler could ask for these things on its own.
* Name - Build butler needs a names. Probably something like Hudson, Jenkins, or Jeeves. But not Travis, that would be confusing.

Alternatives analysis

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
* Very mobile
* Controlling the camera is just a matter of steering the device (no separate logic)

Quadcopter Cons:
* Serious weight restrictions
* No charging docks
* No obstacle detection
* Fan blades are more dangerous than Roomba wheels
* No return-to-dock built in
* Variable cost (lots of work for cheap models, potentially costly misses for expensive models )