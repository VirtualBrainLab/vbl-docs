# Pinpoint tutorial

Press [H] at any time to open the help and settings menu.

To set up a new probe, select the button on the right panel corresponding to the probe type (NP1/NP2/NP2.4). By default we transform coordinates into the IBL "Needles" space, so that AP=0, ML=0, DV=0 coordinate is placed at Bregma. The reference coordinate can be changed in the Atlas settings.

A probe **insertion** is defined by a target coordinate in the brain and a set of angles to reach that point. When you export a planned insertion Pinpoint will compute the **brain surface coordinate** and **depth** of the probe, which you will need to actually perform your experiment. 

## Controls

### Click + Drag

To control your probe left-click on the probe object. While holding the left mouse button press one of the axis keys (e.g. [W] for the AP axis) and drag the probe in space to move the probe along that axis.

### Keyboard

You can also press the keyboard keys to move the probe along that axis in 10um units. Hold **SHIFT** to move in 100um units. Hold **CTRL** to move in 1um units. Pressing and holding a key moves continuously.

![probe controls](https://github.com/dbirman/NPTrajectoryPlanner/raw/main/Images/ProbeControls.png)

Use [W/A/S/D] to move the probe along the AP or ML axis. Use [Z/X] to move the probe along the DV axis.

USe [Q/E] to rotate the probe azimuth, which corresponds to the angle of the probe manipulator relative to the brain.

Use [R/F] to change the angle of the probe on the manipulator (restricted to 0-90 deg range).

Use [1/3] to spin the probe along the axis of the probe shank. Note that NP2.4 probes spin around the leftmost probe shank when looking from the back.

Probes can be deleted with [Backspace]. To recover a probe you didn't mean to delete press [CTRL + Backspace].

## Recording region

Once the probe is at the position and angles you want, you can adjust the recording region size (in the settings) and position (using [T/G]) to match what you plan to do in your recording and adjust the insertion depth accordingly.

## Export coordinates

Click the export button to copy the probe's coordinates to your clipboard. You can paste them into another file for use during your surgery.

## Changing the active probe

When setting up multi-probe insertions you can click the probe panel or the probe model to switch which probe is active. 

## Using coordinates for surgery

To use your coordinates for a surgery, rotate the manipulator to match the azimuth angle (phi) and set the probe elevation angle (theta). Then move your probe tip to Bregma and zero your manipulator.

Translate your probe using the manipulator to match the AP/ML/DV brain surface coordinate provided by Pinpoint. If your probe is rotated off-axis use the *convert AP/ML to probe axis* setting so that you can match the Forward/Side/DV position instead. Use caution! You may reach the brain surface before you reach the DV value specified by Pinpoint, don't break your probe!

Once the probe is touching the dura, zero the depth axis and insert until you reach the specified depth.

