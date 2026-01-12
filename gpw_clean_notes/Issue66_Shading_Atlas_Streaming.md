2018-12-09: [Shading Atlas Streaming](https://www.tugraz.at/institute/icg/research/team-steinberger/research-projects/sas/)

- object based shading approach designed for VR rendering
- splits rendering into client and server operations
- the server calculates visible geometry and object space shading
- the results are stored into a shading atlas
- the client receives a preprocessed vertex stream and the shading atlas
- the visible geometry is rendered from a single vertex buffer and shading is applied from the information cached in the shader atlas
- presents the memory management technique and mip-level selection
