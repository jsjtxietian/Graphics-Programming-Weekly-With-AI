Unknown Date: [Interval Shading: using Mesh Shaders to generate shading intervals for volume rendering](https://hal.science/hal-04561269)

- the paper proposes the use of tetrahedrons as primitives for volume rendering using mesh shaders
- uses mesh shaders to compute the depths of the front and back faces at the same time when interpolating vertex attributes and passing both depths to the rasterizer stage
- additionally presents how to use the same idea to implement SDF tracing
