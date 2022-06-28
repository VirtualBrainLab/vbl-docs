# Installation and Use

<p float="left">
 <img src="https://github.com/dbirman/UMRenderer/raw/main/Examples/gallery/flatmap_layout.png" width="25%"> 
 <img src="https://github.com/dbirman/UMRenderer/raw/main/Examples/gallery/data_onesided.png" width="25%"> 
 <img src="https://github.com/dbirman/UMRenderer/raw/main/Examples/gallery/RS_fig1.png " width="35%">
</p>

<p float="center">
 <img src="https://github.com/dbirman/UMRenderer/raw/main/Examples/gallery/brain_rotate_cropped.gif" width="45%"> 
</p>

Urchin (Unity Renderer for Neuroscience) allows you to connect your Python scripts to a standalone rendering program, to create graphics like the ones above.

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

By default calling `setup()` opens a web browser and links it to your Python client. Passing `urn.setup(standalone = True)` allows you to connect to a Desktop renderer.

### Troubleshooting ID

Your Python scripts and the renderer are linked by an ID, which should be set automatically when you call `setup()`. If this link fails you can manually set your ID in the renderer by pressing `I` and entering your account username, which can be obtained with:

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

Hold [SHIFT] or [CTRL] while moving on any axis to increase or decrease the speed, respectively.

### Grids and Axes

In orthographic camera mode these will look a bit weird, use the perspective camera.

Press [G] to bring up a flat grid

Press [A] to bring up a set of 3D axes (I know... they'll get better eventually)

### Screenshot mode

Press [S] to hide the settings menus

## Settings

<!-- In the application settings (which are open by default) you can "explode" the brain using the slider option. You can explode all areas, or just the cortex and hippocampus "vertically" sort of like a nested doll. You can also switch from exploding all areas to just the left side, as well as set the colors to the defaults on the right side of the brain.  -->

When individual brain areas are loaded, e.g. by using `urn.load_beryl_areas()`, you can "explode" the brain using the slider option. Options allow you to explode just one side as well as set the default colors on one side of the brain. Additional "explode" axes can be added on request.

The camera rotation button continuously increments the spin angle to rotate the camera around the current camera target. The speed is controlled by the slider. You can then capture videos using the windows screen capture features [WINDOWS + G].

## Rendering

We're in full beta mode right now -- asking Dan to build you an example is probably the best way to get started.

You can also browse the [Examples](https://github.com/dbirman/UnityNeuroscience/tree/main/Examples) and [API](file:///C:/proj/VBL/vbl-docs/docs/build/html/_autosummary/unityneuro.render.html#module-unityneuro.render) for inspiration.

## Citing

If you use this to make figures for a publication you should cite this repo, email me (dbirman@uw.edu) and I can generate a DOI.
