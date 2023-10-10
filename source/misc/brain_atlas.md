# BrainAtlas

[BrainAtlas for Unity](https://github.com/VirtualBrainLab/BrainAtlas/) is a package which wraps the BrainGlobe Atlas API into a package for easy use in Unity.

There is currently no citation for BrainAtlas for Unity. Please cite the BrainGlobe Atlas paper when using this package: Claudi, F., Petrucco, L., Tyson, A., Branco, T., Margrie, T., & Portugues, R. (2020). BrainGlobe Atlas API: a common interface for neuroanatomical atlases. Journal of Open Source Software, 5(54), 2668-2668.

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
- Mesh files: *.obj file for each region, *L.obj file for each left hemisphere region
- Region centers: .csv file with the ap/ml/dv coordinate for the center of each area

### Unity files

When the pipeline runs it converts the intermediate files into a set of ScriptableObjects, Prefabs, and Textures:

- atlas metadata ScriptableObject: holds the name, dimensions, resolution, and other metadata
- parent Prefab: prefab that has the translation/rotation necessary to align the mesh files to the annotation data volume
- annotations.bytes: raw annotation values (uncompressed)
- annotation Texture3D: rgba annotation colors
- reference Texture3D: greyscale reference texture colors

## Using BrainAtlas

To use the package, simply import it from https://github.com/VirtualBrainLab/BrainAtlas.git?path=/Packages/vbl.brainatlas and then drag the BrainAtlas prefab into your scene. Then, link a callback to the `MetaLoadedEvent` that calls `BrainAtlasManager.LoadAtlas('atlas_name')`. That's it!

You can then access the active `ReferenceAtlas` object through `BrainAtlasManager.ReferenceAtlas` and the Ontology as a child of that.

Note that the Textures and annotations are not automatically loaded, you have to further load them by calling the loaders through the ReferenceAtlas object.

## Development

[TODO]

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