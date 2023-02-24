# Pinpoint

Pinpoint is under active development, there is no requirement to maintain backwards compatibility with version changes.

## Organization

### Unity 

The Trajectory Planner is built out of a single [main repository](https://github.com/VirtualBrainLab/Pinpoint/) which holds the Unity codebase. Code that is shared across multiple VBL projects is stored in the [vbl-core repository](https://github.com/VirtualBrainLab/vbl-core) which you should add to the main repo as a git submodule. The full pull sequence for the entire repository is:

```
git clone https://github.com/VirtualBrainLab/Pinpoint
git submodule add https://github.com/dbirman/vbl-core Assets/vbl-core
```

If you use Github Desktop the `vbl-core` repository will automatically be pulled. If you are working on multiple VBL projects you should add the repository as a separate repo in Desktop and give it an alias, e.g. `Pinpoint-vbl-core`.

#### Additional assets

Some of the asset folders are too large to push to Github. We store these separately in a [Google Drive folder](https://drive.google.com/drive/folders/1aGtR8W7rTRgMShMX2Gn-8vXFp29jiwQT?usp=sharing). Download these and unzip them into the `/Assets/` folder in Pinpoint.

#### Branch structure

The latest minor release version (e.g. X.Y.**Z**) is kept on the **main** branch and released to the [/Pinpoint/](https://data.virtualbrainlab.org/Pinpoint/) folder.

The latest development build is kept on the **develop** branch and released to the [/Pinpoint-develop/](https://data.virtualbrainlab.org/Pinpoint-develop/) folder.

Incremental features are built on separate branches off of develop and are not released to the public. Outdated builds will be kept available in their corresponding [/Pinpoint_X.Y.Z/](https://data.virtualbrainlab.org/Pinpoint/) folder on the server. Until **v1.0.0** we are not making any promises of backward compatibility or maintenance. 

#### Build process

A Windows (win64) and WebGL build configuration are included 

To run a new build there are three steps:

  1. Re-build [Addressables Storage](https://github.com/dbirman/AddressablesStorage/) (if needed) and push this to the server.
    a) If you modify the storage files you need to update the version number in Pinpoint
  2. Re-build the Addressables build for Pinpoint and push this to the server.
    a) You can copy the files without over-writing the existing files, to maintain backward compatibility
  3. Build the WebGL build and again push these files to the server in the htdocs/Pinpoint/ folder. We recommend labeling the folder with the version number.

Once you confirm that the new version works you can re-name the folders appropriately. The current stable version is always labeled `Pinpoint` and older versions have the version number appended, e.g. `Pinpoint_0_1_0`.

#### IL2CPP

You may have to install optional visual studios features, specifically the Windows 10 SDK and MSVC, see: https://forum.unity.com/threads/unable-to-build-il2cpp-in-2021-2.1189441/

### Assets

Most of the VBL assets are shared across projects, these are accessed from a shared [Addressables Storage](https://github.com/VirtualBrainLab/AddressablesStorage/) repository. Shared assets are accessed via the `AddressablesRemoteLoader` class in `vbl-core`, see [here](https://github.com/VirtualBrainLab/vbl-core/tree/main/Scripts/Addressables).

### Scenes

When contributing to a VBL project you should avoid modifying the main scenes, except to add or remove **Prefab** objects. Merges between scenes are very difficult to handle in git and should be avoided.

## Core components

### Code

The trajectory planner runs out of a central class `TrajectoryPlannerManager` or `tpmanager` which coordinates loading the main functionality of the planner.

#### Managers

Manager classes handle the high-level coordination of functionality in Pinpoint. In general, creating and using Manager classes that share an AssemblyDefinition with TrajectoryPlannerManager should be avoided as much as possible.

#### Function code

Function classes handle the isolated functionality of specific features in Pinpoint. For example, the code allowing control of the Camera is an isolated functionality. Other examples include the Accounts system, Ephys Link, the Rig code, etc.

#### Modules

Modules contain code that needs to be re-used across Functions. For example, the CoordinateSpace/CoordinateTransform classes, or the ProbeInsertion class.

#### Assembly definitions

We have a three level assembly definition hierarchy. The top level is `trajectoryplanner` which contains `*Manager` classes. The second level is `trajectoryplanner.function` where `function` refers to a specific functionality in Pinpoint. The bottom level is `trajectoryplanner.function.module` where module is a set of scripts that may be re-used across functions. For example, `trajectoryplanner.core.utils` holds a set of convenience functions for parsing data files. The folder structure in the `Scripts/` folder should reflect the assembly definition hierarchy.

Because of this hierarchy, Managers can see *all* Functions, but Functions cannot see Managers or other Functions. All code can access modules.

#### UnityEvent callbacks

There are four ways that Manager and Function classes might need to communicate.

 1. A Manager needs to send data to a Function. Because Manager classes can be linked directly to Functions, you can define a function that takes a variable as input in your Function class.
 2. A Manager needs to request data from a Function. Because Manager classes can be linked directly to Functions, you define a function with a return type in your Function class.
 3. A Function needs to send data to a Manager or another Function. Functions *cannot see* Manager or other Function classes. Instead, to send data to a Manager you should expose a [UnityEvent](https://docs.unity3d.com/ScriptReference/Events.UnityEvent.html) that the Manager/Function can subscribe to. 
 4. A Function needs to request data from a Manager or another Function. Again, Functions *cannot see* Manager or other Function classes. Instead, to request data you need to create a UnityEvent that the other code subscribes to. In the case of a Manager, the UnityEvent can trigger a callback that pushes data to the Function. In the case of another Function, the Unityevent should trigger a second UnityEvent that the original Function can be subscribed to.

### Datasets

#### Allen CCF

At the core of the planner is the Allen CCF annotation dataset. You can learn more about the dataset on the Allen's [documentation page](http://help.brain-map.org/display/mouseconnectivity/API#API-DownloadAtlas3-DReferenceModels=). We use the 25 um atlas which has dimensions 528 x 320 x 456, the `nrrd` file downloaded from the Allen. 

The annotation dataset is stored internally as a [Texture3D](https://docs.unity3d.com/ScriptReference/Texture3D.html) object for GPU access as well as in an [AnnotationDataset](https://github.com/dbirman/vbl-core/blob/main/Scripts/AllenCCF/AnnotationDataset.cs) object. 

The 3D models are controlled via the [CCFModelControl](https://github.com/dbirman/vbl-core/blob/main/Scripts/AllenCCF/CCFModelControl.cs) component. Models are loaded from the shared addressables system and the mesh is saved locally to render the models.

#### Rat atlas

[todo]

### Probes

Probe models are stored as prefabs and instantiated by the tpmanager. Each probe is controlled by a [ProbeManager](https://github.com/VirtualBrainLab/Pinpoint/blob/main/Assets/Scripts/TrajectoryPlanner/ProbeManager.cs) component which also handles probe movement. When a probe is moved it updates its associated probe panel prefabs, which are run by the [TP_ProbePanel](https://github.com/VirtualBrainLab/Pinpoint/blob/main/Assets/Scripts/TrajectoryPlanner/TP_ProbePanel.cs) and [ProbeUIManager](https://github.com/VirtualBrainLab/Pinpoint/blob/main/Assets/Scripts/TrajectoryPlanner/ProbeUIManager.cs) components. The probe panels are interpolated using a [custom shader](https://github.com/dbirman/vbl-core/blob/main/Shaders/VolumeShaders/ProbePanelSliceShader.shadergraph) which is a variant of the in-plane slice shader. 

#### Probe Insertion Coordinates

The [ProbeInsertion](https://github.com/VirtualBrainLab/Pinpoint/blob/main/Assets/Scripts/Insertion/ProbeInsertion.cs) class represents a target coordinate in space. At the lowest level a probe has a tip coordinate (Vector3: ap, ml, dv) space and a set of probe angles (Vector3: azimuth, elevation, spin). Note that a ProbeInsertion must be defined with both a CoordinateSpace and CoordinateTransform, which define the relationship between the insertion's coordinates/angles and Unity world space. 

Using an [AnnotationDataset](https://github.com/VirtualBrainLab/vbl-core/blob/main/Scripts/VolumeData/CCFAnnotationDataset.cs) it's possible to recover the entry/surface coordinate of an insertion. 

#### Coordinate Spaces and Transforms

Each Atlas space (e.g. mouse CCF, or rat Waxholm) has its own set of axes and coordinates. Even within a single species different researchers may have used different conventions to refer to directions in space. To deal with this, we introduce three concepts: Unity World Space, Coordinate Spaces, and Coordinate Transforms.

Unity "World" space is the ground truth space inside of Unity. It has an X, Y, and Z axis and units are measured in millimeters. The (0,0,0) coordinate is at the center of the space. All of the objects in the Unity scene are placed in Unity World coordinates. This is the *only real coordinate system in the Unity Editor*. What this means is that when you reference a Transform on a GameObject the `Transform.position` value is returning the object's coordinates in Unity World space. If you want to know where this coordinate is in a particular Coordinate Space, you would need to use the `World2Space` function. If you want to know what direction a unit vector points in a CoordinateSpace, you would use the `World2SpaceAxisRotation` function. 

<image src="../_static/images/pinpoint/coordinate_spaces.png" alt="overview image" position="left" style="width:100%">

A [CoordinateSpace](https://github.com/VirtualBrainLab/vbl-core/blob/main/Scripts/CoordinateSystems/CoordinateSpace.cs) defines an axis rotation and a relative offset for the (0,0,0) coordinate. For example, the CCF space defines a (13.2 x 11.4 x 8 mm) rectangle with the (0,0,0) coordinate in the "front, left, top" corner. The axes are rotated so that the +Z axis becomes +AP, the +X axis becomes -ML, and the +Y axis becomes -DV. In Pinpoint, we then override the relative offset by moving it to Bregma at (+5.4, +5.7, +0.33) in CCF Space.

A [CoordinateTransform](https://github.com/VirtualBrainLab/vbl-core/blob/main/Scripts/CoordinateSystems/CoordinateTransform.cs) is necessary to represent situations where a CoordinateSpace has been further rotated or warped. For example, you might want to know your coordinates in Paxinos space but visually see the Allen CCF annotations. To go back and forth between these spaces we use a CoordinateTransform. The simplest transform is an AffineTransform which can stretch or shrink each axes and/or reverse them and can apply rotations. For example, the MRITransform flips the directions in CCFSpace, applies a scaling to each axis, and pitches the brain up by five degrees. More complex non-linear transforms are also possible. 

**Unity World Space is Transformed**

The most important thing to keep in mind is that objects in the scene are positioned according to their transformed coordinates. What the heck does that mean!?! This means that the `Transform.position` of a 3D model in the scene is computed by calculating: `CoordinateSpace.Space2World(CoordinateTransform.Transform2SpaceAxisChange(coordinate))`. Note that we **do not un-transform the cooordinate** by using `CoordinateTransform.Transform2Space`, it's only correct to do this when you need to know where a Transformed coordinate is in a *different* CoordinateTransform. 

The reason that we represent objects in their Transformed coordinates is that this means that objects in the Unity scene obey euclidian geometry, i.e. the distance between two points in the Unity scene (and therefore in the Transformed space) can be calculated with `Vector3.Distance` and the angle between two vectors in the scene (and therefore in the Transformed space) can be calculated using `Vector3.Angle`, these distances are angles are the correct distances and angles in the Transformed Coordinate Space. If it's not obvious why this is important ask Dan to explain it.

**Moving between spaces and transforms**

Lets work through some examples.

*Where should I place the tip of a probe in Unity World space*: Because coordinates in the Unity scene represent the transformed coordinates we need to first take the coordinate and find it's position in its CoordinateSpace by calculating: `CoordinateTransform.Transform2SpaceAxisChange`, then to find the corresponding point in the scene we use `CoordinateSpace.Space2World`.

*How do I interpolate annotations along a probe insertion*: Here we are going to need to translate between two CoordinateSpaces: from the Space the insertion is defined in and to the space where the annotations are defined. In addition, we need two points a *start* and an *end* coordinate, so that we can keep track of directions as we do our transforms. In general, to translate between CoordinateSpaces you need to use Unity World space as an intermediate. So the full set of steps here would be:

 1. Un-transform the start/end coordinates: `CoordinateTransform.Transform2Space`
 2. Move into World Space: `CoordinateSpace.Space2World`
 3. Move into the new coordinate space: `CoordinateSpace.World2Space`
 4. Transform into the space's transform (if there is one): `CoordinateTransform.Space2Transform`

*How do I move vectors between tranforms and spaces?* Vectors are a special case, since we don't want to scale them and they have no origin, but we still want to make sure they get rotated correctly. Both `CoordinateSpace` and `CoordinateTransform` have special `AxisChange` functions that apply all rotations but skip scaling and origin changes, for use with vectors. If you pass a unit vector to these functions, they should return a unit vector. 

*How do I know the coordinates of a probe insertion in a different CoordinateTransform*: This happens when you change the active CoordinateTransform in the scene and all the probes need to be updated. This is as simple as going back into un-transformed space and then transforming into the new one. Hopefully it's clear how you do that by now!

## Building new features and fixing bugs

We use Github Issues to track development. Any changes you make should first be posted as an issue and flagged either as a *bug* or a *feature* and assigned to the relevant developer. When you complete adding a new feature you should either merge it to the corresponding development branch (if it's minor) or submit a pull request (if it's a major feature change). In either case, you should link to the relevant commit in the issue. 

We use a Project to track development on the planner and milestones to assign bugs/features to releases. 

When a **bug/feature** is closed it should be added to the incremental update list on the next Release page, or added to the current release as a **hotfix**.

## Builds

The Trajectory Planner can build to WebGL (primary), Windows, and Linux. Building to Mac is more complex than we can handle right now.

### Addressables

Any assets that don't need to be immediately loaded with the trajectory planner should be marked as Addressable and loaded asynchronously.

If you modified the Addressables assets you need to re-build these and deploy them on the asset server before you build to targets. In the Addressables Groups window go to Build > New Build > Default Build Script, or use Build > Update a Previous Build if you only modified existing assets but did not add new ones.

#### Remote Build and Load Paths

Addressables should be built to the remote build and load paths, which should point to `ServerData` and `http://data.virtualbrainlab.org/NPTraj/[BuildTarget]` respectively. These can be modified in the Addressables Profiles window.

### WebGL

WebGL builds function without extra steps, just zip the output directory, move it to the asset server, and swap it for the existing file. Note that there is an `.htaccess` file in the `Build` directory which needs to be manually copied to the new release.

### Windows

Windows builds function without extra steps, just zip the output directory and upload it as either a hotfix to the [Releases page](https://github.com/dbirman/NPTrajectoryPlanner/releases) (make sure to increment the hotfix number) or as a new release.

### Linux

Linux builds function but you need to load the build on a Linux machine and mark the output file as executable.

### Mac builds

Mac builds require extra steps to certify the build, we don't have the capacity right now to deal with these.