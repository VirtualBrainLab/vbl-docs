# Ephys Link

The [Electrophysiology Manipulator Link](https://github.com/VirtualBrainLab/ephys-link)
(or Ephys Link for short) is a Python WebSocket server that allows any
WebSocket-compliant application (such
as [Pinpoint](https://github.com/VirtualBrainLab/Pinpoint))
to communicate with manipulators used in electrophysiology experiments.

Currently, Ephys Link only supports Sensapex uMp Micromanipulators. However,
this platform is designed to be extensible to other manipulators and more may be
added in the future.

For more information regarding the server's implementation and how the code is
organized, see
the [package's API reference](https://virtualbrainlab.org/api_reference_ephys_link.html)

## Installation

### Prerequisites

1. [Python 3.10+](https://www.python.org/downloads/) and pip.
2. An **x86 Windows PC is required** to run the server.
    1. The server has been verified to work well with Sensapex devices on
       Windows. It has not been bundled with libraries for Linux and
       macOS. However, developing the server is possible on other OS's.
3. For Sensapex devices, the controller unit must be connected to a Windows PC
   via an ethernet cable. A USB-to-ethernet adapter is acceptable.
4. To use the emergency stop feature, ensure an Arduino with
   the [StopSignal](https://github.com/VirtualBrainLab/StopSignal) sketch is
   connected to the computer. Follow the instructions on that repo for how to
   set up the Arduino.

**NOTE:** Ephys Link is an HTTP server without cross-origin support. The server
is currently designed to interface with local/desktop instances of Pinpoint. It
will not work with the web browser versions of Pinpoint at this time.

### Install

<div style="padding: 15px; border: 1px solid transparent; border-color: transparent; margin-bottom: 20px; border-radius: 4px; color: #31708f; background-color: #d9edf7; border-color: #bce8f1;">
<b>Using a python virtual environment is encouraged.</b>
<p>Create a virtual environment by running <code>python -m venv ephys_link</code>.</p>
<p>Activate the environment by running <code>.\ephyes_link\scripts\activate</code></p>
<p>A virtual environment helps to isolate installed packages from other packages on your computer and ensures a clean installation of Ephys Link</p>
</div>

Run the following command to install the server:

```bash
pip install ephys-link
```

## Usage

To start the server with the default settings, run `python -m ephys_link`.

Default configuration:

- Configured for Sensapex manipulators (add `-t new_scale` to use New Scale
  Manipulators; MPM software is _not_ required)
- Broadcasts on port 8081
- No emergency stop button
- No GUI
- No verbose logging

### Options

All options can be viewed with `python -m ephys_link --help`.

| Option                           | Input                                   | Default     | Description                                                    |
|----------------------------------|-----------------------------------------|-------------|----------------------------------------------------------------|
| `-h, --help`                     |                                         |             | Show help message and options                                  |
| `-t TYPE, --type TYPE`           | `sensapex` or `new_scale`               | `sensapex`  | Select manipulator type                                        |
| `-p PORT, --port PORT`           | Valid HTTP port number                  | `8081`      | HTTP port to serve on                                          |
| `-s [SERIAL], --serial [SERIAL]` | Serial port name (i.e. `COM3`) or empty | `no-e-stop` | Emergency stop serial port. Auto searches if no port specified |
| `-d, --debug`                    |                                         |             | Enable verbose logging for debugging                           |
| `-g, --gui`                      |                                         |             | Experimental GUI for server                                    |
| `--version`                      |                                         |             | Version number of server                                       |