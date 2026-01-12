2019-03-06: [Real-Time Continuous Level of Detail Rendering of Point Clouds](https://www.cg.tuwien.ac.at/research/publications/2019/schuetz-2019-CLOD/)

- a new technique for continuous level of detail generation of point clouds, designed for VF applications
- additive point storage, each point is assigned to one level
- compute shader used to iterate over all points, time-sliced over multiple frames, and builds a new vertex buffer that only contains required points
- each point is classified into distinct LOD levels + a random factor, this makes it possible to allow the set to be changed continuously
- points have a blend zone to reduce aliasing, in this zone point sizes are adjusted so that they gradually are blended to the final extent as the camera approaches the points
