# Description
Build Butler is a robot that finds whoever broke the build. One day, every software team will have a build bot, taking "visualize your build" to the next level!

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
* Migrate the text to speech module to something cross-platform
* Migrate the master script to Pyro-objects
  * Migrate STT module to Pyro (Pi does STT, sends text back)
* Improve recognition library
  * Easier to tune
  * Adjust to greatest common number of images
  * Adjust to greatest common image size
* Purchase and integrate speakers to RPi
* Purchase and mount iRobot Create
* Implement the pathfinding module and integrate into State
* Use a real Jenkins POST body (POC in sample code)

##### Cleanup
* Move FSM to a module
* Move agent code to a module
* Cleanup modules/States - Especially recognition
* Rewrite FSM to avoid stack overflow
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
* Touch and go drone charger similar to the Create charging dock - apparently Parrot is also working on this!
