2020-05-18: [Spatiotemporal reservoir resampling for real-time ray tracing with dynamic direct lighting](https://cs.dartmouth.edu/~wjarosz/publications/bitterli20spatiotemporal.html)

- the paper presents a new technique that allows a massive number of dynamic lights to be rendered in real-time
- the presented implementation shows 3.4 million dynamic, emissive triangles in under 50 ms
- this is archived by reusing information from spatially and temporally adjacent pixels to filter probabilities to guide rays
