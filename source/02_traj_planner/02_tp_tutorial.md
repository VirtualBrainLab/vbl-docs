# Tutorial

Press [H] at any time to open the help and settings menu.

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube-nocookie.com/embed/uzKulUziWFI?rel=0&modestbranding=1" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border:0;" allowfullscreen title="Overview"></iframe>
</div>
<br>

## Overview

<image src="../_static/images/tutorial/overview.png" alt="overview image" position="left" style="width:100%">

Pinpoint presents you with an interactive 3D scene where you can plan and test different probe insertion trajectories. The scene view shows the mouse brain **(1)** composed of 3D models built from the Allen Common Coordinate Framework annotations and **(2)** the probe 3D model, showing in white the active recording region. The scene view and probe can be rotated and moved by clicking and dragging with your mouse, see the section titled *Controls*, below. **(3)** The rotation gizmo helps you understand the orientation of the brain, with Yellow representing the Dorsal-Ventral axis, Red the Anterior-Posterior axis, and blue the Left-Right (or Medial-Lateral) axis. Double-clicking the gizmo will snap the camera view to the corresponding planar view (i.e. Axial, Coronal, and Sagittal).

Pinpoint interpolates the recording region on the probe in two viewports to help you understand where your electrodes are placed in the brain. The probe UI **(4)** shows you a linear interpolation through the recording region. The in-plane slice **(5)** shows you a view of not only the probe but also the surrounding regions. You can click regions in the in-plane slice to highlight them in the 3D scene. You can also highlight regions of interest by searching for them in the search panel **(6)**. Click a region turns it on and off and pressing the *Clear* button removes all highlighted regions. The *snap-to-area* button (downward arrrow) moves the probe tip to the center of that region.

To set up a new probe, select the corresponding button the new probe panel **(7)**. By default, probes are spawned at Bregma. You can change the reference coordinate in the *Atlas* settings. When you have multiple probes in the scene you can click on the probe objects to switch the *active* probe, or you can click on the probe panels on the left side of the screen.

The coordinates of a probe are shown in the last panel **(8)** and can be copied to the clipboard using the download icon at the top right. When the probe is outside of the brain we display the tip coordinate and angles. When the probe is inside the brain Pinpoint computes for you the *brain surface coordinate* and *depth* of the probe, which are the coordinates you would need to re-create an insertion. See the 

A probe **insertion** is defined by a target coordinate in the brain and a set of angles to reach that point. When you export a planned insertion Pinpoint will compute the **brain surface coordinate** and **depth** of the probe, which you will need to actually perform your experiment. 

## Camera controls

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube-nocookie.com/embed/Lj7YQGq4NWE?rel=0&modestbranding=1" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border:0;" allowfullscreen title="Overview"></iframe>
</div>
<br>

## Probe controls

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube-nocookie.com/embed/-W7r9d5SKzM?rel=0&modestbranding=1" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border:0;" allowfullscreen title="Overview"></iframe>
</div>
<br>

### Click + Drag

To control your probe left-click on the probe object. While holding the left mouse button press one of the axis keys and drag the probe in space to move the probe along that axis. The axis keys are [W/S] for AP, [A/D] for ML, [Q/E] for DV, and [Z/X] for depth.

<image src="../_static/images/tutorial/controls.png" alt="overview image" position="left" style="width:100%">

### Keyboard

You can also press the keyboard keys to move the probe along that axis in 10um units. Hold **SHIFT** to move in 100um units. Hold **CTRL** to move in 1um units. Pressing and holding a key moves continuously.

![probe controls](https://github.com/dbirman/NPTrajectoryPlanner/raw/main/Images/ProbeControls.png)

Use [W/A/S/D] to move the probe along the AP or ML axis. Use [Z/X] to move the probe along the DV axis.

USe [Q/E] to rotate the probe azimuth, which corresponds to the angle of the probe manipulator relative to the brain.

Use [R/F] to change the angle of the probe on the manipulator (restricted to 0-90 deg range).

Use [1/3] to spin the probe along the axis of the probe shank. Note that NP2.4 probes spin around the leftmost probe shank when looking from the back.

Probes can be deleted with [Backspace]. To recover a probe you didn't mean to delete press [CTRL + Backspace].

### Recording region

Once the probe is at the position and angles you want, you can adjust the recording region size (in the settings) and position (using [T/G]) to match what you plan to do in your recording and adjust the insertion depth accordingly.

## Help and settings

<image src="../_static/images/tutorial/help.png" alt="overview image" position="left" style="width:100%">

The help and settings menu is accessed by pressing **H**. Press H again to close the window. The tabs **(1)** on the left side switch between the different sub-menus.

### Designing a trajectory and probe coordinates

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube-nocookie.com/embed/T1ZVcbwLCVw?rel=0&modestbranding=1" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border:0;" allowfullscreen title="Overview"></iframe>
</div>
<br>
 
### Rig components

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube-nocookie.com/embed/pcwMFFWdbG4?rel=0&modestbranding=1" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border:0;" allowfullscreen title="Overview"></iframe>
</div>
<br>

### Areas & Atlas options

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube-nocookie.com/embed/qLoy63HSswA?rel=0&modestbranding=1" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border:0;" allowfullscreen title="Overview"></iframe>
</div>
<br>
 

### Ephys Link

### Account

## Surgery

To use your coordinates for a surgery, rotate the manipulator to match the azimuth angle (phi) and set the probe elevation angle (theta). Then move your probe tip to Bregma and zero your manipulator.

Translate your probe using the manipulator to match the AP/ML/DV brain surface coordinate provided by Pinpoint. If your probe is rotated off-axis use the *convert AP/ML to probe axis* setting so that you can match the Forward/Side/DV position instead. Use caution! You may reach the brain surface before you reach the DV value specified by Pinpoint, don't break your probe!

Once the probe is touching the dura, zero the depth axis and insert until you reach the specified depth.

