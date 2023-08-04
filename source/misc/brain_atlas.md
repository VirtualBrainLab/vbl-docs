# BrainAtlas

The [BrainAtlas repository](https://github.com/VirtualBrainLab/BrainAtlas/) is a package which wraps the BrainGlobe Atlas API into a package for easy use in Unity.

## Data pipeline

BrainAtlas implements a Python pipeline which converts the bg-atlas API files into a convenient format for ingesting into Unity. The pipeline downloads and organizes the raw data into the /Pipelines/data/ folder for each available atlas.

Note that the data pipeline can take a long time to run, as it downloads each atlas locally.

### bg-atlas files

- annotation.tiff: annotation IDs
- metadata.json: name, citation + link, species, symmetric, resolution, orientation, version, shape, 4x4 transform matrix
- README.txt: 
- reference.tiff: reference image RGB
- structures.json: acronym, id, full name, hierarchy path, rgb color

### Intermediate data files

- Reference image: .bytes file with the flattened data from the reference image, in uint16 format (2 bytes per voxel)
- Annotation image: .bytes file with the flattened data from the annotation image, in uint32 format (4 bytes per voxel)
- structures.json
- Mesh files: .obj file for each region
- One-sided mesh files: .obj file for each region

### Unity files

### Pipeline steps

### Mesh splitting

A Blender script `convert_to_one_sided.blend` exists to load each individual mesh file and split it in half to expose just the left hemisphere.

### Processed files

In the Unity project, an editor script Convert2Unity implements a conversion pipeline to import the raw data into Unity and convert them to prefabs. There are two separate pipelines that get run, first converting the reference and annotation images and then converting the brain region metadata and mesh files.

The final output of this process are the prefab files that can be loaded via the BrainAtlasRemoteLoader component.

- Reference image: Texture3D RGB24
- Annotation image: Texture3D R16?, note that R=0 is reserved for regions with no annotation
- BrainAtlas prefab: Prefab that represents the CoordinateSpace and Transform

## BrainAtlasRemoteLoader

After installing the Unity package into a new project, you'll need to import the BrainAtlas prefab to be able to use the available features. Note that all of the loading functions are asynchronous

### Load an Atlas

Call the `BrainAtlas.LoadAtlas` function to load a single atlas. This loads the prefab for the atlas Space and any available Transforms into the scene and loads the ontology.

### Load an Annotation or Reference texture

Call the `BrainAtlas.LoadTexture` functions to obtain the Texture3D objects for this atlas.

### Load a Region

Call the `BrainAtlas.LoadRegion` to bring a single region into the scene. Note that there are three copies of every region, Full (both hemispheres), Left, and Right. 

## Development

### Adding new atlases

The pipeline should run for all existing bg-atlas atlases. 

### Under-the-hood for Pipelines

Pipeline steps:

1. ?
2. ?

### Building new bundles

The remote loader uses a simple versioning setup by tagging each build with a tag (e.g. v0.1.1). Increment the patch number if you are modifying an existing file. Increment the minor number if you are adding new files that don't modify existing functionality. Increment the major number if you are making a backward-incompatible change to the codebase.

To ensure backward-compatibility you should modify the remote URL to include the build target version as a suffix on the url. This avoids accidentally over-writing files and causing hash code mis-matches. 

### Pushing to the server

Build the addressable assets and copy the entire new `ServerData/` folder to the `ServerData/X.Y.Z/` folder on the local server. Make sure to build for Windows standalone, WebGL, MacOS, and Linux.

### Update projects

Existing projects should then be migrated to target the new storage version, by modifying the field in the `AddressablesRemoteLoader` component.