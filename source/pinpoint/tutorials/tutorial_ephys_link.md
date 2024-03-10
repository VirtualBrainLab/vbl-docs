# Connecting to Manipulators via Ephys Link

Pinpoint can be connected to electrophysiology manipulators
enabling experimenters to automate the placement of manipulators as well as
observe live where probes are placed inside the brain.

**In this tutorial you will learn how to:**

1. [Configure and launch Ephys Link](configure-and-launch-ephys-link)
2. [Mirror the positions of _in
   vivo_ probes in Pinpoint](ephys-link-mirror-probes)
3. [Automate insertions with Ephys Copilot](ephys-copilot)

[//]: # (**If you would like to use beta version of)

[//]: # (Ephys Link with Pinpoint, please use Steam to install Pinpoint and [switch to)

[//]: # (the `ephys-link-beta`branch]&#40;https://partner.steamgames.com/doc/store/application/branches#:~:text=To%20switch%20to%20a%20custom,be%20the%20%22BETAS%22%20tab&#41;)

[//]: # (.**)

[//]: # (To enable this feature, an instance of an Ephys Link server must be running on)

[//]: # (the local network. Please see the)

[//]: # (instructions [here]&#40;https://virtualbrainlab.org/ephys_link/installation_and_use.html#installation&#41;)

[//]: # (on how to install and run a server.)

[//]: # ()

[//]: # (<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">)

[//]: # (  <iframe src="https://www.youtube-nocookie.com/embed/QK87XBd46aQ?rel=0&modestbranding=1" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border:0;" allowfullscreen title="Overview"></iframe>)

[//]: # (</div>)

[//]: # (<br>)

(configure-and-launch-ephys-link)=

## 1. Configure and Launch Ephys Link

Ephys Link comes bundled with Pinpoint. Navigate to the "Ephys Link" tab in the
menu to configure and launch the server.

![Ephys Link configuration window](../../_static/images/tutorial/ephys_link/ephys_link_launch.png)

1. Press <kbd>ESC</kbd> or <kbd>H</kbd> to open the main menu.
2. Navigate to the "Ephys Link" tab.
3. Use the dropdown to select the manipulator platform that you are using.
4. Press the launch button to start the server. After a few seconds, you will
   see the Ephys Link window open separately and Pinpoint will establish a
   connection. Leave the Ephys Link window running in the background.
5. Your manipulators will appear here. You can configure them and link them to
   probes in the scene.
6. To disconnect from the server, press the disconnect button. The Ephys Link
   window will close as well. Ephys Link will disconnect and close automatically
   when you close Pinpoint.
7. When you are finished, press <kbd>ESC</kbd> or <kbd>H</kbd> to close the
   settings menu.

Below are more details on the configuration options for each manipulator type.

### Connecting to Sensapex Manipulators

Select the appropriate Sensapex model from the dropdown.

- "Sensapex uMp-4": 4-axis manipulators.
- "Sensapex uMp-3": 3-axis manipulators.

### Connecting to New Scale Manipulators via Pathfinder MPM Control

1. Open Pathfinder MPM.
2. Connect your manipulators.
3. Ensure
   the [HTTP server is broadcasting](https://www.newscaletech.com/sending-commands-to-pathfinder-from-other-applications/).
4. In Pinpoint, select the "New Scale Pathfinder MPM Control v2.8.8+" option
   from the dropdown.
5. A text box will appear to let you configure the port number of Pathfinder's
   HTTP server. You only need to change this value if you changed the
   broadcasting port in Pathfinder (the default of 8080 should work for most
   users).
6. Press "Launch".
7. Pinpoint will connect to Pathfinder and generate dummy probes for
   visualization in Pinpoint.

Pathfinder's configuration is automatic so there is no need to continue with the
rest of this tutorial.

### Connecting to New Scale Manipulators via M3-USB-3:1-EP

1. Select "New Scale M3-USB-3:1-EP" from the dropdown.
2. Press "Launch".
3. After the Ephys Link window opens, a second window will open to select the
   serial port that the manipulators are connected to. Select the appropriate
   port and press "OK".

### Connecting to an Existing Server Instance (Advanced)

This option is for users who have Ephys
Link [installed](https://virtualbrainlab.org/ephys_link/installation_and_use.html#installation)
and running on a separate machine than Pinpoint. This is useful for users who
have a dedicated computer for controlling manipulators or are using the hardware
stop button feature.

1. Select "Connect to Existing Server" from the dropdown.
2. Text boxes will appear to let you configure the IP address and port number of
   the server. Fill in the appropriate values and press "Connect".

(ephys-link-connection)=

## 2. Connect to Ephys Link from Pinpoint

![Connecting to Ephys Link](../../_static/images/tutorial/ephys_link/ephys_link_connection.png)

1. Press \[ESC\] to open the settings menu
2. Switch to the "Ephys Link" tab
3. Fill in the server's IP address
4. And the port number
5. Click "Connect". Upon success, the connect button will read "Disconnect"
6. Panels for each manipulator will appear here. These panels allow for the
   configuration of manipulators and linking them to probes in the scene.
7. Press \[ESC\] again to close the settings menu

(ephys-link-mirror-probes)=

## 3. Mirror the Positions of _in vivo_ Probes in Pinpoint

This step is not required for New Scale Pathfinder MPM connections. [See below
for details](mpm-no-need-config).

![Connect a probe to a manipulator](../../_static/images/tutorial/ephys_link/ephys_link_connect_probe.png)

1. Spawn the corresponding probe in the planner scene.
2. Press \[ESC\] to open the settings menu.
3. Switch to the "Ephys Link" tab.
4. Scroll down to the panel that represents the _in vivo_ manipulator.
5. Use the dropdown to configure the manipulator's handedness. As of July
   2023 configuration is necessary for Sensapex uMp manipulators only.
   Configuration is hidden for New Scale manipulators. See the section below for
   more information.
6. Use the dropdown to select a probe to link to this manipulator. Probes are
   identified by their unique ID (UUID) and their color in the scene.
7. Upon connection, the probe's stereotaxic position will be used as the zero
   coordinate that all movements will be relative to. This zero coordinate can
   be edited manually through the text boxes or by clicking the home button to
   reset the position to the current probe position.
8. The probe's offset from the brain surface and which direction it is
   calculated can be adjusted here. The offset is the distance from the probe
   tip to the brain surface. This offset can be determined as the distance from
   the tip to the brain surface along the DV axis or the probe's depth axis.
9. Manual control of the manipulators can be enabled here. This allows
   manipulators to be controlled with
   the [same keyboard shortcuts](https://virtualbrainlab.org/pinpoint/tutorial.html#keyboard)
   used to move probes in the planner around. Manipulators can also be driven
   back to their zero coordinate.
10. Press \[ESC\] again to close the settings menu.

At this point, the _in vivo_ probe positions should be mirrored in Pinpoint in
real time.

### Sensapex Handedness

Handedness determines the orientation of the manipulator and which
direction it moves. Handedness is classified by which side of the
manipulator the probe will be mounted on. Ephys Link will use this to correctly
orient the manipulator's direction.

Below is a diagram of the handedness of Sensapex manipulators. Use this to
determine the handedness of your manipulator.

![Sensapex handedness](../../_static/images/tutorial/ephys_link/sensapex_manipulators.png)

(mpm-no-need-config)=

### New Scale Pathfinder MPM connections do not require configuration

Launching Ephys Link requires specifying the type of manipulator that is being
used. Configuration in Pinpoint will differ depending on the type of
manipulator. **New Scale Pathfinder connections do not require any
configuration** in Pinpoint as all manipulators are configured in Pathfinder.
Pinpoint will automatically create probes (colored in magenta) for
each manipulator from Pathfinder and automatically echo their positions,
angles, and shank count.

## Enabling experiment automation (Ephys Copilot)

Automation is currently a beta feature that is still in development.
Please [contact](https://virtualbrainlab.org/about/overview.html) Dan or Kenneth
if you would like to try it out.