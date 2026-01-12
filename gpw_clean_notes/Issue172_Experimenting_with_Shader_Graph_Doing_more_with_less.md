2021-02-26: [Experimenting with Shader Graph: Doing more with less](https://blogs.unity3d.com/2021/02/24/experimenting-with-shader-graph-doing-more-with-less/)

- the article presents an alternative way to pack PBR textures into a single 4 channel texture
- albedo information stored as a gradient with gradient reconstruction, normals stored as height derivates, and linear smoothness
- presents how this was integrated into Unity
- shows the setup tested on a 6 material blend setup and presents performance comparison against the classical packing
