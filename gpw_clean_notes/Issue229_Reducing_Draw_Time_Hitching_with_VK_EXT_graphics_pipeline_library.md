2022-04-01: [Reducing Draw Time Hitching with VK_EXT_graphics_pipeline_library](https://www.khronos.org/blog/reducing-draw-time-hitching-with-vk-ext-graphics-pipeline-library)

- the blog post describes the functionality of the new pipeline library extension and how to use it to reduce draw-time shader compilation stalls
- the extension breaks up PSO compilation into four distinct areas Vertex Input Interface, Pre-Rasterization Shaders, Fragment Shader, Fragment Output Interface
- these separate aspects can then be linked together to create the PSO
- link-time optimizations are optional to trade compilation time for runtime performance
