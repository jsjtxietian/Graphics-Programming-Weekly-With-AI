2018-05-21: [Kernel Foveated Rendering](http://duruofei.com/Research/KernelFoveatedRendering)

- implements foveated rendering through usage of log-polar transformation
- gbuffer is written as normal, attributes transformed into sub-resolution textures using a log-polar transformation
- shading is done in log-polar space before the results are transformed back into Cartesian space
