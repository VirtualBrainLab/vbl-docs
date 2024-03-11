# Automate Experiments with Ephys Copilot

<div style="padding: 15px; border: 1px solid transparent; border-color: transparent; margin-bottom: 25px; border-radius: 4px; color: #8F5031; background-color: #F7E3D9; border-color: #F1C5BC;">
<p><b>Ephys Copilot is still in Early Beta!</b></p>
<p>This is an internal document for Steinmetz Lab members to reference.</p>
<p>Please <a href="https://virtualbrainlab.org/about/overview.html">contact</a> Dan or Kenneth if you would like to try it out.</p>
</div>

**Overview**

1. Launch Pinpoint
2. Create/Load experiment
3. Create dummy probes for visualization
4. Launch Ephys Link
5. Configure manipulators
6. Connect dummy probes to manipulators
7. Activate Copilot
8. Calibrate manipulators to Bregma
9. Drive manipulators to target
10. Calibrate to the Dura
11. Punch through the Dura
12. Drive to target depth
13. Record data
14. Return to the surface
15. Clean up

## 1. Launch Pinpoint

1. Double-click the Pinpoint icon on the desktop to launch the application.

   ![Pinpoint icon](../../_static/images/tutorial/ephys_copilot/pinpoint_icon.png)

2. Wait until you see the brain in the middle of the screen. The app may take a
   while to open if it is updating. You may need to switch to it if other
   windows are in front.

## 2. Create/Load experiment

Use the accounts system to log in and load an experiment.

TODO: Add more details once accounts are operational.

## 3. Create dummy probes for visualization

1. Click the "Add new probe" button in the top right corner of the screen:

   ![Add new probe](../../_static/images/tutorial/ephys_copilot/add_new_probes_btn.png)

2. Select the type of probe you want to create:

   ![Select probe type](../../_static/images/tutorial/ephys_copilot/select_probe_type.png)

3. Set your probe's angles using the text boxes to match your manipulator's
   angles:

   ![Set probe angles](../../_static/images/tutorial/ephys_copilot/set_probe_angles.png)
    1. Angles of 0, 0, 0 represent a probe that is parallel to
       the ground, pointing anteriorly, and probe head stage is facing
       ventrally. A pitch of 90 degrees would point the probe straight down.
4. Repeat steps 1 - 3 for each manipulator you will be using.
    1. You can click the colored square to change the color of the probe in the
       scene.
       ![img.png](../../_static/images/tutorial/ephys_copilot/probe_color_btn.png)

## 4. Launch Ephys Link

1. Press <kbd>ESC</kbd> to open the main menu.
2. Switch to the "Ephys Link" tab.
   ![img.png](../../_static/images/tutorial/ephys_copilot/ephys_link_tab.png)
3. Set the dropdown to "Sensapex uMp-4" (it should be by default) and press the
   launch button.
   ![img.png](../../_static/images/tutorial/ephys_copilot/ephys_link_launch.png)
4. After a few seconds, you will see the Ephys Link window open separately and
   Pinpoint will establish a connection. Leave the Ephys Link window running in
   the background.
5. Your manipulators will appear as separate panels in the Ephys Link window.
   ![img.png](../../_static/images/tutorial/ephys_copilot/ephys_link_connected.png)

## 5. Configure manipulators

1. Set the handedness of each manipulator by selecting it from the dropdown.
   ![img.png](../../_static/images/tutorial/ephys_copilot/handedness_dropdown.png)
    1. Handedness determines the orientation of the manipulator and which
       direction it moves. Handedness is classified by which side of the
       manipulator the probe will be mounted on. Ephys Link will use this to
       correctly orient the manipulator's direction. Below is a diagram of the
       handedness of Sensapex manipulators. Use this to determine the handedness
       of your manipulator.
       ![Sensapex handedness](../../_static/images/tutorial/ephys_link/sensapex_manipulators.png)

## 6. Connect dummy probes to manipulators

1. Click the dropdown by "Link Probe" and select the probe you want to link to
   the manipulator.
   ![img.png](../../_static/images/tutorial/ephys_copilot/link_probe_dropdown.png)

2. Repeat for each manipulator _in vivo_. There should be a 1:1 pairing of
   dummy probes to manipulators.
3. You should end up with something like this:
   ![img.png](../../_static/images/tutorial/ephys_copilot/linked_probes.png)

## 7. Activate Copilot

1. Press the Enable Copilot Checkbox to activate the Copilot panel. The Copilot
   Panel opens behind the settings panel.
   ![img.png](../../_static/images/tutorial/ephys_copilot/enable_copilot.png)<br><br>
2. Close the menu by pressing <kbd>ESC</kbd> to see the Copilot panel.
   ![img.png](../../_static/images/tutorial/ephys_copilot/copilot_panel_solo.png)