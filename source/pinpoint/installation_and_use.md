# Installation and Use

Pinpoint is a tool for planning Neuropixels recordings with up to sixteen 1.0, 2.0, or up to four 4-shank 2.0 probes.

<image src="../_static/images/center.png" alt="overview image" position="left" style="width:100%">

Code is on our [Github repository](https://github.com/VirtualBrainLab/Pinpoint/).

<!-- <div style="padding: 15px; border: 1px solid transparent; border-color: transparent; margin-bottom: 20px; border-radius: 4px; color: #31708f; background-color: #d9edf7; border-color: #bce8f1;">
<p>Pinpoint will be at SfN 2022!</p>
<p><b>Saturday Nov 12th 1pm-5pm</b> we'll be at poster 088.07</p>
<p><b>Sunday Nov 13th 6:30pm-9pm</b> we'll be at the <i>Tools, Tech and Theory: BRAIN Initiative Alliance Social</i> at the Bayfront hotel with the full rig demo set up.</p>
</div> -->


## Install

The easiest way to use Pinpoint is through our [web app](https://data.virtualbrainlab.org/Pinpoint/).

If you encounter issues please try refreshing the page (sometimes the 3D mesh files don't download on the first load). If that fails, disable any plugins that might be interfering with javascript (e.g. ad blockers).

### Standalone builds

Windows desktop builds are available on the [releases page](https://github.com/VirtualBrainLab/Pinpoint/releases).

Linux and Mac builds available on request.

<!-- ### Additional linux instructions

To run the linux executable you need to go to the unzipped folder and run `chmod +x` on the .x86_64 file. Some users may run into permissions issues, in which case running ` chown -R yourusername .` from within the folder should repair those. -->

<!-- ### Additional mac instructions

The mac executable currently only runs on MacOS **Mojave** and earlier. You will probably have a security issue because the app is unsigned. Go to Systems Preferences > Security & Privacy > General and allow the file to "run anyway".  -->

## Instructions

Please see the [tutorials](https://virtualbrainlab.org/02_traj_planner/02_tp_tutorial.html) pages for instructions.

## Troubleshooting

The most common cause of Pinpoint not loading is that your browser is blocking the data from downloading. Disabling plugins that interfere with javascript often resolves these issues (e.g. ad blocking plugins).

The second common issue is not using **https** to access the site, this is required for the data to download properly.

## Bugs

Please report issues on the [issues page](https://github.com/VirtualBrainLab/Pinpoint/issues).

## References

Inspired by Andy Peters' [trajectory explorer](https://github.com/petersaj/neuropixels_trajectory_explorer). 

CCF Atlas downloaded from the [Allen data portal](http://download.alleninstitute.org/informatics-archive/current-release/mouse_ccf/annotation/)

Mouse brain artwork from [Scidraw](https://scidraw.io/drawing/286)

## Citing

<a href="https://doi.org/10.5281/zenodo.7312786"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.7312786.svg" alt="DOI"></a>

Your citations are critical for making it possible to get grant funding for Pinpoint in the future.