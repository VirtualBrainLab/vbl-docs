# General Programming Advice

Some general philosophy about coding is stored here. A good more in-depth dive into modern practices in science can be found [here](https://goodresearch.dev). 

In general my approach is to split projects into **pipelines** which process data, **pilot notebooks** which are for testing, **summary notebooks** which generate the final figures for processed data intended for public release or publication, and **applications** which perform a specialized function for public users. A pipeline should, ideally, run entirely on its own given access to raw data and may require tests and assertions to maintain when part of a collaboration. Pilot notebooks are where you do all our debugging and testing and the general expectation is that they will never be run by other users. Summary notebooks are the final output of a project and often tied closely with a publication. Applications are standalone products where all the necessary data are bundled into the product, which is released as an app or even better as a website.

I build pipelines in Python and use Jupyter to create notebooks. For applications I build in Unity or in straight HTML/Javascript for simple apps. 

## Getting started

To work in the VBL ecosystem you will need to install Python 3.9, preferably through [Anaconda](https://www.anaconda.com/products/distribution). You will also need the [Unity 2020.3 LTS](unityhub://2020.3.33f1/915a7af8b0d5) installed and the build tools for Windows and WebGL. I recommend you install and link [Visual Studio 2022](https://visualstudio.microsoft.com/vs/) to Unity and use [VSCode](https://code.visualstudio.com/) for Python. 

For version control I use [Github Desktop](https://desktop.github.com/) rather than mess around with the command line, but this is because I have dozens of repositories some of which have submodules. If this is your first time using git and you are only handling a single repository learning the command line can be to your advantage. 

If you plan to work on the Unity Renderer for Neuroscience **Server** or the ephys-atlas server you will need to install [Node.js](https://nodejs.org/en/).

### Python environment

For the VBL you should be using the `iblenv` conda environment during development, which you can [install here](https://github.com/int-brain-lab/iblenv). We expect to migrate to the Open Ephys environment in the near future.

### Documentation

If you plan to modify this documentation you will need to install Sphinx `pip install -U sphinx` in your environment. Use `make html` in the `vbl-docs/docs` folder to run the build script.

To build the C# documentation you need to run [Doxygen](https://doxygen.nl/) in XML output mode and then use [Breathe](https://breathe.readthedocs.io/en/latest/) to convert the XML output for use with Sphinx.