# Addressables Storage

The Addressables Storage repository holds binary files and assets that are re-used across multiple projects. Loading these files is done through the `AddressablesRemoteLoader` component which can be attached to any empty GameObject.

## Adding a new file

### Setting up the asset

You can add a new file by importing it into the project and marking it as Addressable in the inspector. The file will be assigned a string for access, which you will need to use when loading the file in the remote loader. Set the group settings appropriately so that the file loads as part of an existing or new bundle.

Make sure to set the "load separately" flag if your bundle contains multiple assets that need to be separated.

In the remote loader you will then need to add a function so that other projects can access the file. Use the existing examples as a template.

### Building new bundles

The remote loader uses a simple versioning setup by tagging each build with a tag (e.g. v0.1.1). Increment the patch number if you are modifying an existing file. Increment the minor number if you are adding new files that don't modify existing functionality. Increment the major number if you are making a backward-incompatible change to the codebase.

### Pushing to the server

Build the addressable assets and copy the entire new ServerData/ folder to the local server. Make sure to build for Windows standalone and for WebGL (and Linux, if needed).

### Update projects

Existing projects should then be migrated to target the new storage version, by modifying the field in the `AddressablesRemoteLoader` component.