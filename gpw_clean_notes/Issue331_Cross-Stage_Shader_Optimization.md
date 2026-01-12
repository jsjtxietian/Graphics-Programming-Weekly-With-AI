2024-03-18: [Cross-Stage Shader Optimization](https://www.lunarg.com/news-insights/white-papers/cross-stage-shader-optimization/)

- the whitepaper presents which tools and optimizations passes in spirv-cross and glslang are available to optimize shaders, taking advantage of knowledge from multiple shader stages
- shows an example of how vertex outputs can be eliminated if the connected pixel shader doesn't read the attribute
