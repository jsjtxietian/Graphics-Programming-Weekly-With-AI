2018-05-28: [GPU Driven rendering experiments at the Digital Dragons conference](https://interplayoflight.wordpress.com/2018/05/25/gpu-driven-rendering-experiments-at-the-digital-dragons-conference/amp/)

- discussions of problems with old occlusion culling systems
- renders occluders in a pre-pass, uses the depth information to cull instances
- how to implement culling against the depth  buffer, remove culled instance from the stream
- stream compaction implementation
- extend the system to handle LOD, materials and manual vertex fetching
- performance results on Nvidia  and Intel
