2022-12-24: [Two-Pass Occlusion Culling](https://medium.com/@mil_kru/two-pass-occlusion-culling-4100edcad501)

- the blog posts describes how Hierarchical Z-Buffer (HZB) Occlusion Culling uses a depth buffer to improve culling efficiency
- describes two possible solutions that can be used to solve the problem that a depth buffer of the view is required to accelerate the rasterization of the same view
- focuses on a technique that uses information about which objects have been visible in the previous frame to accelerate the current
