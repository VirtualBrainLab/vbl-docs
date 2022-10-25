# Installation and Use

Pinpoint is a tool for planning Neuropixels recordings with up to sixteen 1.0, 2.0, or up to four 4-shank 2.0 probes.

![Azimuth example](https://github.com/dbirman/NPTrajectoryPlanner/raw/main/Images/2022_04_21.png)

Code is on our [Github repository](https://github.com/dbirman/NPTrajectoryPlanner/).

## Install

The easiest way to use the trajectory planner is through our [web app](http://data.virtualbrainlab.org/Pinpoint/).

If you encounter issues please try refreshing the page (sometimes the 3D mesh files don't download on the first load). If that fails, disable any plugins that might be interfering with javascript (e.g. ad blockers).

### Standalone builds

Windows desktop builds are available on the ![releases page](https://github.com/VirtualBrainLab/NPTrajectoryPlanner/releases).

<!-- ### Additional linux instructions

To run the linux executable you need to go to the unzipped folder and run `chmod +x` on the .x86_64 file. Some users may run into permissions issues, in which case running ` chown -R yourusername .` from within the folder should repair those. -->

<!-- ### Additional mac instructions

The mac executable currently only runs on MacOS **Mojave** and earlier. You will probably have a security issue because the app is unsigned. Go to Systems Preferences > Security & Privacy > General and allow the file to "run anyway".  -->

## Instructions for use

Please see the [tutorials](https://virtualbrainlab.org/02_traj_planner/02_tp_tutorial.html) pages for instructions.

## Troubleshooting

The most common cause of Pinpoint not loading is that your browser is blocking the data from downloading. Disabling plugins that interfere with javascript often resolves these issues (e.g. ad blocking plugins)

## Bugs

Please report issues on the [issues page](https://github.com/dbirman/NPTrajectoryPlanner/issues).

## References

Inspired by Andy Peters' [trajectory explorer](https://github.com/petersaj/neuropixels_trajectory_explorer). 

CCF Atlas downloaded from the [Allen data portal](http://download.alleninstitute.org/informatics-archive/current-release/mouse_ccf/annotation/)

Mouse brain artwork from [Scidraw](https://scidraw.io/drawing/286)

## Citing

If this project is used as part of a research project you should cite this repository. Please email Dan (dbirman@uw.edu) and we can set up a DOI for the version you are using.