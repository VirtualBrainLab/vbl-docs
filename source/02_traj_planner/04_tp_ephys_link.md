# Ephys Manipulator Link

Pinpoint can be connected to Sensapex manipulators enabling experimenters to automate the placement of manipulators as well as observe live where probes are placed inside the mouse brain.

To enable this feature, an instance of an Ephys Link server must be running on the local network. Please see the instructions [here](https://virtualbrainlab.org/05_misc/03_ephys_link.html#installation) on how to install and run a server. 

## Connecting to a server

![Connecting to Ephys Link](../_static/images/Ephys-Link-connection.png)

1. Press \[H\] to open the settings menu
2. Switch to the "Ephys Link" tab
3. Fill in the server's IP address
4. And the port number
5. Click "Connect". Upon success, the connect button will read "Disconnect"
6. Manipulators by default spawn as "left-handed". Use the drop-down menu to change the handedness of each detected manipulator.
 1. Handedness determines the orientation of the manipulator and which direction it moves. Handedness is determined by which side of the manipulator the probe will be mounted on.
 2. Example of a left-handed manipulator: ![Left Handed Manipulator](../_static/images/Sensapex-uMp4-LEFT.jpg)
 3. Example of a right-handed manipulator: ![Right Handed Manipulator](../_static/images/Sensapex-uMp4-RIGHT.jpg)
7. Press \[H\] again to close the settings menu

## Linking a probe in the planner to a manipulator in real life

![Connect a probe to a manipulator](../_static/images/Ephys-Link-connect-probe.png)

1. Spawn the corresponding probe (NP 1.0/2.0/2.4) in the planner scene
2. Press \[H\] to open the settings menu
3. Switch to the "Ephys Link" tab
4. Using the dropdown for each probe, select the desired manipulator to connect to. Only manipulators that are connected to the server will be listed.
5. Upon connection, the probe's stereotaxic position will be used as the zero coordinate all movements will be relative to. This zero position can be edited manually through the text boxes or by clicking the home button to reset the position to the current probe position.
6. The probe's offset from the brain surface and which direction it is calculated can be adjusted here. The offset is the distance from the probe tip to the brain surface. This offset can be determined as the distance from the tip to the brain surface along the DV axis or the probe's depth axis.

## Quick settings

Quick settings for the active probe are found at the bottom of the right-hand panel stack. There, a manipulator's position, angles, zero coordinate, and offset from the brain can be set.

- Use the text boxes to edit and position and angles of the probe.
- Use the down arrow button to set the offset from the brain surface and drop the probe to the brain surface.
- Use the home button to reset the probe's position to the current probe position.