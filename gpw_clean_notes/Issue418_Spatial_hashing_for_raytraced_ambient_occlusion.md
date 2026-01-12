2025-12-02: [Spatial hashing for raytraced ambient occlusion](https://interplayoflight.wordpress.com/2025/11/23/spatial-hashing-for-raytraced-ambient-occlusion/)

- implements a spatial hash structure to cache and accelerate ray-traced ambient occlusion for static scenes
- presents hash functions using PCG and xxhash32 with position and normal quantization to create cells that accumulate AO samples
- discusses distance-based cell sizing, conflict resolution via linear probing, and temporal management to handle hashmap capacity limits
