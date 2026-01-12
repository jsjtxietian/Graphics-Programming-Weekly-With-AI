2023-08-21: [Optimizing Metal: Stitch several Metal functions into a single shader using MTLFunctionStitchingGraph](https://mtldoc.com/metal/2023/08/18/optimizing-metal-stitching)

- the article presents how to use MTLFunctionStitchingGraph to allow the creation of a final shader from multiple pre-compiled pieces at runtime
- shows how to express that functions will be stitched at shader compile time, how to load and stitch the shaders from the API
- combines everything to show how to use the stitched graph to apply image processing operations
