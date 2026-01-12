2018-07-01: [Deferred Adaptive Compute Shading](http://www.cemyuksel.com/research/papers/DACS_HPG2018.pdf)

- technique changes shading rate adaptively based on the local content of the image
- partitions the framebuffer into subdivision levels; uses these to estimate the variance between neighboring pixels to decide if new shading information needs to be calculated or if the shading result can be estimated from neighboring pixels
