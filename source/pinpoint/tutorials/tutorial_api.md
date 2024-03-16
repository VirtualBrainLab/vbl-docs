# API

Pinpoint can send anatomical data about probes in the scene to the Open Ephys GUI and SpikeGLX during experiments. This is an independent feature from the electrophysiology link features (below) and they can be used together, or separately.

**These features are only available on the Windows Desktop build of Pinpoint**
they will not run in the web browser.

## Open Ephys GUI

<image src="../../_static/images/tutorial/API/open_ephys.png" alt="Open Ephys" position="left" style="width:60vw">

1. Launch Open Ephys and connect to or simulate one or more probes using the Neuropix-PXI plugin.
2. Make sure at least one [Probe Viewer](https://open-ephys.github.io/gui-docs/User-Manual/Plugins/Probe-Viewer.html#probe-viewer) plugin is in your signal chain. If you don't see the Probe Viewer in your processor list, you can add it via the Plugin Installer (Probe Viewer version ≥0.3.1 is needed to interface with Pinpoint).
3. Make sure the HTTP Server is enabled in Open Ephys ("File > Enable HTTP Server" should have a checkmark next to it).
4. In Pinpoint, press <kbd>ESC</kbd> to open the settings menu and navigate to the "API" tab
5. In the "OpenEphys API" section, make sure the IP address matches that of the machine running Open Ephys. If Pinpoint is running on the same computer, this will be "localhost". The port number will always be 37497.
6. Toggle the API on
7. In the probe matching list on the right, you should see each of your Pinpoint probes. Use the dropdown menus to link each probe to its corresponding name in Open Ephys.
8. You should immediately see should see an update to the anatomy data in Open Ephys.
9. You can update the Probes and the links to Open Ephys from within Pinpoint, but if you make a change to the signal chain in Open Ephys you'll need to toggle the API off and then back on to refresh the connection. 

## SpikeGLX

<image src="../../_static/images/tutorial/API/spikeglx.png" alt="SpikeGLX" position="left" style="width:60vw">

Make sure that your SpikeGLX version is updated, you'll need a 202306 or later version number. You can update to the latest SpikeGLX [here](https://billkarsh.github.io/SpikeGLX/).

1. Download [HelloSGLX](https://github.com/billkarsh/HelloSGLX) and place the folder in a convenient location, e.g. C:/HelloSGLX
2. Launch SpikeGLX 
3. In the Options > Command server Settings menu, make sure that *Enable Remote Command Server* option is checked.
4. Start a **New Acquisition**, using existing data in simulation or a live probe. Note that the *Open File Viewer* option does not work with the API.
5. In Pinpoint, press <kbd>ESC</kbd> to open the settings menu and navigate to the "API" tab
6. Make sure the location of the HelloSGLX file is accurate. Use the file navigator to locate the file if it's wrong.
7. Toggle the API on. If you see an API Status error, it probably means you didn't turn the command server on, see step 3.
8. In the probe matching list on the right, you should see each of your Pinpoint probes. Using the dropdown menus, select which SpikeGLX probe ID each probe should be linked to
9. You should immediately see an update to the anatomy data in SpikeGLX (make sure to open the probe shank view to see this)
10. You can update the Probes and the links to SpikeGLX from within Pinpoint, but if you make a change to the acquisition in SpikeGLX you'll need to toggle the API off and then back on to refresh the connection. 