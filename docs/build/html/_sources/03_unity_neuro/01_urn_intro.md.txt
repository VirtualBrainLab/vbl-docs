# Installation and Use

<p float="left">
 <img src="https://github.com/dbirman/UMRenderer/raw/main/Examples/gallery/flatmap_layout.png" width="25%"> 
 <img src="https://github.com/dbirman/UMRenderer/raw/main/Examples/gallery/data_onesided.png" width="25%"> 
 <img src="https://github.com/dbirman/UMRenderer/raw/main/Examples/gallery/RS_fig1.png " width="35%">
</p>

<p float="center">
 <img src="https://github.com/dbirman/UMRenderer/raw/main/Examples/gallery/brain_rotate_cropped.gif" width="45%"> 
</p>

The Unity Renderer for Neuroscience allows you to connect your Python scripts to a standalone rendering program, to create graphics like the ones above. As a user, you only need to read the first set of instructions below (install + instructions).

## Install

```
pip install unityneuro
```

The bundled examples in the Examples folder should open the Unity Renderer web app automatically. You can also run in standalone mode by downloading the desktop app for Windows from the [releases page](https://github.com/dbirman/UnityNeuroscience/releases). Linux standalone available on request.

## Instructions

```
import unityneuro.render as urn
urn.setup()
```

By default calling `setup()` opens a web browser and links it to your Python client. Setting `standalone = True` allows you to connect to the standalone Renderer application. 

### Setting ID on web

If you open the web browser page automatically from Python your ID should be set automatically. If this fails or you need to change your ID press `I` and enter your account username. If you aren't sure what that is, try running:

```
python
import os
os.getlogin()
```

You can press `C` to open the console to confirm your ID was set correctly.

## Interaction

Left click + drag along the Y axis to pitch the brain

Left click + drag along the X axis to yaw the brain

Hold shift while left clicking and dragging along the X axis to spin the brain

Scroll to zoom

Right click + drag to pan

## Rendering

Our basic test suite can be run using the [example script](https://github.com/dbirman/UnityNeuroscience/blob/main/Examples/example_client.py) which is also a good starting point for learning about the different function calls that are available. 

Please see the [Examples](https://github.com/dbirman/UnityNeuroscience/tree/main/Examples) and [API](file:///C:/proj/VBL/vbl-docs/docs/build/html/_autosummary/unityneuro.render.html#module-unityneuro.render) for more comprehensive examples.

### Settings

<!-- In the application settings (which are open by default) you can "explode" the brain using the slider option. You can explode all areas, or just the cortex and hippocampus "vertically" sort of like a nested doll. You can also switch from exploding all areas to just the left side, as well as set the colors to the defaults on the right side of the brain.  -->

The camera rotation button continuously increments the `set_camera_y_angle` function to rotate the camera around the current camera target point. The speed is controlled by the slider.

## Citing

If you use this to make figures for a publication you should cite this repo, email me (dbirman@uw.edu) and I can generate a DOI.
