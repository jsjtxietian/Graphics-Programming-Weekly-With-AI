2021-02-16: [Bilinear down/upsampling, aligning pixel grids, and that infamous GPU half pixel offset](https://bartwronski.com/2021/02/15/bilinear-down-upsampling-pixel-grids-and-that-half-pixel-offset/)

- the article shows a few ways of doing bilinear upsampling and downsampling
- explains why it's essential to follow the same convention everywhere and verify that no unintended shifts are introduced
- suggests that the same half-pixel offset convention as used by GPUs should also be followed in CPU code
- discussing the different tradeoffs for performance/aliasing/smoothing
