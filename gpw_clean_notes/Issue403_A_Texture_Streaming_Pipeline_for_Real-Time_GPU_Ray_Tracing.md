2025-08-11: [A Texture Streaming Pipeline for Real-Time GPU Ray Tracing](https://www.yiningkarlli.com/projects/gpuptex.html)

- presents Disney Animation's solution for handling massive Ptex datasets (1.5 TB) in GPU ray tracing using only 2 GB of GPU VRAM
- employs a fast LRU eviction scheme and caps GPU cache size to maintain zero-stall experience while preserving texture detail
