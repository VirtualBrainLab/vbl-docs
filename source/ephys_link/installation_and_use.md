# Ephys Link

The [Electrophysiology Manipulator Link](https://github.com/VirtualBrainLab/ephys-link)
(or Ephys Link for short) is a Python WebSocket server that allows any
WebSocket-compliant application (such
as [Pinpoint](https://github.com/VirtualBrainLab/Pinpoint))
to communicate with manipulators used in electrophysiology experiments.

Currently, Ephys Link only supports Sensapex uMp Micromanipulators and New Scale
manipulators. However, this platform is designed to be extensible to other
manipulators and more may be
added in the future.

For more information regarding the server's implementation and how the code is
organized, see
the [package's API reference](https://virtualbrainlab.org/api_reference_ephys_link.html)

## Installation

### Prerequisites

1. [Python 3.10+](https://www.python.org/downloads/) and pip.
2. An **x86 Windows PC is required** to run the server.
3. For Sensapex devices, the controller unit must be connected via an ethernet
   cable. A USB-to-ethernet adapter is acceptable. For New Scale manipulators,
   the controller unit must be connected via USB and be powered by a 6V power
   supply.
4. To use the emergency stop feature, ensure an Arduino with
   the [StopSignal](https://github.com/VirtualBrainLab/StopSignal) sketch is
   connected to the computer. Follow the instructions on that repo for how to
   set up the Arduino.

**NOTE:** Ephys Link is an HTTP server without cross-origin support. The server
is currently designed to interface with local/desktop instances of Pinpoint. It
will not work with the web browser versions of Pinpoint at this time.

### Install

<div style="padding: 15px; border: 1px solid transparent; border-color: transparent; margin-bottom: 20px; border-radius: 4px; color: #31708f; background-color: #d9edf7; border-color: #bce8f1;">
<b>Using a Python virtual environment is encouraged.</b>
<p>Create a virtual environment by running <code>python -m venv ephys_link</code></p>
<p>Activate the environment by running <code>.\ephys_link\scripts\activate</code></p>
<p>A virtual environment helps to isolate installed packages from other packages on your computer and ensures a clean installation of Ephys Link</p>
</div>

Run the following command to install the server:

```bash
pip install ephys-link
```

## Usage

| Manipulator Platform              | Command                                     |
|-----------------------------------|---------------------------------------------|
| Sensapex                          | `python -m ephys_link`                      |
| New Scale                         | `python -m ephys_link -t new_scale`         |
| New Scale via Pathway HTTP server | `python -m ephys_link -t new_scale_pathway` |

By default, the server will broadcast with its local IP address on port 8081.
**Copy this information into Pinpoint to connect**.

For example, if the server is running on the same computer that Pinpoint is, use

- Server: `localhost`
- Port: `8081`

### "New Scale" vs "New Scale via Pathway HTTP server"

New Scale manipulators have two methods of connection. The first method is through a direct hardware
connection (`-t new_scale`). The second is via the HTTP server broadcast by the Pathway
software (`-t new_scale_pathway`). The latter method is only available if Pathway is running on the same computer as
Ephys Link. New Scale manipulators should be connected to the Pathway software first and the HTTP server should be
running.

### Options

All options can be viewed with `python -m ephys_link --help`.

| Option                           | Input                                   | Default     | Description                                                    |
|----------------------------------|-----------------------------------------|-------------|----------------------------------------------------------------|
| `-h, --help`                     |                                         |             | Show help message and options                                  |
| `-t TYPE, --type TYPE`           | `sensapex` or `new_scale`               | `sensapex`  | Select manipulator type                                        |
| `-p PORT, --port PORT`           | Valid HTTP port number                  | `8081`      | HTTP port to serve on                                          |
| `--pathway_port`                 | Valid HTTP port number                  | `8080`      | HTTP port Pathway's server is running on                       |
| `-s [SERIAL], --serial [SERIAL]` | Serial port name (i.e. `COM3`) or empty | `no-e-stop` | Emergency stop serial port. Auto searches if no port specified |
| `-d, --debug`                    |                                         |             | Enable verbose logging for debugging                           |
| `--version`                      |                                         |             | Version number of server                                       |