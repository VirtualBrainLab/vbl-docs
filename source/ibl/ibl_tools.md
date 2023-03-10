
# IBL Tools

## IBL Website

As part of the International Brain Laboratory's [public data website](https://viz.internationalbrainlab.org) we created two interactive 3D tools. You can see them in action on the site!

### Mini Brain

<image src="../_static/images/trial_viewer/mini_brain.png" alt="overview image" position="left" style="width:100%">

The Mini Brain is a widget that lets you select different probe insertions from the Brain Wide Map and explore the alignment of the insertion within the 3D mouse brain.

### Trial Viewer

<image src="../_static/images/trial_viewer/trial_viewer.png" alt="overview image" position="left" style="width:100%">

The Trial Viewer is an interactive component that lets you re-play the metadata recorded during a session, including the stimulus position, wheel movements, sounds, and the videos. These are rendered in a cartoon 3D environment with the deeplabcut output overlayed on the videos. 

## IBL Average Trial

The IBL Average Trial is a pair of tools used to explore the International Brain Laboratory's *Brain Wide Map* dataset. You can find more information at the [IBL website](https://www.internationalbrainlab.com/).

### Virtual Reality Demo

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube-nocookie.com/embed/kcBHoQBtzZE?rel=0&modestbranding=1" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border:0;" allowfullscreen title="VR Demo Reel"></iframe>
</div>
<br>

### Standalone Tool

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube-nocookie.com/embed/xlwDX_17o20?rel=0&modestbranding=1" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border:0;" allowfullscreen title="VR Demo Reel"></iframe>
</div>
<br>

#### Download 
The standalone IBL *neuron explorer* can be download [here](https://drive.google.com/file/d/1Iw5ENIheBoSuD5pJzozvjASN-N7PDnM4/view?usp=share_link), Windows-only for now. Eventualily we will integrate this into the IBL data portal.

### Development

#### Installation

`cd source_dir` <br>
`git clone https://github.com/int-brain-lab/ibl-avg-trial-viz.git`

The cloned directory contains usage examples and the main event_avgs.py file that can be imported with <br>

`from ibl-avg-trial-viz.event_avgs import *`.

Must be used with the IBL's [iblenv](https://github.com/int-brain-lab/iblenv)

#### Usage

See the API reference for more detailed function documentation and examples.

<p align="center">
  <img src="https://raw.githubusercontent.com/int-brain-lab/ibl-avg-trial-viz/main/examples/img/event_avgs_flow_diagram.png?token=GHSAT0AAAAAABTCBECVGXUWA2BD6EZGZGWUYX5GB6A" width="75%"/>
</p>

examples/**event_avgs_full_runs.py** will run the pipeline on all insertions in the brainwide map and output event averages for raw spikes, baselined spikes, baselined and normalized spikes, and fano factor. The script also contains the (untested) code to generate the average raw spikes timelocked to different events. At the top of this 

examples/**event_avgs_testing.ipynb** contains visualizations of output data including baseline normalized event averaged spike rates for clusters in different regions:

<p display="flex">
  <img src="https://raw.githubusercontent.com/int-brain-lab/ibl-avg-trial-viz/main/examples/img/baselined_normed_PSV_frs.png?token=GHSAT0AAAAAABTCBECU4I7BOEORRE6OLQDIYX5GDHQ" width="49%"/>

  <img src="https://raw.githubusercontent.com/int-brain-lab/ibl-avg-trial-viz/main/examples/img/cluster_mlapdv.png?token=GHSAT0AAAAAABTCBECUBBEVTC2QODXWH4O2YX5GCSA" width="49%"/>
</p>