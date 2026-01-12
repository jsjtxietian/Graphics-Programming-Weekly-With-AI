2020-07-17: [Optimizing Compute Shaders for L2 Locality using Thread-Group ID Swizzling](https://developer.nvidia.com/blog/optimizing-compute-shaders-for-l2-locality-using-thread-group-id-swizzling/)

- the article shows how to improve performance of fullscreen compute shader passes by tiling thread workloads to take advantage of memory locality
- test cases show an example improvement of 1.47x on memory bound workloads
