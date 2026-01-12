Unknown Date: [Bringing Ray-tracing into Remedy‘s Northlight Engine](https://www.youtube.com/watch?v=ERlcRbRoJF0)

- a brief overview of the concepts of the ray tracing extension
- started integration with replacing screenspace AO and shadow map implementations
- how to implement ray trace reflections, techniques to reduce noise and optimizations
- best optimization advice is to split ray casting and shading
- export ray hit information from raycasting shader, and shade samples later using a conventional compute shader
- overview of the indirect diffuse voxel solution used in Quantum Break and how ray tracing can be used to improve the results
