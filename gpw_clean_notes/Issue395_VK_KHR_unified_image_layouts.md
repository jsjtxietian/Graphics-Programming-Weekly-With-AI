2025-06-17: [VK_KHR_unified_image_layouts](https://docs.vulkan.org/features/latest/features/proposals/VK_KHR_unified_image_layouts.html)

- presents a Vulkan extension that simplifies image layout management by allowing VK_IMAGE_LAYOUT_GENERAL to be used in most cases
- reduces the need for explicit image layout transitions to  simplify synchronization
- discusses how some hardware doesn't distinguish between image layouts, so not using the specific layouts doesn't cause performance issues
