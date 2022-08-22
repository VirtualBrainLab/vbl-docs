# Electrophysiology Manipulator Link (Ephys Link)

Pinpoint can be connected to Sensapex manipulators enabling experimenters to automate the placement of manipulators as well as observe live where probes are placed inside the mouse brain.

To enable this feature, an instance of an Ephys Link server must be running on the local network. Please see the instructions [here](https://virtualbrainlab.org/05_misc/03_ephys_link.html#installation) on how to install and run a server. 

## Connecting to a server

1. Press [H] to open the settings menu
2. Switch to the "Ephys Link" tab
3. Fill in the server's IP address and port number
4. Click connect. Upon success, the connect button will read "disconnect"
5. If manipulators are detected, set their handedness
   1. Handedness determines the orientation of the manipulator and which direction it moves (click on the [?] button for more information)
6. Press [H] again to close the settings menu

## Linking a probe in the planner to a manipulator in real life

1. Spawn the corresponding probe (NP 1.0/2.0/2.4) in the planner scene
2. Press [H] to open the settings menu
3. Switch to the "Sensapex Link" tab
4. Using the dropdown for each probe, select the desired manipulator to connect to
   1. Only manipulators that are connected to the server *and* have their handedness set will be listed
5. Set the angles of the manipulator/probe in the experiment
6. Set a custom Bregma offset (if needed)
7. Press "Connect" and confirm the manipulator is at Bregma to complete the connection

## Quick settings

Quick settings for the active probe are found at the bottom of the right-hand panel stack. There, a probe's position to Bregma and offset from brain surface can be reset.