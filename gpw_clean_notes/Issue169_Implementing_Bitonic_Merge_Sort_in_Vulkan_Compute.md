2021-02-04: [Implementing Bitonic Merge Sort in Vulkan Compute](https://poniesandlight.co.uk/reflect/bitonic_merge_sort/)

- Shows how to sort data on the GPU using Bitonic Merge Sort networks using GLSL/Vulkan compute
- Derives how to non-recursively calculate per-thread index pairs for sorting networks
- Explains how to orchestrate compute-shader dispatches for large input data
- provides example implementation that sorts pixel by the brightness
