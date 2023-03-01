# Installation and Use

The [Electrophysiology Manipulator Link](https://github.com/VirtualBrainLab/ephys-link) (
or Ephys Link for short) is a Python
WebSocket server that allows any WebSocket-compliant application (such
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
       macOS. However, developing the server is possible on a Linux operating
       system (macOS users should virtualize Linux).
2. For Sensapex devices, the controller unit must be connected to the PC via an
   ethernet cable. A USB-to-ethernet adapter is acceptable as well.
3. To use the emergency stop feature, ensure an Arduino with
   the [StopSignal][StopSignal] sketch is connected to the computer. Follow
   the instructions on that repo for how to set up the Arduino.

**NOTE:** Ephys Link is an HTTP server without cross-origin support. The server is currently designed to interface with local/desktop instances of Pinpoint. It will not work with the web browser versions of Pinpoint at this time.

## Installation

1. Ensure Python 3.8+ and pip are installed
2. `pip install ephys-link --use-pep517`
    1. PEP 517 is needed to allow the Sensapex Manipulator API to be installed
3. Run `python -m ephys_link` to start the server
    1. To view available command-line arguments,
       run `python -m ephys_link --help`
    2. Note: all arguments are optional and none are needed to use the server
       normally

The server defaults to connecting to Sensapex manipulators. To run for New Scale, use `python -m ephys_link --type sensapex`

### For usage like a library

1. Ensure Python 3.8+ and pip are installed
2. `pip install ephys-link`
3. Use `from ephys_link import server` and call `server.launch()` to start the
   server
    1. Alternatively, use `import ephys_link` and
       call `ephys_link.server.launch()`

### To develop this package with a local install

1. Ensure Python 3.8+ and pip are installed
2. Clone the [repo](https://github.com/VirtualBrainLab/ephys-link)
3. `cd ephys-link` and run `pip install -r requirements.txt`
4. `python ephys_link/server.py` launches the server
5. Unit tests are available to run under the `tests/` directory

### To develop this package with Docker

1. [Install Docker](https://www.docker.com/get-started/) in any way you like
2. Clone the [repo](https://github.com/VirtualBrainLab/ephys-link)
3. `cd ephys-link`
4. `docker-compose up` to build the container and run the server
5. `docker attach <container-id>` to view the server logs
6. You can edit the `command` line in `docker-compose.yml` to configure the
   server's parameters
7. `docker exec -it <container_id> /bin/bash` if you need to enter the container
8. The package is located in the root directory as `ephys_link`
9. Unit tests are available to run under the `tests/` directory
10. `docker-compose stop` to stop the container or `docker-compose down` to stop
    and remove the container