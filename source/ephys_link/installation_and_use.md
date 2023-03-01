# Installation and Use

The [Electrophysiology Manipulator Link](https://github.com/VirtualBrainLab/ephys-link)
(or Ephys Link for short) is a Python WebSocket server that allows any
WebSocket-compliant application (such
as [Pinpoint (electrophysiology planning tool)](https://github.com/VirtualBrainLab/Pinpoint))
to communicate with manipulators used in electrophysiology experiments.

Currently, Ephys Link only supports Sensapex uMp Micromanipulators. However,
this platform is designed to be extensible to other manipulators and more may be
added in the future.

For more information regarding the server's implementation and how the code is
organized, see
the [package's API reference](https://virtualbrainlab.org/api_reference_ephys_link.html)

## Installation

### Prerequisites

1. An **x86 Windows PC is recommended** to run this server.
    1. The server has been verified to work well with Sensapex devices on
       Windows. This is unverified for Linux and
       macOS. However, developing the server is possible on other OS's.
2. For Sensapex devices, the controller unit must be connected to a Windows PC
   via an ethernet cable. A USB-to-ethernet adapter is acceptable.
3. To use the emergency stop feature, ensure an Arduino with
   the [StopSignal](https://github.com/VirtualBrainLab/StopSignal) sketch is
   connected to the computer. Follow the instructions on that repo for how to
   set up the Arduino.

**NOTE:** Ephys Link is an HTTP server without cross-origin support. The server
is currently designed to interface with local/desktop instances of Pinpoint. It
will not work with the web browser versions of Pinpoint at this time.

## Installation

1. Ensure Python 3.10+ and pip are installed
2. `pip install ephys-link --use-pep517`
    1. PEP 517 is needed to allow the Sensapex Manipulator API to be installed

## Usage

To start the server with the default settings, run `python -m ephys_link`.

Default settings:

- Configured for Sensapex manipulators
- Broadcasts on port 8081
- No emergency stop button
- No GUI
- No verbose logging

### Options

All options can be viewed with `python -m ephys_link --help`.

| Option                            | Input                                   | Default                           | Description                                                    |
|-----------------------------------|-----------------------------------------|-----------------------------------|----------------------------------------------------------------|
| `-h, --help`                      |                                         |                                   | Show help message and options                                  |
| `-t TYPE, --type TYPE`            | `sensapex` or `new_scale`               | `sensapex`                        | Select manipulator type                                        |
| `-p PORT, --port PORT`            | Valid HTTP port number                  | `8081`                            | HTTP port to serve on                                          |
| `--new-scale-port NEW_SCALE_PORT` | Valid HTTP port number                  | `8081`                            | New Scale HTTP server port (deprecating soon)                  |
| `-s [SERIAL], --serial [SERIAL]`  | Serial port name (i.e. `COM3`) or empty | `no-e-stop` (disable stop button) | Emergency stop serial port. Auto searches if no port specified |
| `-d, --debug`                     |                                         |                                   | Enable verbose logging for debugging                           |
| `-g, --gui`                       |                                         |                                   | Experimental GUI for server                                    |
| `--version`                       |                                         |                                   | Version number of server                                       |