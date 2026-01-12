2020-09-23: [Fighting Fragmentation: Vulkan Portability Extension Released and Implementations Shipping](https://www.khronos.org/blog/fighting-fragmentation-vulkan-portability-extension-released-implementations-shipping)

- the blog post provides an overview of the different API layering implementations (Vulkan on Metal, D3D11on12, etc..)
- Vulkan Portability Initiative exposes a new extension (VK_KHR_portability_subset) that allows these layers to mark features as unsupported
- progress on updating the conformance testing and device capabilities emulators to make them aware of these constraints
