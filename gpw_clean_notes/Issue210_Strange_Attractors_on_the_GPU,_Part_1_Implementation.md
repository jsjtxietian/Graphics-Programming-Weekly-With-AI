2021-11-16: [Strange Attractors on the GPU, Part 1: Implementation](https://observablehq.com/@rreusser/strange-attractors-on-the-gpu-part-1)

- the article presents how to implement GPU particles with movement tails without CPU interaction
- all particle simulations happen in pixel shaders, and results are copied into ring buffers expressed as rows of textures
- implementation is provided using WebGL (regl)
