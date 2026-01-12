2024-08-19: [Workarounds for issues with mesh shaders + Vulkan + HLSL](https://anki3d.org/workarounds-for-issues-with-mesh-shaders-vulkan-hlsl/)

- the blog post explains how HLSL shaders compiled for mesh shader usage with Vulkan require special annotations
- default shader behavior doesn't handle it correctly, and it only fails on AMD without any validation errors
