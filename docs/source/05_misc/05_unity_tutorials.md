# Unity

## General tips

**Tutorials**

Brackeys has a great high quality introductory sequence: [start here](https://www.youtube.com/watch?v=j48LtUkZRjU&list=PLPV2KyIb3jR5QFsefuO2RlAgWEz6EvVi6)

[Imphenzia](https://www.youtube.com/watch?v=pwZpJzpE2lQ) also has a great and slightly more up-to date introduction.

### Version and packages

The majority of our code relies only on the base Unity environment. We are currently (2022-06) on Unity Editor version 2020.3 LTS. We will move to the 2021 LTS when all of our required packages have migrated. We also migrate as soon as a new version is available.

Below are a list of all the major packages we use with a short explanation for their use.

### Neurons (DOTS/ECS)

To display large numbers of neurons we rely on the entities and components system (ECS) from DOTS. This codebase organizes memory in a more efficient layout which allows us to render and update hundreds of thousands of scene objects on each frame.

**Tutorials**: [Turbo Makes Games](https://www.youtube.com/c/TurboMakesGames) probably has the best tutorials for DOTS/ECS. 

### Large asset streaming (Addressables)

Whenever we have to store and load large files we rely on Unity's impressive Addressables asset bundle system. They use state-of-the-art compression and streaming which seriously reduces the overhead for us when using very large files. 

Addressable assets are an excellent way to reduce memory overhead in builds, but they come at the cost of increased complexity and the requirement to write code with asynchronous function calls.

**Tutorials**: Bit out of date but this one by [Jason Weimann](https://www.youtube.com/watch?v=uNpBS0LPhaU) is good.

**Warning:** Addressables rely on the Unity version matching in the Addressables build and the Unity build, if you make any changes you must update the builds and change them on the asset server.

### Networking (Unity Netcode for Gameobjects)

The currently not-in-development education tools used a Server/Client architecture to stream information about the neural datasets. We set this up using Unity's Netcode for Gameobjects architecture. It's possible that in the future a better solution would be to use Addressables for this purpose.

## WebGL limitations

When developing new Unity tools you should be very careful about introducing new memory requirements or heavy GPU usage. WebGL has a frame rate limitation of about 60hz on most computers and a memory limitation of 2GB.
