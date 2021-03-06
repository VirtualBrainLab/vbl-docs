# Sensapex Link
The Sensapex Link is a python WebSocket server that allows any WebSocket compliant application (such as [Pinpoint (Neuropixels Trajectory Planner)](https://github.com/dbirman/NPTrajectoryPlanner/)) to have limited communication with [Sensapex uMp Micromanipulators](https://www.sensapex.com/products/ump-micromanipulators/)

**Table of Contents**
- [Installation](installation)
- [Usage](usage)
- [Code Organization](code-organization)


(installation)=
## Installation

An x86 machine or Docker is required to install or run the server.

### Install locally and use like a standalone app/server

1. Ensure Python 3.8+ and pip are installed
2. `pip install nptraj-sensapex-link`
3. Run `python -m nptraj-sensapex-link` to start the server
    1. To view available command-line arguments, run `python -m nptraj-sensapex-link --help`
    2. Note: all arguments are optional and none are needed to use the server normally

### For usage like a library

1. Ensure Python 3.8+ and pip are installed
2. `pip install nptraj-sensapex-link`
3. Use `from nptraj_sensapex_link import launch` and call `launch()` to start the server
    1. Alternatively, use `import nptraj_sensapex_link` and call `nptraj_sensapex_link.launch()`

### To develop this package with a local install

1. Ensure Python 3.8+ and pip are installed
2. Clone the [repo](https://github.com/dbirman/nptraj-sensapex-link)
3. `cd nptraj-sensapex-link` and run `pip install -r requirements.txt`
4. `python nptraj_sensapex_link/server.py` launches the server
5. Unit tests are available to run under the `tests/` directory

### To develop this package with Docker

1. [Install Docker](https://www.docker.com/get-started/) in any way you like
2. Clone the [repo](https://github.com/dbirman/nptraj-sensapex-link)
3. `cd nptraj-sensapex-link`
4. `docker-compose up` to build the container and run the server
5. `docker attach <container-id>` to view the server logs
6. You can edit the `command` line in `docker-compose.yml` to configure the server's parameters
7. `docker exec -it <container_id> /bin/bash` if you need to enter the container
8. The package is located in the root directory as `nptraj_sensapex_link`
9. Unit tests are available to run under the `tests/` directory
10. `docker-compose stop` to stop the container or `docker-compose down` to stop and remove the container


(usage)=
## Usage
This is a list of available WebSocket events. The code shown is pseudo-WebSocket code that can be used to interact with the server. The exact implementation will depend on the platform and WebSocket interface used.

In general:
- Each event will take in an input and call a callback function with a response dictionary/object as the argument
- Before a manipulator can be used, it must be [registered](registering-a-manipulator) and [calibrated](calibrating-a-manipulator)
  - Before a manipulator can be moved (including being calibrated), it must have its [movement enabled](enable-movement)
  - A manipulator's position can be read before its movement is enabled though
- The server will log unknown events, but will not return callback arguments or emit any messages

**Table of Contents**
- [Getting available manipulators](getting-manipulators)
- [Registering a manipulator](registering-a-manipulator)
- [Calibrating a manipulator](calibrating-a-manipulator)
  - [Bypassing calibration](bypassing-calibration)
- [Get a manipulator's position](get-a-manipulators-position)
- [Set position of a manipulator](set-position-of-a-manipulator)
- [Drive manipualtor to depth](drive-to-depth)
- [Set "inside brain" state of a manipulator](set-inside-brain)
- [Enable movement](enable-movement)
- [Emergency Stop](emergency-stop)

(getting-manipulators)=
### Getting available manipulators
Many implementations may want to first find out what manipulators are available. This can be done by simply sending this event which takes no arguments. A callback will return a list of the available manipulators (up to 50 of them).

**Event:** `get_manipulators`

**Expected Arguments:** None

**Callback Responses Format:** `(manipulators: list[int], error: string)`

| Error message (`error: string`) | Description                                                                 |
| ------------------------------- | --------------------------------------------------------------------------- |
| `''`                            | No errors, the list of all discoverable/available manipulators is returned |
| `Error getting manipulators`    | An unknown error has occurred getting discoverable/available manipulators   |

- `manipulators` will be an empty list on error, however, it is possible that there truly are no discoverable/available/compatible manipulators

#### Example
```python
# Register manipulator with ID 1
ws.emit('get_manipulators', callback=my_callback_func)
```

(registering-a-manipulator)=
### Registering a manipulator
Every manipulator in a Sensapex setup must be registered to the server before being used.

**Event:** `register_manipulator`

**Expected Arguments:**
- Manipulator ID: `int`

**Callback Responses Format:** `(error: string)`

| Error message (`error: string`)  | Description                                                                       |
| -------------------------------- | --------------------------------------------------------------------------------- |
| `''`                             | No errors, registered manipulator with ID `manipulator_id`                        |
| `Manipulator already registered` | Manipulator is already registered, no action taken                                |
| `Manipulator not found`          | The manipulator is not discoverable by the API and may be disconnected or offline |
| `Error registering manipulator`  | An unknown error has occurred while registering                                   |


#### Example
```python
# Register manipulator with ID 1
ws.emit('register_manipulator', 1, callback=my_callback_func)
```

(calibrating-a-manipulator)=
### Calibrating a manipulator
To ensure all manipulators are working properly before applying autonomous control, all manipulators must have their movement checked and calibrated. This is done by moving all *four* axes through their full range of motion while also invoking the calibrate functionality.

**Event:** `calibrate`

**Expected Arguments:**
- Manipulator ID: `int`

**Callback Responses Format:** `(error: string)`

| Error message (`error: string`) | Description                                                |
| ------------------------------- | ---------------------------------------------------------- |
| `''`                            | No errors, calibrated manipulator with ID `manipulator_id` |
| `Manipulator not registered`    | Manipulator is not registered yet                          |
| `Error calling calibrate`       | A Sensapex SDK error has occurred while calibrating        |
| `Error calibrating manipulator` | An unknown error has occurred while calibrating            |


#### Example
```python
# Calibrate manipulator 1
ws.emit('calibrate', 1, callback=my_callback_func)
```

(bypassing-calibration)=
### Bypassing calibration
***FOR TESTING PURPOSES ONLY!! Do not use in production code.***

The calibration requirement may be bypassed by sending this event.

**Event:** `bypass_calibration`

**Expected Arguments:**
- Manipulator ID: `int`

**Callback Responses Format:** `(error: string)`:

| Error message (`error: string`) | Description                                                              |
| ------------------------------- | ------------------------------------------------------------------------ |
| `''`                            | No errors, bypassed calibration for manipulator with ID `manipulator_id` |
| `Manipulator not registered`    | Manipulator is not registered yet                                        |
| `Manipulator not calibrated`    | Manipulator is not calibrated yet                                        |
| `Error bypassing calibration`   | An unknown error has occurred while bypassing calibration                |


#### Example
```python
# Bypass calibration for manipulator 1
ws.emit('bypass_calibration', 1, callback=my_callback_func)
```


(enable-movement)=
### Enable movement
To prevent accidental movement commands, a manipulator must have its movement feature enabled. A manipulator may have its movement enabled for a set period or enabled indefinitely. Relevant information is passed through the event. Once a write lease has expired, an event is emitted back to the server with the ID of the manipulator which can no longer write as the payload.

**Event:** `set_can_write`

**Expected Arguments (dictionary/object with the following format):**
- `manipulator_id`: `int`
- `can_write`: `bool`
- `hours`: `float`

**Callback Responses Format:** `(state: bool, error: string)`

| Error message (`error: string`) | Description                                            |
| ------------------------------- | ------------------------------------------------------ |
| `''`                            | No errors, set state is returned                       |
| `Invalid data format`           | Invalid/unexpected argument format                     |
| `Error in set_can_write`        | An unknown error occurred while starting this function |
| `Manipulator not registered`    | Manipulator is not registered yet                      |
| `Manipulator not calibrated`    | Manipulator is not calibrated yet                      |
| `Error setting can_write`       | An unknown error has occurred enabling movement        |

- `state`: Will be `False` if one was not provided properly in the request or if an error occurred

**Response Event:** `write_disabled` (sent when the write lease has expired)

**Payload:** `manipulator_id`: `int`

#### Example
```python
# Enable movement for manipulator 1 indefinitely (0 = indefinite hours)
ws.emit('set_can_write', {
    'manipulator_id': 1,
    'can_write': True,
    'hours': 0
})
```


(get-a-manipulators-position)=
### Get a manipulator's position
Receive the position of a specified manipulator as X, Y, Z, W (depth) in ??m from the origin.

**Event:** `get_pos`

**Expected Arguments:**
- Manipulator ID: `int`

**Callback Responses Format:** `(position: array, error: string)`

| Error message (`error: string`) | Description                                          |
| ------------------------------- | ---------------------------------------------------- |
| `''`                            | No errors, position is returned                      |
| `Manipulator not registered`    | Manipulator is not registered yet                    |
| `Manipulator not calibrated`    | Manipulator is not calibrated yet                    |
| `Error getting position`        | An unknown error has occurred while getting position |

- `position`: Will be an empty array if one was not provided properly in the request or if an error occurred

```python
# Gets the position of manipulator 1
ws.emit('get_pos', 1, callback=my_callback_func)
```

(set-position-of-a-manipulator)=
### Set position of a manipulator
Instructs a manipulator to go to a position relative to the origin in ??m.

Manipulators move asynchronously from each other. This means large batches of movement events can be sent to the server for several manipulators and each manipulator will move through the events assigned to them independently.

When a manipulator is set to be "inside" the brain, it will have all axes except the depth axis locked. This is to prevent accidental lateral movement while inside brain tissue. This state is set by [`set_inside_brain`](set-inside-brain). One may also explicitly specify movement in only the depth axis using [`drive_to_depth`](drive-to-depth)

**Event:** `goto_pos`

**Expected Arguments (dictionary/object with the following format):**
- `manipulator_id`: `int`
- `pos`: `float[4]` (in x, y, z, w as ??m from the origin)
- `speed`: `int` (in ??m/s)

**Callback Responses Format:** `(position: array, error: string)`

| Error message (`error: string`) | Description                                                          |
| ------------------------------- | -------------------------------------------------------------------- |
| `''`                            | No errors, position is returned                                      |
| `Invalid data format`           | Invalid/unexpected argument format                                   |
| `Error in goto_pos`             | An unknown error occurred while starting this function               |
| `Manipulator movement canceled` | Emergency stop was used and manipulator movements have been canceled |
| `Manipulator not registered`    | Manipulator is not registered yet                                    |
| `Manipulator not calibrated`    | Manipulator is not calibrated yet                                    |
| `Error moving manipulator`      | An unknown error has occurred while moving to position               |

- `position`: Will be an empty array if one was not provided properly in the request or if an error occurred

```python
# Set manipulator 1 to position 0, 0, 0, 0 at 2000 ??m/s
ws.emit('goto_pos', {
    'manipulator_id': 1,
    'pos': [0, 0, 0, 0],
    'speed': 2000
})
```

(drive-to-depth)=
### Drive to depth
Instructs a manipulator to go to a specific depth in ??m. This is equivalent to setting the position of the manipulator to the same position but with a different depth. This function helps to explicitly make sure no other axis except the depth axis is moving during a movement call.

**Event:** `drive_to_depth`

**Expected Arguments (dictionary/object with the following format):**
- `manipulator_id`: `int`
- `depth`: `float` (in ??m from the origin)
- `speed`: `int` (in ??m/s)

**Callback Responses `(depth: float, error: string)`**
| Error message (`error: string`) | Description                                                          |
| ------------------------------- | -------------------------------------------------------------------- |
| `''`                            | No errors, position is returned                                      |
| `Invalid data format`           | Invalid/unexpected argument format                                   |
| `Error in drive_to_depth`       | An unknown error occurred while starting this function               |
| `Manipulator movement canceled` | Emergency stop was used and manipulator movements have been canceled |
| `Manipulator not registered`    | Manipulator is not registered yet                                    |
| `Manipulator not calibrated`    | Manipulator is not calibrated yet                                    |
| `Error moving manipulator`      | An unknown error has occurred while driving to depth                 |

#### Example
```python
# Drive manipulator 1 to a depth of 1000 ??m at 2000 ??m/s
ws.emit('drive_to_depth', {
    'manipulator_id': 1,
    'depth': 1000,
    'speed': 2000
})
```

(set-inside-brain)=
### Set inside brain
Sets the "inside brain" state of a manipulator. When a manipulator is inside the brain, it will have all axes except the depth axis locked. This is to prevent accidental lateral movement while inside brain tissue.

**Event:** `set_inside_brain`

**Expected Arguments (dictionary/object with the following format):**
- `manipulator_id`: `int`
- `inside`: `bool`

**Callback Responses `(state: bool, error: string)`**

| Error message (`error: string`) | Description                                                          |
| ------------------------------- | -------------------------------------------------------------------- |
| `''`                            | No errors, position is returned                                      |
| `Invalid data format`           | Invalid/unexpected argument format                                   |
| `Error in set_inside_brain`     | An unknown error occurred while starting this function               |
| `Manipulator not registered`    | Manipulator is not registered yet                                    |
| `Manipulator not calibrated`    | Manipulator is not calibrated yet                                    |
| `Error moving manipulator`      | An unknown error has occurred while setting inside brain             |

#### Example
```python
# Set manipulator 1 to be inside the brain
ws.emit('inside_brain', {
    'manipulator_id': 1,
    'inside': True
})
```

(emergency-stop)=
### Emergency Stop
There are two ways an emergency stop can be triggered: through this event or the hardware/serial attached button. The server will connect to the first serial device it finds which names itself "USB Serial Device" (which is what an Arduino would appear as) and listen for any serial input from this source (at a baud rate of 9600). The system will poll the serial port every 50 ms to check. The Arduino is running [this sketch](https://github.com/VirtualBrainLab/StopSignal) which will continuously send `1` (followed by a new line symbol) through serial whenever the stop button is pressed.

Both the WebSocket event and the serial method will stop all movement, remove all movement in the queue, ***and set all manipulators to be unwritable.*** Therefore, one must re-enable movement on the manipulators again before continuing.


**Event:** `stop`

**Expected Arguments (dictionary/object with the following format):**
- None

**Callback Responses Format:** `state: bool`
- `true`: No errors, all movement stopped
- `false`: An unknown error has occurred while stopping all movement

#### Example
```python
# Stop all movement
ws.emit('stop')
```


(code-organization)=
## Code Organization
There are three main components of this package:
1. `server.py`: The main server code
2. `sensapex_handler.py`: Code for communicating with the Sensapex API
3. `manipulator.py`: A class for representing a manipulator


### `server.py`
All code responsible for WebSocket server functionality is in this file. This includes client connection/disconnection, event handling, and the main server loop.

For every event, the server does the following:

1. Extract the arguments passed in the event
2. Log that the event was received
3. Call the appropriate function in `sensapex_handler.py` with the arguments
4. Call the callback function with the response from `sensapex_handler.py` as parameters


### `sensapex_handler.py`
All code responsible for communicating with the Sensapex API is in this file. This includes loading the DLL, establishing a connection with the equipment, and maintaining a dictionary of registered manipulators.

Functions names here are the same as the WebSocket events. They are called when the server receives an event from a client. In general, the function does the following:
1. Recieve extracted arguments from `server.py`
2. Inside try/except block, call the appropriate Sensapex API function
3. Log/handle successes and failures
4. Return the callback parameters to `server.py`


### `manipulator.py`
To help make calling functions on manipulators easier, a custom class containing the necessary functions and flags is created. This class is used by `sensapex_handler.py` to call manipulator-specific APIs such as `get_pos` (get position) and to keep track of manipulator-specific flags such as if it has been calibrated yet.

Manipulator functions handle errors and return the appropriate callback parameters like in `sensapex_handler.py`.

## General code practices (for developers looking to contribute)
- Type hinting is implemented where possible
- Tuples are used when possible
- Only one client can be connected at a time