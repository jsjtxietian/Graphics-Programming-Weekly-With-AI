2018-09-21: [A Ray-Box Intersection Algorithm and Efficient Dynamic Voxel Rendering](http://www.jcgt.org/published/0007/03/04/)

- a new algorithm to compute the intersection point and surface normal of an oriented 3D box without precomputations or spatial data structures
- uses rasterizer pipeline to generate screen-space AABB to limit tests to only potentially visible pixels
- provides GLSL shader implementation
