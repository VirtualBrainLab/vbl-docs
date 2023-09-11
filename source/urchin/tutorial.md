# Tutorials

## Camera control

Left click + drag along the Y axis to pitch the brain

Left click + drag along the X axis to yaw the brain

Hold shift while left clicking and dragging along the X axis to spin the brain

Scroll to zoom

Right click + drag to pan

Hold [SHIFT] or [CTRL] while moving on any axis to increase or decrease the speed, respectively.

You can use `urchin.camera.capture_image(filename)` to take screenshots.

### Grids and Axes

In orthographic camera mode these will look a bit weird, use the perspective camera.

Press [G] to bring up a flat grid

Press [A] to bring up a set of 3D axes (I know... they'll get better eventually)

### Screenshot mode

Press [S] to hide the settings menus

## Settings

<!-- In the application settings (which are open by default) you can "explode" the brain using the slider option. You can explode all areas, or just the cortex and hippocampus "vertically" sort of like a nested doll. You can also switch from exploding all areas to just the left side, as well as set the colors to the defaults on the right side of the brain.  -->

When individual brain areas are loaded, e.g. by using `urchin.ccf.load_beryl()`, you can "explode" the brain using the slider option. Options allow you to explode just one side as well as set the default colors on one side of the brain. Additional "explode" axes can be added on request.

The camera rotation button continuously increments the spin angle to rotate the camera around the current camera target. The speed is controlled by the slider. You can then capture videos using the windows screen capture features [WINDOWS + G].

## Rendering

We're in full beta mode right now -- asking Dan to build you an example is probably the best way to get started.

You can also browse the [Examples](https://github.com/dbirman/UnityNeuroscience/tree/main/Examples) and [API](file:///C:/proj/VBL/vbl-docs/docs/build/html/_autosummary/unityneuro.render.html#module-unityneuro.render) for inspiration.