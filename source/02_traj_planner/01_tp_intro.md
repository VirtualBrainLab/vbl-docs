# Installation and Use

Pinpoint is a tool for planning Neuropixels recordings with up to sixteen 1.0, 2.0, or up to four 4-shank 2.0 probes.

![Azimuth example](https://github.com/dbirman/NPTrajectoryPlanner/raw/main/Images/2022_04_21.png)

Code is on our [Github repository](https://github.com/dbirman/NPTrajectoryPlanner/).

## Known issues

### Alignment

The CCF atlas is not aligned with the in vivo mouse brain. We transform the CCF to try to account for this, but please read the alignment section for details and make sure you understand what is happening before performing a surgery. 

## Install

The easiest way to use the trajectory planner is through our [web app](http://data.virtualbrainlab.org/Pinpoint/).

If you encounter issues please try refreshing the page (sometimes the 3D mesh files don't download on the first load). If that fails, disable any plugins that might be interfering with javascript (e.g. ad blockers).

### Standalone builds

You can also download a Desktop build from the ![releases page](https://github.com/VirtualBrainLab/NPTrajectoryPlanner/releases). We can build for linux on request.

<!-- ### Additional linux instructions

To run the linux executable you need to go to the unzipped folder and run `chmod +x` on the .x86_64 file. Some users may run into permissions issues, in which case running ` chown -R yourusername .` from within the folder should repair those. -->

<!-- ### Additional mac instructions

The mac executable currently only runs on MacOS **Mojave** and earlier. You will probably have a security issue because the app is unsigned. Go to Systems Preferences > Security & Privacy > General and allow the file to "run anyway".  -->

## Instructions for use

To set up a new probe, select the button on the right panel corresponding to the probe type (NP1/NP2/NP2.4). By default we transform coordinates into the IBL "Needles" space, so that AP=0, ML=0, DV=0 coordinate is placed at Bregma. This setting can be disabled in the settings (under Atlas).

A probe **insertion** is defined by a target coordinate in the brain and a set of angles to reach that point. When you export a planned insertion Pinpoint will compute the **brain surface coordinate** and **depth** of the probe, which you will need to actually perform your experiment. 

At any time you can press [M] to open the manual coordinate entry window and enter coordinates directly. 

### Controls

#### Click + Drag

To control your probe left-click on the probe object. While holding the left mouse button press one of the axis keys (e.g. [W] for the AP axis) and drag the probe in space to move the probe along that axis.

#### Keyboard

You can also press any of the keyboard keys to move the probe along that axis in 10um units. Hold **SHIFT** to move in 100um units. Hold **CTRL** to move in 1um units. Pressing and holding a key will move continuously.

![probe controls](https://github.com/dbirman/NPTrajectoryPlanner/raw/main/Images/ProbeControls.png)

Use [W/A/S/D] to move the probe along the AP or ML axis. Use [Z/X] to move the probe along the DV axis.

USe [Q/E] to rotate the probe azimuth, which corresponds to the angle of the probe manipulator relative to the brain.

Use [R/F] to change the angle of the probe on the manipulator (restricted to 0-90 deg range).

Use [1/3] to spin the probe along the axis of the probe shank. Note that NP2.4 probes spin around the leftmost probe shank when looking from the back.

Probes can be deleted with [Backspace]. To recover a probe you didn't mean to delete press [CTRL + Backspace].

### Recording region

Once the probe is at the position and angles you want, you can adjust the recording region size (in the settings) and position (using [T/G]) to match what you plan to do in your recording and adjust the insertion depth accordingly.

### Export coordinates

Clicking on the coordinates shown at the bottom of the screen copies them to the clipboard. If the azimuth angle is not at 0/90/180 use the "convert AP/ML to probe axis" setting to export the position along the probe forward/side axis.

### Changing the active probe

When setting up multi-probe insertions you can click the probe panel, the probe model, or the probe coordinate text to set that probe to active. 

## Using coordinates for surgery

To use your coordinates for a surgery, rotate the manipulator to match the azimuth angle and set the probe elevation angle. Then move your probe tip to Bregma and zero your manipulator.

Translate your probe using the manipulator to match the AP/ML/DV brain surface coordinate provided by Pinpoint. If your probe is rotated off-axis use the *convert AP/ML to probe axis* setting so that you can match the Forward/Side/DV position instead. Depending on your craniotomy you may reach the brain surface before you reach the DV value specified by Pinpoint, don't break your probe!

Once the probe is touching the dura, zero the depth axis and insert until you reach the specified depth.

### Sensapex Link

Coming soon...

## Saving and loading probes

You can save the coordinates of an insertion for future use by clicking on the coordinate text. This copies the active probe coordinates to a string.

## Bugs

Please report issues on the [issues page](https://github.com/dbirman/NPTrajectoryPlanner/issues).


<!-- ## Settings -->

<!-- **Reset active probe** - Returns the active probe to the original starting position (Bregma by default)

**Spawn IBL probes** - Places two NP1.0 probes in the configuration used by the IBL

**Detect collisions** - Warns the user when two probes are colliding on their shank or on their probe holders

**Set (0,0,0) to Bregma** - On: sets the 0,0,0 coordinate to Bregma, or to the 0,0,0 CCF coordinate when unchecked (default: on)

**Depth from brain surface** - On: measures insertion depth from the brain surface, Off: from the DV=0 plane (default: on)

**Sagittal/Coronal slices** - Dropdown menu allows you to choose different volumes to slice. The annotation dataset is the most useful for trajectory planning.

**Display area acronyms** - On: show only acronyms for brain areas (default: off)

**Areas include layers** - On: include the layers (e.g. in cortex) (default: on)

**Rig** - Dropdown with options for rigs to display

**Recording region only** - On: display only the areas within the recording region, Off: show the areas along the whole probe shank (default: on)

**Recording region size** - Slider controls the size of the recording region. Defaults to a set of options that depend on the probe.

**Display In-Plane Slice** - On: shows a slice of cortex that is "in-plane" with the probe, note that this uses a camera that is looking at the probe from the "front", i.e. towards the electrodes (default: on)

**Convert AP/ML to probe** - On: when the probe manipulator is off of the 0/90 axis the AP/ML positions are not useful for calculating the insertion point relative to Bregma with a regular manipulator, turn this on to display the position along the probe forward/side axes (default: off)

**Use stereotaxic coordinates** - On: displays the **s**tereo**t**axic stAP, stML, and stDV coordinates instead of the CCF space coordinates. (default: off)

**Craniotomy** - On: opens a window that allows the user to control the skull craniotomy window, use with the Rig: Skull dropdown option (default: off)

**IBL map** - On: displays a sphere at the location of each remaining second pass map location, clicking on a sphere moves the active probe controller to that location. You must set the depth value by hand (click probe, press [Z/X], then drag down; or just press [Z/X]) -->

## References

Inspired by Andy Peters' trajectory explorer https://github.com/petersaj/neuropixels_trajectory_explorer. 

CCF Atlas downloaded from http://download.alleninstitute.org/informatics-archive/current-release/mouse_ccf/annotation/ 

Mouse brain artwork from https://scidraw.io/drawing/286

## Citing

If this project is used as part of a research project you should cite this repository. Please email Dan (dbirman@uw.edu) and we can set up a DOI for the version you are using.
