2023-06-11: [Far Cry Dunia Engine Shader Pipeline - Long-term Vision & Lessons Learned](https://enginearchitecture.realtimerendering.com/downloads/reac2023_dunia_shader_pipeline.pdf)

- the presentation covers the development story of the Far Cry shader system
- shows how over multiple games, the architecture was iteratively improved to solve the D3D12 transitions
- focuses on how the PSO design was approached by making all PSO information known during build time
- presents techniques to reduce PSO hitching by skipping draw calls, introducing optional variations, and allowing fallbacks
