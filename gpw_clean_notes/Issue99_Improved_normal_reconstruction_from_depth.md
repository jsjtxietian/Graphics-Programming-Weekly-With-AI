2019-09-22: [Improved normal reconstruction from depth](https://wickedengine.net/2019/09/22/improved-normal-reconstruction-from-depth/)

- the article presents what kind of artifacts happen when reconstructing normals from world space positions
- suggests how to reduce the artifacts by selecting triangles that are most likely to have originated from the same object
- additionally shows how to use compute shaders and group shared memory to optimize the reconstruction
