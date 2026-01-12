2025-12-07: [Minimalist ray-tracing leveraging only acceleration structures](https://anki3d.org/minimalist-ray-tracing-leveraging-only-acceleration-structures/)

- presents a low-quality ray tracing mode using ray queries and data stored in acceleration structures
- eliminates ray pipelines, shader binding tables, and texture access by storing average diffuse color in TLAS instanceCustomIndex
- uses VK_KHR_ray_tracing_position_fetch to compute face normals from triangle vertex positions
