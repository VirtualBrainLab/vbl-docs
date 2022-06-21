# Sensapex Link
The Sensapex Link is a python server which allows any WebSocket compliant application (such as [Pinpoint (Neuropixels Trajectory Planner)](https://github.com/dbirman/NPTrajectoryPlanner/)) to have limited communication with [Sensapex uMp Micromanipulators](https://www.sensapex.com/products/ump-micromanipulators/)

# Installation
## For usage
1. Ensure Python >3.5 and pip are installed
2. `pip install nptraj-sensapex-link`

## For development
Pulled from the [repository README](https://github.com/dbirman/nptraj-sensapex-link/blob/main/README.md)

1. Ensure Python >3.5 and pip are installed
2. Clone the [repo](https://github.com/dbirman/nptraj-sensapex-link)
3. `cd nptraj-sensapex-link` and run `pip install requirements.txt`
4. Get the [Sensapex uM SDK](http://dist.sensapex.com/misc/um-sdk/latest/) binary zip
   1. Currently (June 2022), the SDK version is that is compatible with the Sensapex python SDK is [v1.022](http://dist.sensapex.com/misc/um-sdk/latest/umsdk-1.022-binaries.zip)
   2. **Make sure the firmware version installed on the manipulators matches the SDK version you install**
5. Extract the zip and copy the DLL or lib file appropriate for your system into the installation location for the python Sensapex module
   1. i.e. if you are using a virtual environment in windows, copy the DLL into `{path to venv}/Lib/site-packages/sensapex/`
6. Upon completion, run `python main.py` to launch the server
7. Unit tests are available to run under the `tests/` directory

# Usage
This is a list of available WebSocket events. The code shown is example pseudo-WebSocket code that can be used to interact with the server. The exact implementation will depend on the platform and WebSocket interface used.

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

**Callback Responses (`int, string`):**
- `manipulator_id, ''`: No errors, registered manipulator with ID `manipulator_id`
- `manipulator_id, 'Manipulator already registered'`: Manipulator is already registered, no action taken
- `manipulator_id, 'Manipulator not found'`: The manipulator is not discoverable by the API and may be disconnected or offline
- `manipulator_id, 'Error registering manipulator'`: An unknown error has occured while getting position

### Example
```python
# Register manipulator with ID 1
ws.emit('register_manipulator', 1, callback=my_callback_func)
```

(get-a-manipulators-position)=
## Get a manipulator's position
Recieve the position of a specified manipulator as X, Y, Z, W (depth)

**Event:** `get_pos`

**Expected Arguments:**
- Manipulator ID: `int`

**Callback Responses (`int, float[4], string`)**
- `manipulator_id, [x, y, z, w], ''`: No errors, position is returned
- `manipulator_id, [], 'Manipulator not registered'`: Manipulator is not registered yet
- `manipulator_id, [], 'Error getting position'`: An unknown error has occured while getting position

```python
# Gets the position of manipulator 1
ws.emit('get_pos', 1, callback=my_callback_func)
```

(set-position-of-a-manipulator)=
## Set position of a manipulator
Instructs a manipulator to go to a position. The manipulator will travel to the given positions in the order the server receives them. All movement is sequential and the handler for this event is blocked while a movement is taking place.

**Event:** `goto_pos`

**Expected Arguments (dictionary/object with the following format):**
- `manipulator_id`: `int`
- `pos`: `float[4]` (in x, y, z, w)
- `speed`: `int` (in um/s)

**Callback Responses (`int, float[4], string`)**
- `manipulator_id, [x, y, z, w], ''`: No errors, final position is returned
- `manipulator_id, [], 'Manipulator not registered'`: Manipulator is not registered yet
- `manipulator_id, [], 'Error moving manipulator'`: An unknown error has occured while getting position

```python
# Set manipulator 1 to position 0, 0, 0, 0 at 2000 um/s
ws.emit('goto_pos', {
    'manipulator_id': 1,
    'pos': [0, 0, 0, 0],
    'speed': 2000
})
```