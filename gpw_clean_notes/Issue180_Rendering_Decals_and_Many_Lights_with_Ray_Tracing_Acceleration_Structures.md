2021-04-26: [Rendering Decals and Many Lights with Ray Tracing Acceleration Structures](http://i3dsymposium.github.io/2021/posters/hansen2021_rendering_decals_and_many_lights_paper.pdf)

- the paper presents a method that uses the AABS from hardware raytracing shaders to apply decals and lights
- uses a zero-length ray to collect all overlapping decals/lights per pixel
- compares performance against deferred decals
