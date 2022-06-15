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

## Starting a project

At the beginning of a research project you are usually about to start doing a lot of exploratory data analysis and programming. This is good! It's pretty unlikely that the goals you set out with at the start will be the same as those you converge on by the end. Building Python notebooks in the beginning is probably the fastest and easiest way to make quick progress learning a new dataset or API.

As soon as you start finding yourself copy-pasting code blocks or defining functions inside of blocks you'll know that it's time to start building a function [module](https://docs.python.org/3/tutorial/modules.html) and a pipeline. A module is just a `.py` file with a collection of functions in it, which you call from your other code by importing the module. A pipeline is a `.py` file or a function which takes as input raw data (or intermediate analysis results) and outputs some analyzed version of that data. Both of these are just programming constructs for organizing your code! One nice aspect of organizing your functions into modules is that eventually you can share these, e.g. on Pypi. 

## Getting work done

At some point in your project there's a good chance you will start to feel burnt out. In research projects this often hits when the initial excitement of a new endeavour has worn off and the real work is starting. In my experience, this is unfortunately when only around 10% of the work will be finished. There is no way to avoid putting in time and hard work to see a project to completion but there are a lot of tricks I use to motivate yourself. These are largely focused on programming, since that's usually where I get burnt out first.

### Tricks

#### Sleep, eat, sun, relationships, exercise

The best way to write bad code is to push yourself when you're tired and hungry or when you're skipping important life activities like spending time with your partner and friends or exercising.

#### Work for a set amount of time each morning, before distractions

For those of you who drink coffee, pour yourself a double cup, sit down with your to-do list from the day before and start coding. Don't stop until your coffee is finished and you've crossed at least one item off. When you're *done* with that item, you can check your email, check your phone, etc. By this point you'll have some momentum and you can probably see a few more items through. When you run out of steam, write down a list of to-do items for the next coding session. Start with one or two easy wins and then add one or two real features. Three or four items maximum on the list -- anything else you can put in your tracking system.

#### Use an issue tracker

I track all of my projects using the public Github issues tracker. I use four labels to mark issues:

 - **bug**: something that is impeding users or causing analysis problems and needs to be fixed ASAP
 - **feature**: a new idea, small or large, that I want to work on in the future
 - **question**: a UI/UX or documentation improvement I need to make, usually prompted by a user asking about something confusing
 - **wontfix**: a request by a user that I can't deal with either because it's too hard or I'm time limited

One thing I don't do is sort my issues by priority. I usually know the priority and I can bubble up the important issues when I write my to-do list after coding. If something is falling down the issue list and never getting then that's a sign that it either isn't actually important (and should become a *wontfix* item) or that it's hard and I might need help with it. 

#### Flow

When I was first learning to program and I was still building pure fun applications, such as small coding projects in classes where the hard parts were done by the TAs, I found it easy to get into that flow programming state where you get a ton finished and time just zooms by. Now that I'm writing the fun parts and the hard parts I find it's harder to get into the zone. Music can help me, and there are particular songs and styles of music that I find most helpful.

## Finishing a project

At some point it will be clear that there is an endpoint to your project. This is when you need to take a step back and probably refactor your code.

### Refactoring

Programming languages are fundamentally languages used to communicate and unfortunately our first attempt to communicate an idea is often quite poor. Re-organizing your code to use better structure and to be more understandable is almost always worth it when you are getting to a late stage. If you don't do it for others, at least do it for yourself on the (high) chance that you'll be forced to revisit your code in the future.

Before you refactor your code you should write some tests or establish some user tests to confirm that your refactored changes actually function. Then, I take some time to whiteboard the existing code, writing out how the different components and functions interact and where the pain points are. Often that's enough and I can go straight to ripping out the offenders and replacing them with improvements. Once the tests pass, you're free.

### Publishing

Modern research publishing has two parts: the paper, and the code (and data). The code is very much underappreciated these days but this is changing. 