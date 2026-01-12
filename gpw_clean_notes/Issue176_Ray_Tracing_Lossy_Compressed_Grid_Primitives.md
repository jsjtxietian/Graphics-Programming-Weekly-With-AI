2021-03-29: [Ray Tracing Lossy Compressed Grid Primitives](https://www.embree.org/related.html)

- the paper presents a method that allows a 5−7× reduction in memory footprint compared to indexed triangle meshes
- this is archived by converting vertices into vertex grids and using compressed displacement vectors to compress the vertex data
- the additional work required to decompress the data adds around 15% of overhead
