# Ephys Link

Pinpoint can be connected to electrophysiology manipulators
enabling experimenters to automate the placement of manipulators as well as
observe live where probes are placed inside the mouse brain.

We currently (July 2023) support Sensapex uMp-4 and New Scale 3-axis
manipulators.

**These features are only available on the Windows Desktop build of Pinpoint**
they will not run in the web browser.

[//]: # (**If you would like to use beta version of)

[//]: # (Ephys Link with Pinpoint, please use Steam to install Pinpoint and [switch to)

[//]: # (the `ephys-link-beta`branch]&#40;https://partner.steamgames.com/doc/store/application/branches#:~:text=To%20switch%20to%20a%20custom,be%20the%20%22BETAS%22%20tab&#41;)

[//]: # (.**)

To enable this feature, an instance of an Ephys Link server must be running on
the local network. Please see the
instructions [here](https://virtualbrainlab.org/ephys_link/installation_and_use.html#installation)
on how to install and run a server.

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube-nocookie.com/embed/QK87XBd46aQ?rel=0&modestbranding=1" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border:0;" allowfullscreen title="Overview"></iframe>
</div>
<br>

## Connecting to a server

![Connecting to Ephys Link](../../_static/images/Ephys-Link-connection.png)

1. Press \[ESC\] to open the settings menu
2. Switch to the "Ephys Link" tab
3. Fill in the server's IP address
4. And the port number
5. Click "Connect". Upon success, the connect button will read "Disconnect"
6. Panels for each manipulator will appear here. These panels allow for the
   configuration of manipulators and linking them to probes in the scene.
7. Press \[ESC\] again to close the settings menu

## Linking a probe in the planner to a manipulator _in vivo_

This step is not required for New Scale Pathfinder connections. See below
for details.

![Connect a probe to a manipulator](../../_static/images/Ephys-Link-connect-probe.png)

1. Spawn the corresponding probe in the planner scene.
2. Press \[ESC\] to open the settings menu.
3. Switch to the "Ephys Link" tab.
4. Scroll down to the panel that represents the _in vivo_ manipulator.
5. Use the dropdown to configure the manipulator's handedness. Currently (July
   2023), configuration is necessary for Sensapex uMp manipulators only.
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

### Sensapex Handedness

Handedness determines the orientation of the manipulator and which
direction it moves. Handedness is classified by which side of the
manipulator the probe will be mounted on. Ephys Link will use this to correctly
orient the manipulator's direction.

Below is a diagram of the handedness of Sensapex manipulators. Use this to
determine the handedness of your manipulator.

![Sensapex handedness](../../_static/images/tutorial/sensapex_manipulators.png)

### New Scale Pathfinder connections do not require configuration

Launching Ephys Link requires specifying the type of manipulator that is being
used. Configuration in Pinpoint will differ depending on the type of
manipulator. **New Scale Pathfinder connections do not require any
configuration** in Pinpoint as all manipulators are configured in Pathfinder.
Pinpoint will automatically create probes (colored in magenta) for
each manipulator from Pathfinder and automatically echo their positions and
angles.

## Enabling experiment automation (Ephys Copilot)

Automation is currently a beta feature that is still in development.
Please [contact](https://virtualbrainlab.org/about/overview.html) Dan or Kenneth
if you would like to try it out.