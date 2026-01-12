2018-09-03: [Contact-hardening Soft Shadows Made Fast](https://www.gamedev.net/articles/programming/graphics/contact-hardening-soft-shadows-made-fast-r4906/)

- explains what contact-hardening shadows are
- presents one technique that can be used to implement them and deal with artifacts
- discussions of a method to optimize the process by splitting the shadow mask generation into two passes
- the first pass generates the penumbra mask at a quarter resolution and the second pass generates the soft shadows, sampling from the quarter resolution penumbra mask
