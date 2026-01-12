2025-09-13: [Dynamic levels of detail in Evolve](https://www.evolvebenchmark.com/blog-posts/dynamic-levels-of-detail-in-evolve)

- details a GPU-driven LOD system using solid angle calculations on camera unit spheres
- projects mesh AABBs onto the unit sphere to estimate screen coverage for LOD selection
- implements bindless rendering with unified vertex/index buffer access across all LOD levels
