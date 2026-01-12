2022-04-30: [Faster Visibility Buffer/Deferred Material Rendering via Analytical Attribute Interpolation using Ray Differentials](https://www.reddit.com/r/GraphicsProgramming/comments/uf4ykj/faster_visibility_bufferdeferred_material/)

- the post presents a method for reducing the size of visibility output buffers and the effect on performance
- shows that it's more efficient to recalculate ray differentials than it is to rely on hardware differentials to be stored in additional channels
