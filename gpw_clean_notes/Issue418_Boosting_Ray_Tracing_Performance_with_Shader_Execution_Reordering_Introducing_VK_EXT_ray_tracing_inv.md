2025-11-19: [Boosting Ray Tracing Performance with Shader Execution Reordering: Introducing VK_EXT_ray_tracing_invocation_reorder](https://www.khronos.org/blog/boosting-ray-tracing-performance-with-shader-execution-reordering-introducing-vk-ext-ray-tracing-invocation-reorder)

- announces the multi-vendor Vulkan extension VK_EXT_ray_tracing_invocation_reorder for Shader Execution Reordering (SER) to reduce divergence in ray tracing workloads
- explains how SER uses hit objects to separate ray traversal from shader invocation and allows the GPU to reorder invocations for improved coherence
- provides best practices, GLSL/Slang code examples, and how to profile with NVIDIA and AMD tools
