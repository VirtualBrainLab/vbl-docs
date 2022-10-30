
# IBL Average Trial

The IBL Average Trial is a pair of tools used to explore the International Brain Laboratory's *Brain Wide Map* dataset. You can find more information at the [IBL website](https://www.internationalbrainlab.com/).

## Virtual Reality Demo



## Standalone Tool

## Development

### Installation

`cd source_dir` <br>
`git clone https://github.com/int-brain-lab/ibl-avg-trial-viz.git`

The cloned directory contains usage examples and the main event_avgs.py file that can be imported with <br>

`from ibl-avg-trial-viz.event_avgs import *`.

Must be used with the IBL's [iblenv](https://github.com/int-brain-lab/iblenv)

### Usage

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

### TODOs

- [ ] Import `load_trials_df` from **brainbox.io.one** instead of **updated_one.py** once ([#492](https://github.com/int-brain-lab/ibllib/pull/493)) is fixed. Delete **updated_one.py**
- [ ] Replace **filter_eids.py** system with Mayo's updated one.alyx.rest query in `get_bwm_sessions` that only pulls insertions with the needed files. This will mean we won't have to download everything when searching for good eids/pids. 
- [ ] Fix file paths and plots in **event_avgs_full_runs.py** and **event_avgs_testing.ipynb** that were broken by recent updates to the event averaging pipeline.
