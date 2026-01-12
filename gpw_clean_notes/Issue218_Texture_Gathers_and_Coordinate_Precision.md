2022-01-16: [Texture Gathers and Coordinate Precision](https://www.reedbeta.com/blog/texture-gathers-and-coordinate-precision/)

- the article presents a deep dive into a gather related artifact
- discusses texture filtering, how fixed point is involved and how many bits of sub-pixel precision is used on different GPU vendors
- shows the necessary parts in the Vulkan and D3D spec to understand why an offset is required to match the hardware behavior
