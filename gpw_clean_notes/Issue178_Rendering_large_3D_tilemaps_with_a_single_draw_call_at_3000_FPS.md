2021-04-10: [Rendering large 3D tilemaps with a single draw call at 3000 FPS](https://blog.paavo.me/gpu-tilemap-rendering/)

- the articles describes the evolution of a multiple layered tilemap renderer
- starting at using the build-in Unity renderers, showing the incremental improvements
- the final solution is a custom rendering stack that stores the layers as voxels, containing indices into texture array slices
