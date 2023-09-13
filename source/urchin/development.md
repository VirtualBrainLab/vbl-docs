# Urchin

## Organization

Urchin is organized into three parts. An API, server, and renderer.

### API

The Python API allows users to push and get data to the serverer and to a renderer instance. This allows users to run Urchin online through Google Colab.

### Server

The server runs both an HTTP REST endpoint and a Node.js Socket.IO server. The REST endpoints allow users to push new datasets to the server and retrieve them from data buckets, see below. The Socket.IO server acts as a proxy between a client API and the renderer itself, this can be used for testing visualizations without saving the data or for grabbing screenshot or video data back from the renderer.

### Renderer

The renderer is a standalone WebGL or Desktop client that displays data alongside anatomical reference atlases.

## Virtual environment

To develop for Urchin you will need to run a local copy of the client, server, and Unity builds. For the Python API you will need a new virtual environment with `oursin` installed in **editable** mode.

To setup the venv go into the API folder and run:

```
python -m venv urchin-venv
urchin-venv/Scripts/activate
pip install -e .
```

Updates you make to the code will then be accessible by restarting your Python kernel.

## Adding new functionality

To add a new render function you need three pieces:

 1. Add the new API documentation
 2. Add the `socket.io` call to the set of calls in `Server/server.js`
 3. Add the new functionality to the UnityClient in `Client.cs` and in your manager class

Before deploying you should add a new test script in the [urchin-examples](https://github.com/VirtualBrainLab/urchin-examples) repository which runs your new functionality and makes sure that it works.

### Schema

Schemas are stored in the `Schema/` folder. They have the following pattern:

```
?
```

### Python (oursin package)

The Urchin API has two patterns for inputs, a single object (singular) pattern and a multi-object (plural) pattern. They should in general look like this:

**Singular pattern**

```
object = urchin.object_type.create()
object.set_variable(variable)
```

**Plural pattern**

```
N = 5
object_list = urchin.object_type.create(N)
urchin.object_type.set_variables(object_list, variable_list)
```

Please make sure that inputs are sanitized whenever possible (see `API/utils.py`).

Make sure to add documentation to all of your new renderer functions. Or default Python docstring looks like:

```
def function(parameters):
"""Description.

Parameters
----------
param_name : type
    param description

Examples
--------
>>> urchin...
"""
```

#### Testing

Unit tests should test that the functions generate valid JSON and that the sanitizing functions perform their job correctly for a variety of inputs.

### HTTP REST Server (HTTPServer/?)

### Socket.IO Server (Server/server.js)

The server calls just echo the data from the sender (API) to the receiver (Unity). Copy any of the existing calls and replace the message headers. Please keep the server organized.

### Unity (Client.cs and your manager code)

Your code in Unity should be separated into two layers. All socket messages should be received in the `Client.cs` class and then passed on to a `XXManager.cs`. The `Client` handles all socket communication, while the `Manager` handles all of the Unity local content. Keep managers separated by functionality (e.g. `ProbeManager`, `NeuronManager`, `LineRendererManager`, etc).

## Testing your code

To test your code locally, run the server on your local machine by navigating to the `Server/` folder and running `node server.js`. Then, run client in standalone localhost mode:

```
import oursin as urchin
urchin.setup(localhost=True, standalone=True)
```

Finally, run the Unity renderer app in the editor. You may need to manually set your username as the ID in the app if it doesn't detect it automatically (either via code in `Client.cs` or by pressing `I` and opening the ID input window).

## Deployment

### Deploying the client

The client is accessed by users in two ways: either through the [web server](http://data.virtualbrainlab.org/Urchin/) or through a standalone desktop app which is deployed on Steam. To deploy a new client you need to take a few steps.

 1. If you changed the Addressable assets or updated to a new version of Unity you need to re-build the assets. Do this for each build target separately. Then copy the `UnityClient/ServerData` folder to the `htdocs/UMData` subfolder on the server.
 2. Build the WebGL target build, then copy this to the `htdocs/UMRenderer` subfolder on the server.
 3. Build the Windows target build, compress to zip, and attach this to the next release version. Or, if you are hotfixing a previous release, update the hotfix version number and swap the new build for the previous one.

#### Uploading to the server

The server runs Apache, the htdocs file is at `C:/Apache24/htdocs`. Ask Dan for the login details. You can copy files locally onto the data server or copy them through google drive or slack.

### Pushing the Pypi package

Push to the real server

```
py -m build
py -m twine upload dist/*
```

### Deploying the server

#### On Heroku

Every time the github repository is pushed the Heroku server will re-build. You will get back a 503 server response if there are errors in the code running on Heroku.


### Running code on Colab

Colab is a good solution for hosting and running notebooks off of gitub. All the code has to be built in the notebook, as additions within colab will not be saved. Once a Jupyter Notebook is uploaded to GitHub, an open in github button can be made by pasting the github link into https://openincolab.com/. The resulting html can be inserted into a markdown in the top of the notebook, for users to directly run the code in colab.

When creating a notebook to run in colab, make sure to add !pip install oursin -U at the top of every notebook for users to run their first time running the notebook in colab. Any data can be accessed within the notebook once uploaded to Google Drive, and accessed with the help of the gspread library.
