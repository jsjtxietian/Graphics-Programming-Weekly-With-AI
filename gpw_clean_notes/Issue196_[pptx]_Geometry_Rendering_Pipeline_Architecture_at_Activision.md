2021-08-16: [[pptx] Geometry Rendering Pipeline Architecture at Activision](http://enginearchitecture.realtimerendering.com/downloads/reac2021_geometry_pipeline_rendering_architecture.pptx)

- the talk presents how Activision had to rethink the geometry pipeline when moving from tightly controlled levels to open worlds
- focusing on the shipped F+ and experimental V+ implementation
- shows what mesh types use what technique and explains the reasons
- showing how the GPU based pipeline has been implemented around bitmasks and data expansion
- presents performance numbers, final F+ culling pipeline reduces rendering time significantly
- additionally contains a look at a possible tile-based V+ / F+ hybrid pipeline
