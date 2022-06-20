# Sensapex Link
The Sensapex Link is a python server which allows any WebSocket compliant application (such as [Pinpoint (Neuropixels Trajectory Planner)](https://github.com/dbirman/NPTrajectoryPlanner/)) to have limited communication with [Sensapex uMp Micromanipulators](https://www.sensapex.com/products/ump-micromanipulators/)

# Installation
1. Ensure Python >3.5 and pip is installed
2. Clone the [repo](https://github.com/dbirman/nptraj-sensapex-link)
3. `cd nptraj-sensapex-link` and run `pip install requirements.txt`
4. Upon completion, run `python main.py` to launch the server
5. You may optionally run the various tests under the `tests` directory to try different functions

# Usage
This is a list of available functions. The code shown is example pseudo-WebSocket code that can be used to interact with the server. The exact implementation will depend on the platform and WebSocket interface used. 
## Registering a manipulator
Every manipulator in a Sensapex setup must be registered to the server to be used.

```python
# Register manipulator with ID 1
ws.emit('register_manipulator', 1)
```

## Get a manipulator's position
Recieve the position of a specified manipulator as X, Y, Z, W (depth)

```python
# Gets the position of manipulator 1
ws.emit('get_pos', 1)

# Returns [x, y, z, w] of a manipulator to 'get_pos'
onMessage('get_pos')
# Example:
# {
#     'manipulator_id': 1,
#     'pos': [1234.56789, 1234.56789, 1234.56789, 1234.56789]
# }
```

## Set position of a manipulator
Instructs a manipulator to go to a position. The manipulator will travel to set positions in the order the server recieves them. Recieve a message upon the move's completion. 

```python
# Set manipulator 1 to position 0, 0, 0, 0 at 2000 um/s
ws.emit('goto_pos', {
    'manipulator_id': 1,
    'pos': [0, 0, 0, 0],
    'speed': 2000
})

# Returns [x, y, z, w] of a manipulator to 'goto_pos'
onMessage('goto_pos')
# Example:
# {
#     'manipulator_id': 1,
#     'pos': [1234.56789, 1234.56789, 1234.56789, 1234.56789]
# }
```
