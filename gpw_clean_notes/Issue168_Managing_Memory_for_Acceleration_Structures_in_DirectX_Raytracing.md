2021-01-31: [Managing Memory for Acceleration Structures in DirectX Raytracing](https://developer.nvidia.com/blog/managing-memory-for-acceleration-structures-in-dxr/)

- the article presents how to reduce memory usage of bottom level acceleration structure (BLAS)
- instead of using placed resources for each BLAS, it is recommended to sub allocate from one larger structure
