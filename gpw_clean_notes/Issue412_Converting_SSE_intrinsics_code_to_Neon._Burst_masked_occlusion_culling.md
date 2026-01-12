2025-10-15: [Converting SSE intrinsics code to Neon. Burst masked occlusion culling](https://over17.github.io//2025/10/01/burst-occlusion-culling.html)

- details the process of translating SSE intrinsics to Neon for Unity's Burst compiler
- presents optimization techniques that improved performance by 2.3x through removing allocations
- discusses challenges with instruction equivalence and shows SIMD vectorization achieving 7-15x speedups
