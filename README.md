# Description
Build Butler is a robot that finds whoever broke the build. One day, every software team will have a build bot, taking "visualize your build" to the next level!

## Running Build Butler
### Prerequisites
* To run the build butler, you need Pyro installed and configured
* 3-4 Terminal windows
### Starting
1. Begin by configuring and launching the Pyro name server:
~~~
# This is insecure due to an insecure server and insecure serializer method
export PYRO_SERIALIZER=pickle
export PYRO_SERIALIZERS_ACCEPTED=pickle,json,marshal,serpent
python -m Pyro4.naming
~~~
~~~
Not starting broadcast server for localhost.
NS running on localhost:9090 (127.0.0.1)
Warning: HMAC key not set. Anyone can connect to this server!
URI = PYRO:Pyro.NameServer@localhost:9090
~~~
2. Launch the build butler agent (remote sensors)
~~~
python bb_agent.py
~~~
~~~
Finished registering Pyro objects
~~~
3. Launch the build butler master (brain)
~~~
python bb_master.py 
~~~
~~~
Watching for build failures
~~~
4. Send a simulated notification from Jenkins
~~~
sh jenkinsSim.sh
~~~
~~~
Alert received
~~~
5. Return to the build butler master window to observe and test the whole state machine
6. After the alert is received, the face detection and recognition will be performed. Be sure to look square at the camera!
~~~
Received build failure alert
Initiated pathfinding
Scanning for humans
Face detected
~~~
7. You may receive this warning, please ignore it for now:
~~~
/Users/Chris/anaconda/lib/python3.5/site-packages/sklearn/utils/deprecation.py:52: DeprecationWarning: Class RandomizedPCA is deprecated; RandomizedPCA was deprecated in 0.18 and will be removed in 0.20. Use PCA(svd_solver='randomized') instead. The new implementation DOES NOT store whiten ``components_``. Apply transform to get them.
  warnings.warn(msg, category=DeprecationWarning)
~~~
8. After your face has been detected, you will be asked some questions to verify your identity and understanding
~~~
Identifying human
test_faces= ['build_butler/recognition/test_faces/last.png']
Recognized person as ' chris '. Culprit was ' chris '.
Are you chris
yes
I know, I was just being polite
You have broken the build
Do you understand
yes
Good
Fix it or be destroyed
Watching for build failures
~~~

## Architecture

### Finite State Machine
Build butler is a finite state machine (FSM) AI that utilizes human computer interaction and applied machine learning. Below is a diagram of the FSM:

<img src="https://github.com/Shumakriss/build_butler/blob/master/Build%20Butler%20FSM.png?raw=true">

### Deployment Architecture
While build butler is designed with multiple components and uses some cloud components, most of it can be deployed on one system for testing like so:

<img src="https://github.com/Shumakriss/build_butler/blob/master/Testing%20Setup.png?raw=true">

### Performance of distributed components
It should be pointed out that performance can vary heavily depending on location of the components. Currently, most processing is done on the agent or in the cloud and the master is really only responsible for the finite state machine. This architecture evolved while balancing performance of processing and data transfer. 

A better architecture is in progress could look like this:

<img src="https://github.com/Shumakriss/build_butler/blob/master/Production%20Setup.png?raw=true">


## Existing Proof of Concept Features
* Face detection
* Face recognition
* Finite State Machine (FSM) architecture
* Speech to text (STT)
* Text to speech (TTS) - OSX only
* Web server for receiving POST from Jenkins
* Remote data objects (Pyro)

#### Some Next Steps:
##### Features
* Visual debugging mode
* Migrate the text to speech module to something cross-platform
* Desktop mode (all running on Pi)
* Purchase and integrate speakers to RPi
* Purchase and mount iRobot Create
* Implement the pathfinding module and integrate into State
* Use a real Jenkins POST body (POC in sample code)

##### Bugs
* Face detection doesn't pass frame to recognition state (always uses my picture)
* Rewrite FSM to avoid stack overflow

##### Cleanup
* Move FSM to a module
* Move agent code to a module
* Cleanup modules/States - Especially recognition
* Rewrite FSM to pass data more cleanly, perhaps some global info for States
* Update PCA library
* Update Carbon Component Manager library

## Credits
This project was originally built by integrating the works of others mentioned below:

* For Speech recognition: [https://github.com/Uberi/speech_recognition](https://github.com/Uberi/speech_recognition)  
* For Face Detection: [https://realpython.com](https://realpython.com)
* For classifier training: [http://coding-robin.de/2013/07/22/train-your-own-opencv-haar-classifier.html](http://coding-robin.de/2013/07/22/train-your-own-opencv-haar-classifier.html)
* For face recognition: [https://github.com/joshliu/ScandIn-Flask](https://github.com/joshliu/ScandIn-Flask). 

## Hardware
I intend to use the following hardware for this project:
* MacBook running OSX
* Raspberry Pi 1 running Pidora
* iRobot Create (Roomba developer edition)
* Parrot AR drone (or maybe the Mambo?)
* Raspberry Pi Spy Camera https://www.adafruit.com/product/1937
* USB Wifi https://www.raspberrypi.org/products/usb-wifi-dongle/
* USB Mini microphone
* USB + 1/8 inch speaker

## Project Vision
* Generic remote RPi hardware abstraction - Tap into any sensors or media through remote API
* Generic Human-robot interaction (HRI) library - Make modules portable and configurable
* Allow build-butler configuration through HRI - (Sign up with TTS, STT, face detection, etc.)
* Integrate with a drone, perhaps pairing the carry capacity of the iRobot Create with the mobility of a mini drone (like the Parrot Mambo)
* Touch and go drone charger similar to the Create charging dock - apparently Parrot is also working on this but for industrial use
