2018-09-18: [Introduction to Turing Mesh Shaders](https://devblogs.nvidia.com/introduction-turing-mesh-shaders/)

- new shader stages on Turing that allows the generation of primitives for direct consumption by the rasterizer
- task shader: emits mesh shader workgroups
- allows work on larger clusters, the selection of mesh resolution, ...
- mesh shader: generates primitives (index + vertex buffers)
- OpenGL shader implementation that uses the new shader stages to allow culling on a per-cluster basis and generation of efficient mesh data
- [video recording](http://on-demand.gputechconf.com/siggraph/2018/video/sig1811-3-christoph-kubisch-mesh-shaders.html)
