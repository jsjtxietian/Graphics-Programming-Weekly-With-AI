2023-04-03: [You Can Use Vulkan Without Pipelines Today](https://www.khronos.org/blog/you-can-use-vulkan-without-pipelines-today)

- the blog post introduces the VK_EXT_shader_object extension that allows Vulkan to be used without pipeline objects
- instead, applications create shader objects for each stage (and optionally link these). All state setting is dynamic
- the article describes performance expectations that drivers need to follow if they report the feature as supported
- additionally describes how to test the feature on hardware today
