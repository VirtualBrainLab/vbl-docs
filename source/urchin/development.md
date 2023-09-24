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

## Testing

Unit tests should test that the functions generate valid JSON and that the sanitizing functions perform their job correctly for a variety of inputs.

## HTTP REST Server (HTTPServer/?)

## Socket.IO Server (Server/server.js)

The server calls just echo the data from the sender (API) to the receiver (Unity). Copy any of the existing calls and replace the message headers. Please keep the server organized.

## Unity (Client.cs and your manager code)

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

## Adding Google Colab Functionality to Urchin Examples

Google Colab provides a convenient way to host and execute Jupyter Notebooks in the cloud, making it easy for users to interact with your code without the need for local installations.

### Running Uchin Examples on Colab

#### Prepare notebook on Github

Create Jupyter Notebook with all necessary code and explanations, and upload it to the correct GitHub repository. Keep in mind that any edits made within Colab will not be saved to the GitHub repository when building the notebook.

#### Generate "Open in Colab" Button

To allow users to directly run notebook in Google Colab, generate the "Open in Colab" button using https://openincolab.com/. Insert the generated HTML snippet at the top of the notebook within a markdown cell, or anywhere else that is easily accessible to direct users to the notebook on Colab.

#### Ensure Dependancies are installed

Include the following code to ensure that users have the necessary dependencies, including the most up to date version of Urchin installed within their Colab environment:

```
!pip install urchin -U
```

Include a reminder for users to ensure that popups are enabled, and import the Urchin package.

```{python}
#Ensure that popups are enabled.

#Importing necessary libraries:
import oursin as urchin
urchin.setup()
```

#### Data Access

Data files can't be sotred in the urchin-examples repository, so any data used within the example script must first be uploaded publicly to the shared Google Drive in the [ExampleData folder](https://drive.google.com/drive/folders/12RyHx3bh4ChwfN95NLhvJL5BshhM8M7v)(VBL shared drive/1_Urchin/1_SharedFiles/ExampleData/). Ensure that sharing permissions are set so that anyone with link can edit. This allows people to run code off Colab using the data without having to sign into Google first. 

If accessing data within notebook be sure to include the following import code and get data function:

```{python}
import pandas as pd

#Function for easily pulling in data:
#url = link to google sheet (on editing mode) as a string
def get_data(url):
    data = url.replace("/edit#gid=", "/export?format=csv&gid=")
    df = pd.read_csv(data)
    return df
```

The data can then be directly pulled in as a data frame directly from the edit link as a string. For example:

```
data_frame = get_data('https://docs.google.com/spreadsheets/d/1F9NBt-qqcA-IyxowXl82S4NI0gYyczUOEb8MEaW7qm0/edit#gid=1956783922')
```
