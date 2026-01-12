2018-06-06: [Pathtracer 13: GPU threadgroup memory is useful!](https://aras-p.info/blog/2018/05/28/Pathtracer-13-GPU-threadgroup-memory-is-useful/)

- moving the scene information into group shared memory to speed up the ray tracing code a lot
- problems on metal, slower unless passing data by value instead of by const reference
