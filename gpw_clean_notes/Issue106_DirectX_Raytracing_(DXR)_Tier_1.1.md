2019-11-09: [DirectX Raytracing (DXR) Tier 1.1](https://devblogs.microsoft.com/directx/dxr-1-1/)

- the article explains what has been added with DXR tier 1.1
- it doesn't require new hardware features but needs a new windows version and driver support
- provides an alternative to that doesn't use separate dynamic shaders or shader tables
- inline shaders allow all shader stages to trace rays
- additionally added features are DispatchRays generated on the GPU
- growing state objects, GeometryIndex() in ray shaders, flags to skip triangles / procedural geometry
