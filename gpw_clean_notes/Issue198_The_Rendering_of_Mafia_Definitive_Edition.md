2021-08-26: [The Rendering of Mafia: Definitive Edition](http://www.elopezr.com/the-rendering-of-mafia-definitive-edition/)

- in-depth frame analysis of a nighttime scene in Mafia, a d3d11 based deferred rendering engine
- covers g-buffer, occlusion culling, decal blending, GI
- cars use a precalculated shadow texture to cast AO
- heavy use of stencil usage for volumetrics, sky, as well as the minimap rendering
