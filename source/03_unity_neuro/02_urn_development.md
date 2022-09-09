# Development

## Organization

### Adding new functionality

To add a new render function you need three pieces:

 1. Update `unitymouse/render.py` to include the new function and add documentation
 2. Add the `socket.io` call to the set of calls in `Server/server.js`
 3. Add the new functionality to the UnityClient in `UM_Client.cs`

Before deploying you should add a new test script in `Examples` which runs your new functionality and makes sure that it works. See `example_script.py`.

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

#### For local testing

To run a local copy of the server you need to install Node.js and then run the command `node server.js` in the Server folder. This will start the server on `localhost:5000`. You then need to redirect both the python client and UnityClient to access the local server. Do this by running `umr.setup(localhost=True)` and by checking the `localhost` option in the `main` GameObject.

#### On Heroku

Every time the github repository is pushed the Heroku server will re-build. You will get back a 503 server response if there are errors in the code running on Heroku. 
