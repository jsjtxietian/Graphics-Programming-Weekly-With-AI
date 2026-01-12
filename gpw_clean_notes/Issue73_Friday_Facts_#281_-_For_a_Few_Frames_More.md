2019-02-09: [Friday Facts #281 - For a Few Frames More](https://factorio.com/blog/post/fff-281)

- presents performance optimizations done for the 2D rendering system
- reducing overdraw for blended objects
- discussion of texture compression formats for detailed 2D pixel art
- using [YCoCg-DXT compression](https://www.nvidia.com/object/real-time-ycocg-dxt-compression.html) to split luma and chrominance
- requires two textures instead of 1 but still a performance win for the game
