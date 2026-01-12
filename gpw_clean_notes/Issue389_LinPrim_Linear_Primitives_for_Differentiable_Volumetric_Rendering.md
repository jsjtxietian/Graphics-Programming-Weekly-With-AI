2025-04-28: [LinPrim: Linear Primitives for Differentiable Volumetric Rendering](https://arxiv.org/abs/2501.16312v3)

- this paper explores alternative scene representations using transparent polyhedra (octahedra and tetrahedra) with triangular faces
- presents a differentiable rasterizer that efficiently runs on GPUs, enabling end-to-end gradient-based optimization with real-time rendering
- achieves comparable quality to state-of-the-art volumetric methods like 3D Gaussians while requiring significantly fewer primitives
- the bounded nature of these primitives creates natural compatibility with traditional mesh-based tools for downstream applications
