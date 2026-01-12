2021-11-24: [Tessellation-Free Displacement Mapping for Ray Tracing](https://perso.telecom-paristech.fr/boubek/papers/TFDM/)

- the paper presents a new approach that decouples displacement from the tessellation of the base mesh
- a displacement-specific acceleration structure is mapped onto the mesh, and tesselation factors are encoded seperate
- the BVH for the displaced geometry is computed instead of loaded from memory
