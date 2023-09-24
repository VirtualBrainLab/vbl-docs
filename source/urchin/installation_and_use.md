# Installation and Use

<p float="left">
 <img src="../static/images/urchin/exploded.png" width="25%"> 
 <img src="../static/images/urchin/exploded_onesided.png" width="25%"> 
 <img src="../static/images/urchin/repro_ephys.png " width="35%">
</p>

<p float="center">
 <img src="../static/images/urchin/brain_rotate_cropped.gif" width="45%"> 
</p>

The Universal Renderer for Neuroscience (Urchin) allows you to connect your Python scripts to a standalone rendering program, to create graphics like the ones above.

## Install

```
pip install oursin
```

No additional installation is required if you plan to run Urchin in a browser. A standalone desktop application is also available from the [releases page](https://github.com/dbirman/UnityNeuroscience/releases). Linux standalone available on request.

## Instructions

```
import oursin as urchin
urchin.setup()
```

Calling `setup()` opens a web browser and links it to your Python client.

Set the parameter `standalone = True` to connect to a standalone Desktop application. You'll need to manually copy the ID that Urchin displays to the Desktop renderer.

## Citing

There is no citation for Urchin right now, we'll create one soon.
