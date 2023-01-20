# Urchin

## Organization

Urchin is organized into three parts. A client, server, and renderer. The only client right now is the Python API, but in the future we may build other APIs (MATLAB, R). The Server is a Node.js server that echoes messages between clients and renderers. The Renderer is a Unity app that can run either as a standalone desktop build or in the browser. 

### Virtual environment

To develop for Urchin you will need to run a local copy of the client, server, and Unity builds. For the Python API you will need a new virtual environment with `unityneuro` installed in **editable** mode. 

To setup the venv go into the API folder and run:

```
python -m venv urchin-venv
urchin-venv/Scripts/activate
pip install -e .
```

### Adding new functionality

To add a new render function you need three pieces:

 1. Update `unitymouse/render.py` to include the new function and add documentation
 2. Add the `socket.io` call to the set of calls in `Server/server.js`
 3. Add the new functionality to the UnityClient in `UM_Client.cs` and in your manager class

Before deploying you should add a new test script in `Examples/basic` which runs your new functionality and makes sure that it works.

#### Urchin (API/unityneuro/render.py)

The Urchin calls are mostly very simple, they just take input data from the user, sanitize it (or not, most of them don't do this yet) and send it off with a message header to the server.

Make sure to add documentation to all of your new renderer functions so it's clear what they take as input.

#### Server (Server/server.js)

The server calls just echo the data from the sender (API) to the receiver (Unity). Copy any of the existing calls and replace the message headers. Please keep the server organized.

#### Unity (UM_Client.cs and your manager code)

Your code in Unity should be separated into two layers. All socket messages should be received in the `UM_Client.cs` class and then passed on to a `XXManager.cs`. The `Client` handles all socket communication, while the `Manager` handles all of the Unity local content. Keep managers separated by functionality (e.g. `ProbeManager`, `NeuronManager`, `LineRendererManager`, etc).

## Testing your code

To test your code locally, run the server on your local machine by navigating to the `Server/` folder and running `node server.js`. Then, run client in standalone localhost mode:

```
urn.setup(localhost=True, standalone=True)
```

You should see the client connect with your username as ID on the server window.

Finally, run the Unity renderer app in the editor. You may need to manually set your username as the ID in the app if it doesn't detect it automatically (either via code in `UM_Client.cs` or by pressing `I` and opening the ID input window).

## Deployment

### Deploying the client

The client is accessed by users in two ways: either through the [web server](http://data.virtualbrainlab.org/UMRenderer/) or through a standalone desktop app which we include in each minor version release. To deploy a new client you need to take a few steps.

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
