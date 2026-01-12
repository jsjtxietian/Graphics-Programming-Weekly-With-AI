2018-05-01: [Dissecting the Rendering of The Surge](https://de.slideshare.net/philiphammer/dissecting-the-rendering-of-the-surge/)

- 100% dynamic lights, 16 shadow maps in 4kx4k atlas
- gbuffer breakdown
- stores material index in gbuffer, indexing into structured buffer for material information
- deferred decals have problems with depth discontinuities because of wrong mip selections
- use mip0 when depth discontinues are found around the pixel
- object decals, blending arbitrary meshes into the gbuffer
- working on bindless decals, follow the same pattern as clustered deferred lighting
