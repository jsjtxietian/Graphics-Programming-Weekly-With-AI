2021-03-01: [New game changing Vulkan extensions for mobile: Buffer Device Address](https://community.arm.com/developer/tools-software/graphics/b/blog/posts/vulkan-buffer-device-address)

- the article presents the buffer_device_address (BDA) extension for Vulkan
- this extension adds pointer support for Vulkan resources
- allows users to request the virtual memory address of each resource, operate on it, and even resolve it from within shaders
- shows how to use a pointer in a shader
- additionally covers debugging advice and how this is handled inside of SPIR-V
