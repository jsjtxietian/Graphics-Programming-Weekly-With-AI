2018-05-25: [Hybrid Multi-Frustum Logarithmic Depth Buffer](https://cesium.com/blog/2018/05/24/logarithmic-depth/)

- now using Logarithmic depth buffer when available
- writes custom depth in a pixel shader, this does disable early depth optimizations but still a performance win for their use-case
