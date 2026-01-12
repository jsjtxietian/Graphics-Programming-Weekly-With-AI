2019-11-10: [Coming to DirectX 12— Mesh Shaders and Amplification Shaders: Reinventing the Geometry Pipeline](https://devblogs.microsoft.com/directx/coming-to-directx-12-mesh-shaders-and-amplification-shaders-reinventing-the-geometry-pipeline/)

- the article explains the problem with the  classic GPU geometry pipeline
- mesh shaders allow kernels to execute on sub-parts of meshes and output per-vertex and per-primitive attributes
- amplification shaders are run before, and output decide how many mesh shaders to launch
- shows code examples on how to use the feature in both HLSL and C++ API
- ExecuteIndirect also supports launch mesh shaders from the GPU
