# Installation and Use

Pinpoint is a tool for planning electrophysiology recordings and other *in vivo* insertions, as well as tracking the position of probes in real-time inside the brain.

<image src="../_static/images/center.png" alt="overview image" position="left" style="width:100%">

Code is on our [Github repository](https://github.com/VirtualBrainLab/Pinpoint/).

<div style="padding: 15px; border: 1px solid transparent; border-color: transparent; margin-bottom: 20px; border-radius: 4px; color: #31708f; background-color: #d9edf7; border-color: #bce8f1;">
<p>Pinpoint / New Scale Webinar</p>
<p><b>Thursday Apr 18th 8AM PST/11AM EST</b> we'll be hosting a webinar with New Scale. Sign up <a href="https://r20.rs6.net/tn.jsp?f=001r45186-_W6L8rvvWnmIUDiCWp-K9_mKW8UEdjhjEer7N1W0UoTB5iTlxapxVTS8u7ey18EDsC3EChhO5_P3oOLonK1m3vrt7c_tiEhWuWDqr1OoLb07_IQDwpTlxXvWr3ntCixCi-rzfFxmVHK181ORCKEpoNDfRfHxlseEjuAbAe_hQa2du6g9zCRnmGUy0kCB0tjIXCio9RdQ5J2x38uPx1EmbcAafETVRUhaYnDSxUtZMkfxNqnWUSuOlprulOKfHr9F91jBVNZCyraMLVmqMJtcmkKNnjACbl1r1bqU=&c=aRT56swgTfpvquKmdNvKIJpyWwrSDmnWLJWC4N5FFUhdR_SCji7EAw==&ch=oT9R18qiioeHaIgMSbuA81vIoSqkLwssG1WfWDJ2mgHyAbtGDZgDFw==">here</a></p>
</div>


## Install

The easiest way to use Pinpoint is through our [web app](https://data.virtualbrainlab.org/Pinpoint/).

### Standalone builds

Our recommended source for the latest Windows and Linux Desktop builds is through [Pinpoint on Steam](https://store.steampowered.com/app/2434260/Pinpoint/), downloading via Steam ensures your client will always stay up to date. Please note that the standalone Pinpoint builds require an internet connection at startup to download and cache the reference atlas data. Once cached, you can relaunch Pinpoint with no connection to the internet.

You can also find minor releases and release notes on the [releases page](https://github.com/VirtualBrainLab/Pinpoint/releases).

If you need to use an older release of Pinpoint, you can find them by navigating to our [data website](https://data.virtualbrainlab.org/), by using the version tagged Beta branches on Steam, or by downloading older releases from the Github pages. 

### Additional linux instructions

Steam builds on Linux should launch automatically.

To run the linux executable from the Github release, you need to go to the unzipped folder and run `chmod +x` on the .x86_64 file. Some users may run into permissions issues, in which case running `chown -R yourusername .` from within the folder should repair those.

## Instructions

Please see the [tutorials](https://virtualbrainlab.org/pinpoint/tutorial.html) pages for instructions.

## Troubleshooting

The most common cause of Pinpoint not loading is that your browser is blocking the data from downloading. Disabling plugins that interfere with javascript often resolves these issues (e.g. ad blocking plugins).

If you encounter issues after an update, you may need to clear your browser's cache or download the latest release.

## Bugs

Please report issues on the [issues page](https://github.com/VirtualBrainLab/Pinpoint/issues).

## Citing

A preprint describing Pinpoint has been [published on bioRxiv](https://www.biorxiv.org/content/10.1101/2023.07.14.548952). The paper provides an introduction to the key features and it can be used as a citation if Pinpoint proves integral to a scientific publication.
