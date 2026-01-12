2021-02-22: [Temporally Reliable Motion Vectors for Real-time Ray Tracing](https://sites.cs.ucsb.edu/~lingqi/#publications)

- the paper presents a new technique to generate more accurate motion vectors for shadows, glossy reflections, and occlusions
- the key idea is to detect and track the source of the effect (for example, the object blocking the light) and use the change of the source to adjust the back-projection accordingly
