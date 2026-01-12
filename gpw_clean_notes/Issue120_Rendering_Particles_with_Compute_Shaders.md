2020-02-24: [Rendering Particles with Compute Shaders](https://miketuritzin.com/post/rendering-particles-with-compute-shaders/)

- presents an approach to render particle effects using compute shaders
- the primary focus is optimization for tiny, pixel-sized particles that are additively blended
- lacking support of atomic on floats requires float->int->float conversions in the shader and how this influences the final implementation
