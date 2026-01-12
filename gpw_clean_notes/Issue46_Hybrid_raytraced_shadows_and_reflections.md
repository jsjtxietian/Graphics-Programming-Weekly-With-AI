2018-07-10: [Hybrid raytraced shadows and reflections](https://interplayoflight.wordpress.com/2018/07/04/hybrid-raytraced-shadows-and-reflections/)

- implementation of a hybrid approach that mixes rasterization for first hit and raytracing for secondary rays
- tracing against polygons using compute shaders directly (no raytracing API)
- how to create a BVH structure and traverse it
- details about how to raytrace for shadows and reflections
- look at the performance, mainly memory bound
