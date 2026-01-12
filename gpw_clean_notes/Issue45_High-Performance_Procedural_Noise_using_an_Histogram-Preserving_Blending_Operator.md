2018-07-01: [High-Performance Procedural Noise using an Histogram-Preserving Blending Operator](https://eheitzresearch.wordpress.com/722-2/)

- a technique that allows the generation of infinite output space from a small example texture (such a grass, snow) in a pixel shader only
- for example tillable terrain textures
- cheap to evaluate; 0.29ms for a fullscreen quad
- the approach is to partition the output space into a triangle grid and to pick three random patches from the input texture to blend to create the output patch
- this is made possible through the variance preserving blending operation, and this can also be used to improve triplanar mapping
