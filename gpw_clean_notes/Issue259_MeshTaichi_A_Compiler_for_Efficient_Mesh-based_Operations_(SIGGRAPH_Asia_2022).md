2022-11-02: [MeshTaichi: A Compiler for Efficient Mesh-based Operations (SIGGRAPH Asia 2022)](https://github.com/taichi-dev/meshtaichi)

- the paper presents a mesh computation compiler that separates mesh operations from the data partitioning
- the system partitions meshes into sub-patches and reorganize mesh data so that attributes can be accessed from local on-chip memory
- presents performance results and compares against RXmesh, another system that tries to optimize mesh access patterns
