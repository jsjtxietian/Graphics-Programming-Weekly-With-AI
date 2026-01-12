2019-11-19: [Vulkan Mobile Best Practices - Descriptor and Buffer Management](https://community.arm.com/developer/tools-software/graphics/b/blog/posts/vulkan-descriptor-and-buffer-management)

- the article provides an overview of how Vulkan descriptor set management influences CPU performance
- provides 3 possible solutions to the problem
- showing how they affect both performance and application implementation
- suggest a descriptor set caching scheme combined with using a single VkBuffer to store uniform data
