2019-01-28: [Vulkan - GPU-Assisted Validation](https://vulkan.lunarg.com/doc/sdk/1.1.97.0/windows/gpu_validation.html)

- latest Vulkan SDK version (1.1.97.0) adds GPU assisted validation
- validates at runtime that shaders are not accessing any descriptors out of bounds
- this is achieved by adding instrumentation into the SPIR-V
- the document explains the constraints of the layer, known issues and an overview of the implementation details
