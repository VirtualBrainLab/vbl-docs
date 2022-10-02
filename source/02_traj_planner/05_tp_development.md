# Development

Pinpoint is under active development, there is no requirement to maintain backwards compatibility with version changes. We are aiming for a 1.0.0 release timed with SfN 2022.

## Organization

### Unity 

The Trajectory Planner is built out of a single [main repository](https://github.com/dbirman/NPTrajectoryPlanner/) which holds the Unity codebase. Code that is shared across multiple VBL projects is stored in the [vbl-core repository](https://github.com/dbirman/vbl-core) which you should add to the main repo as a git submodule. The full pull sequence for the entire repository is:

```
git clone https://github.com/dbirman/NPTrajectoryPlanner
git submodule add https://github.com/dbirman/vbl-core Assets/vbl-core
```

If you use Github Desktop the `vbl-core` repository will automatically be pulled. If you are working on multiple VBL projects you should add the repository as a separate repo in Desktop and give it an alias, e.g. `NPTrajectoryPlanner-vbl-core`.

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

You may have to install optional visual studios features specifically the Windows 10 SDK and MSVC, see: https://forum.unity.com/threads/unable-to-build-il2cpp-in-2021-2.1189441/

### Assets

Most of the VBL assets are shared across projects, these are accessed from a shared [Addressables Storage](https://github.com/dbirman/AddressablesStorage/) repository. Shared assets are accessed via the `AddressablesRemoteLoader` class in `vbl-core`, see [here](https://github.com/dbirman/vbl-core/tree/75889b1dc2d8de3b95c7864d8008b0fe01ae44ae/Scripts/Addressables).

### Scenes

When contributing to a VBL project you should avoid modifying the main scenes, except to add or remove **Prefab** objects. Merges between scenes are very difficult to handle in git and should be avoided.

## Core components

The trajectory planner runs out of a central class `TP_TrajectoryPlannerManager` which coordinates loading the main functionality of the planner. Most of the code uses a hub-and-spoke model where other components will communicate with the manager but not with each other, to reduce the likelihood of creating deadlocks. 

### Datasets

#### Allen CCF

At the core of the planner is the Allen CCF annotation dataset. You can learn more about the dataset on the Allen's [documentation page](http://help.brain-map.org/display/mouseconnectivity/API#API-DownloadAtlas3-DReferenceModels=). We use the 25 um atlas which has dimensions 528 x 320 x 456, the `nrrd` file downloaded from the Allen. 

The annotation dataset is stored internally as a [Texture3D](https://docs.unity3d.com/ScriptReference/Texture3D.html) object for GPU access as well as in an [AnnotationDataset](https://github.com/dbirman/vbl-core/blob/main/Scripts/AllenCCF/AnnotationDataset.cs) object. 

The 3D models are controlled via the [CCFModelControl](https://github.com/dbirman/vbl-core/blob/main/Scripts/AllenCCF/CCFModelControl.cs) component. Models are loaded from the shared addressables system and the mesh is saved locally to render the models.

#### Rat atlas

[todo]

### Probes

Probe models are stored as prefabs and instantiated by the tpmanager. Each probe is controlled by a [ProbeManager](https://github.com/dbirman/NPTrajectoryPlanner/blob/main/Assets/Scripts/ProbeManager.cs) component which also handles probe movement. When a probe is moved it updates its associated probe panel prefabs, which are run by the [TP_ProbePanel](https://github.com/dbirman/NPTrajectoryPlanner/blob/main/Assets/Scripts/TP_ProbePanel.cs) and [ProbeUIManager](https://github.com/dbirman/NPTrajectoryPlanner/blob/main/Assets/Scripts/ProbeUIManager.cs) components. The probe panels are interpolated using a [custom shader](https://github.com/dbirman/vbl-core/blob/main/Shaders/VolumeShaders/ProbePanelSliceShader.shadergraph) which is a variant of the Inplane Slice shader. 

#### Probe Coordinates

The `TP_ProbeController` component handles movement and positioning of probes. At the lowest level a probe is represented by it's AP (anterior-posterior), ML (medial-lateral), and DV (depth) coordinates and the azimuth (phi), elevation (theta), and spin of the probe. This data is stored inside of a [ProbeInsertion](https://github.com/VirtualBrainLab/NPTrajectoryPlanner/blob/main/Assets/Scripts/Insertion/ProbeInsertion.cs) object. 

Internally we represent positions in the CCF space starting from the front/left/top corner of the CCF space box (anterior, left, dorsal). The CCF box is 13.2 mm long on AP, 11.4 mm wide, and 8 mm deep. Probe coordinates are defined so that +AP goes posterior, +ML goes right, and +DV goes down. 

Probes also have a rotation. `phi` defines the probe's azimuth and we define 0 as forward (AP axis), -90 as facing left, and +90 as facing right. `theta` defines the probe's pitch with 0 being vertical and -90 horizontal, this is the only variable that we restrict to a specific range. `spin` controls the rotation of the probe on its own axis.

**Dealing with coordinate transforms**

There are two kinds of coordinate transforms we have to consider. First are conventions around presenting angles. The IBL defined angles differently with `phi=0` indicating left, -90 forward, and 90 backward. They also defined `theta=0` as vertical and `theta=90` as horizontal. There is a flag in the settings that changes how angles are displayed so that they match the IBL conventions. This does not have any effect under the hood.

The second kind of transforms we have to deal with are transformations of the CCF space itself, both linear affine and nonlinear warping. The raw CCF coordinates are not useful to most users, since almost all recordings are performed relative to bregma and in a live animal. The live mouse brain is quite different from the CCF brain (stretch on AP, squashed on DV, and tilted) and if you have individual MRIs for your mice you can do even better with your targeting.

**CoordinateTransforms**

We use a class `CoordinateTransform` to handle moving back and forth between spaces. Classes that implement this interface are required to have two functions `FromCCF` and `ToCCF` that let you go back and forth. These are used throughout the planner when displaying coordinates. The `CoordinateTransform` object is also required to have a `prefix` string, which we use to differentiate between which coordinate system a user is working in. Raw coordinates in the trajectory planner are therefore in `ccfAP` space (etc), while, for example, IBL NeedlesTransform coordinates are reffered to as `neAP` (etc).

Note again, these transforms are performed on the output coordinates (and reversed on input coordinates). Under the hood, everything is in CCF. Because of this it can sometimes be confusing to be moving the probe in what appears to be CCF space while seeing the target coordinates in a transformed space. If you want to *move* the probe in warped space you can enable an additional feature to **Warp 3D Meshes** which, when turned on, will warp all of the 3D mesh files into the current Transform space. On the back-end dealing with this is quite difficult -- we do this in two steps:
 1. We transform all the mesh vertices into the warped space.
 2. We transform the visible location of the probe into the warped space, while keeping the true position under the hood in CCF. 

### Inplane Slice

Each probe has a [TP_ProbeInsertion](todo) that defines the tip position in CCF AP/ML/DV and the probe angles in Phi/Theta/Spin. The ProbeController component handles interpolating the brain surface position that a probe is going through as well as the depth required to reach the target insertion coordinate.

When a [CoordinateTransform] is active in Pinpoint the ProbeController class modifies the tip and brain surface coordinates accordingly. Rotations are more complex -- (and not currently functional), but to deal with rotations the ProbeController will eventually interpolate the tip and surface coordinates and then back out the corresponding angles needed to reach these points. 

### In-Plane Slice

The in-plane slice is rendered using a [custom shader](https://github.com/dbirman/vbl-core/blob/main/Shaders/VolumeShaders/InPlaneSliceShader.shadergraph) whose settings are controlled by the [TP_InPlaneSlice](https://github.com/dbirman/NPTrajectoryPlanner/blob/main/Assets/Scripts/TP_InPlaneSlice.cs) component.

### Collisions

Collisions are handled by checking the overlap between all of the Probe `Collider` componenets against all of the Colliders in the scene. 

### Rigs

Rigs are a collection of 3D models stored as a prefab and marked as an addressable asset. These are loaded by the [TP_ToggleRigs](https://github.com/dbirman/NPTrajectoryPlanner/blob/main/Assets/Scripts/TP_ToggleRigs.cs) component, which also handles adding their corresponding colliders to the collision checks.  

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