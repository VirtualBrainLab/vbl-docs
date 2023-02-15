# IBL Avg Trial

## Installation

`cd source_dir` <br>
`git clone https://github.com/int-brain-lab/ibl-avg-trial-viz.git`

The cloned directory contains usage examples and the main event_avgs.py file that can be imported with <br>

`from ibl-avg-trial-viz.event_avgs import *`.

Must be used with the IBL's [iblenv](https://github.com/int-brain-lab/iblenv)

## Usage

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