# Development

The Trajectory Planner is under active development, there is no requirement to maintain backwards compatibility with version changes. We are aiming for a 1.0.0 release at the end of 2022.

## Organization

### Unity 

The Trajectory Planner is built out of a single [main repository](https://github.com/dbirman/NPTrajectoryPlanner/) which holds the Unity codebase. Code that is shared across multiple VBL projects is stored in the [vbl-core repository](https://github.com/dbirman/vbl-core) which you should add to the main repo as a git submodule. The full pull sequence for the entire repository is:

```
git clone https://github.com/dbirman/NPTrajectoryPlanner
git submodule add https://github.com/dbirman/vbl-core Assets/vbl-core
```

If you use Github Desktop the `vbl-core` repository will automatically be pulled. You should add the repository as a separate repo in Desktop and give it an alias, e.g. `NPTrajectoryPlanner-vbl-core` to distinguish it from other copies of the submodule if you are working on multiple VBL projects.

### Assets

Most of the VBL assets are shared across projects, these are accessed from a shared [Addressables Storage](https://github.com/dbirman/AddressablesStorage/) repository. Assets in this repository are accessed via the `AddressablesRemoteLoader` class in `vbl-core`, see [here](https://github.com/dbirman/vbl-core/tree/75889b1dc2d8de3b95c7864d8008b0fe01ae44ae/Scripts/Addressables).

### Scenes

When contributing to a VBL project you should avoid modifying the main scenes, except to add or remove **Prefab** objects. Merges between scenes are very difficult to handle in git and should be avoided.

There are two main scenes, a loading scene which loads very quickly and present users with a text warning that it takes time to load the main scene. A second scene loads the actual trajectory planner itself.

## Core components

The trajectory planner runs out of a central class `TP_TrajectoryPlannerManager` which coordinates loading the main functionality of the planner. Most of the code uses a hub-and-spoke model where other components will communicate with the tpmanager but not with each other, to reduce the likelihood of creating deadlock situations. 

### Annotation Dataset

At the core of the planner is the Allen CCF annotation dataset. You can learn more about the dataset on the Allen's [documentation page](http://help.brain-map.org/display/mouseconnectivity/API#API-DownloadAtlas3-DReferenceModels=). We use the 25 um atlas which has dimensions 528 x 320 x 456, the `nrrd` file downloaded from the Allen. 

The annotation dataset is stored internally as a [Texture3D](https://docs.unity3d.com/ScriptReference/Texture3D.html) object for GPU access as well as in an [AnnotationDataset](https://github.com/dbirman/vbl-core/blob/main/Scripts/AllenCCF/AnnotationDataset.cs) object. 

### Allen CCF 3D Models

The 3D models are controlled via the [CCFModelControl](https://github.com/dbirman/vbl-core/blob/main/Scripts/AllenCCF/CCFModelControl.cs) component. Models are loaded from the shared addressables system and the mesh is saved locally to render the models.

### Probes

Probe models are stored as prefabs and instantiated by the tpmanager. Each probe is controlled by a [TP_ProbeController](https://github.com/dbirman/NPTrajectoryPlanner/blob/main/Assets/Scripts/TP_ProbeController.cs) component which handles probe movement. When a probe is moved it updates its associated probe panel prefabs, which are run by the [TP_ProbePanel](https://github.com/dbirman/NPTrajectoryPlanner/blob/main/Assets/Scripts/TP_ProbePanel.cs) and [TP_ProbeUIManager](https://github.com/dbirman/NPTrajectoryPlanner/blob/main/Assets/Scripts/TP_ProbeUIManager.cs) components. The probe panels are interpolated using a [custom shader](https://github.com/dbirman/vbl-core/blob/main/Shaders/VolumeShaders/ProbePanelSliceShader.shadergraph) which is a variant of the Inplane Slice shader. 

### Inplane Slice

The inplane slice is rendered using a [custom shader](https://github.com/dbirman/vbl-core/blob/main/Shaders/VolumeShaders/InPlaneSliceShader.shadergraph) whose settings are controlled by the [TP_InPlaneSlice](https://github.com/dbirman/NPTrajectoryPlanner/blob/main/Assets/Scripts/TP_InPlaneSlice.cs) component.

### Collisions

### Rigs

Rigs are just a collection of 3D models stored as a prefab and marked as an addressable asset. These are loaded by the [TP_ToggleRigs](https://github.com/dbirman/NPTrajectoryPlanner/blob/main/Assets/Scripts/TP_ToggleRigs.cs) component, which also adds their corresponding colliders.  

## Building new features and fixing bugs

We use Github Issues to track development. Any changes you make should first be posted as an issue and flagged either as a *bug* or a *feature* and assigned to the relevant developer. When you complete adding a new feature you should either merge it to the main branch (if it's minor) or submit a pull request (if it's a major feature change). In either case, you should link to the relevant commit in the issue. 

When a **bug/feature** is closed it should be added to the incremental update list on the next Release page, or added to the current release as a **hotfix**.

## Builds

The Trajectory Planner can build to WebGL (primary), Windows, and Linux. 

### Addressables

Any assets that don't need to be immediately loaded with the trajectory planner should be marked as Addressable and loaded asynchronously.

If you modified the Addressables assets you need to re-build these and deploy them on the asset server before you build to targets. In the Addressables Groups window go to Build > New Build > Default Build Script, or use Build > Update a Previous Build if you only modified existing assets but did not add new ones.

#### Remote Build and Load Paths

Addressables should be built to the remote build and load paths, which should point to `ServerData` and `http://data.virtualbrainlab.org/NPTraj/[BuildTarget]` respectively. These can be modified in the Addressables Profiles window 

### WebGL

WebGL builds function without extra steps, just zip the output directory, move it to the asset server, and swap it for the existing file. Note that there is an `.htaccess` file in the `Build` directory which needs to be manually copied to the new release.

### Windows

Windows builds function without extra steps, just zip the output directory and upload it as either a hotfix to the [Releases page](https://github.com/dbirman/NPTrajectoryPlanner/releases) (make sure to increment the hotfix number) or as a new release.

### Linux

Linux builds function but you need to load the build on a Linux machine and mark the output file as executable.

### Mac builds

Mac builds require extra steps to certify the build, we don't have the capacity right now to deal with these.