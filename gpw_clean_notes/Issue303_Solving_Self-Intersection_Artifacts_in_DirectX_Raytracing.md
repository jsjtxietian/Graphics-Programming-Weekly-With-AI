2023-08-31: [Solving Self-Intersection Artifacts in DirectX Raytracing](https://developer.nvidia.com/blog/solving-self-intersection-artifacts-in-directx-raytracing/)

- the article presents a robust solution to resolve self-intersection issues with secondary rays
- the proposed solution works by calculating error bounds and offset the starting point to lie outside of these bounds
- presents methods to reduce floating point numerical issues through using the suitable coordinate space and operation ordering
- HLSL and GLSL implementations are provided
