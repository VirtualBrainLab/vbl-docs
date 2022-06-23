# Sensapex Link
The Sensapex Link is a python server that allows any WebSocket compliant application (such as [Pinpoint (Neuropixels Trajectory Planner)](https://github.com/dbirman/NPTrajectoryPlanner/)) to have limited communication with [Sensapex uMp Micromanipulators](https://www.sensapex.com/products/ump-micromanipulators/)

**Table of Contents**
- [Installation](installation)
- [Usage](usage)
- [Code Organization](code-organization)


(installation)=
# Installation
Copied from the [repo's README.md](https://github.com/dbirman/nptraj-sensapex-link/blob/main/README.md)

## For usage like a standalone app/server
1. Ensure Python 3.8+ and pip are installed
2. `pip install nptraj-sensapex-link`
3. Run `python -m nptraj-sensapex-link` to start the server

## For usage like a library
1. Ensure Python 3.8+ and pip are installed
2. `pip install nptraj-sensapex-link`
3. Use `from nptraj_sensapex_link import launch` and call `launch()` to start the server
   1. Alternatively, use `import nptraj_sensapex_link` and call `nptraj_sensapex_link.launch()`

## To develop this package
1. Ensure Python 3.8+ and pip are installed
2. Clone the [repo](https://github.com/dbirman/nptraj-sensapex-link)
3. `cd nptraj-sensapex-link` and run `pip install requirements.txt`
4. The package is located in `src/`
5. `python src/nptraj_sensapex_link/server.py` launches the server
6. Unit tests are available to run under the `tests/` directory


(usage)=
# Usage
This is a list of available WebSocket events. The code shown is pseudo-WebSocket code that can be used to interact with the server. The exact implementation will depend on the platform and WebSocket interface used.

In general, each event will take in an input and call a callback function with certain arguments.

**Table of Contents**
- [Registering a manipulator](registering-a-manipulator)
- [Get a manipulator's position](get-a-manipulators-position)
- [Set position of a manipulator](set-position-of-a-manipulator)

(registering-a-manipulator)=
## Registering a manipulator
Every manipulator in a Sensapex setup must be registered to the server before being used.

**Event:** `register_manipulator`

**Expected Arguments:**
- Manipulator ID: `int`

**Callback Responses `(int, string)`:**
- `(manipulator_id, '')`: No errors, registered manipulator with ID `manipulator_id`
- `(manipulator_id, 'Manipulator already registered')`: Manipulator is already registered, no action taken
- `(manipulator_id, 'Manipulator not found')`: The manipulator is not discoverable by the API and may be disconnected or offline
- `(manipulator_id, 'Error registering manipulator')`: An unknown error has occurred while getting position

### Example
```python
# Register manipulator with ID 1
ws.emit('register_manipulator', 1, callback=my_callback_func)
```

(get-a-manipulators-position)=
## Get a manipulator's position
Receive the position of a specified manipulator as X, Y, Z, W (depth) in µm from the origin.

**Event:** `get_pos`

**Expected Arguments:**
- Manipulator ID: `int`

**Callback Responses `(int, float[4], string)`**
- `(manipulator_id, (x, y, z, w), '')`: No errors, position is returned
- `(manipulator_id, (), 'Manipulator not registered')`: Manipulator is not registered yet
- `(manipulator_id, (), 'Error getting position')`: An unknown error has occured while getting position

```python
# Gets the position of manipulator 1
ws.emit('get_pos', 1, callback=my_callback_func)
```

(set-position-of-a-manipulator)=
## Set position of a manipulator
Instructs a manipulator to go to a position relative to the origin in µm. The manipulator will travel to the given positions in the order the server receives them. All movement is sequential and the handler for this event is blocked while a movement is taking place.

**Event:** `goto_pos`

**Expected Arguments (dictionary/object with the following format):**
- `manipulator_id`: `int`
- `pos`: `float[4]` (in x, y, z, w as µm from the origin)
- `speed`: `int` (in µm/s)

**Callback Responses `(int, float[4], string)`**
- `(manipulator_id, (x, y, z, w), '')`: No errors, final position is returned
- `(manipulator_id, (), 'Manipulator not registered')`: Manipulator is not registered yet
- `(manipulator_id, (), 'Error moving manipulator')`: An unknown error has occured while getting position

```python
# Set manipulator 1 to position 0, 0, 0, 0 at 2000 µm/s
ws.emit('goto_pos', {
    'manipulator_id': 1,
    'pos': [0, 0, 0, 0],
    'speed': 2000
})
```


(code-organization)=
# Code Organization
There are three main components of this package:
1. `server.py`: The main server code
2. `sensapex_handler.py`: Code for communicating with the Sensapex API
3. `manipulator.py`: A class for representing a manipulator


## `server.py`
All code responsible for WebSocket server functionality is in this file. This includes client connection/disconnection, event handling, and the main server loop.

For every event, the server does the following:

1. Extract the arguments passed in the event
2. Log that the event was received
3. Call the appropriate function in `sensapex_handler.py` with the arguments
4. Call the callback function with the response from `sensapex_handler.py` as parameters


## `sensapex_handler.py`
All code responsible for communicating with the Sensapex API is in this file. This loading the DLL, establishing a connection with the equipment and maintaining a dictionary of registered manipulators.

Functions names here are the same as the WebSocket events. They are called when the server receives an event from a client. In general, the function does the following:
1. Recieve extracted arguments from `server.py`
2. Inside try/except block, call the appropriate Sensapex API function
3. Log/handle successes and failures
4. Return the callback parameters to `server.py`


## `manipulator.py`
To help make calling functions on manipulators easier, a custom class containing the necessary functions and flags is created. This class is used by `sensapex_handler.py` to call manipulator-specific APIs such as `get_pos` (get position) and to keep track of manipulator-specific flags such as if it has been calibrated yet.

Manipulator functions handle errors and return the appropriate callback parameters like in `sensapex_handler.py`.

# General code practices (for developers looking to contribute)
- Type hinting is implemented where possible
- Tuples are used when possible
- Only one client can be connected at a time