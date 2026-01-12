2025-09-22: [The performance impact of vertex shader exports](https://interplayoflight.wordpress.com/2025/09/21/the-performance-impact-of-vertex-shader-exports/)

- detailed analysis of how increasing vertex shader exports affects rendering performance on NVIDIA GPUs and AMD integrated GPUs
- demonstrates that drawcall costs can significantly increase when exporting more data to the vertex shader stage
- uses Nsight Graphics profiling to show how bottlenecks and memory allocation patterns impact vertex-to-pixel data flow
