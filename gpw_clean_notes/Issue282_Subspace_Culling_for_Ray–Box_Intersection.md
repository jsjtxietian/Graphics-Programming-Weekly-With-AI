2023-04-12: [Subspace Culling for Ray–Box Intersection](https://gpuopen.com/download/publications/I3D2023_SubspaceCulling_updated.pdf)

- the paper proposes a new solution to accelerate AABB when used as BVH for objects that are thin and diagonal
- the solution presented embeds a binary voxel data structure for each node and showed how to use these to reduce false positives
- additionally presents how to use a LUT to compress the voxel data
