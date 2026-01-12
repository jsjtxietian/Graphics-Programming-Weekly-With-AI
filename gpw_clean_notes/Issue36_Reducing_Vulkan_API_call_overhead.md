2018-05-01: [Reducing Vulkan API call overhead](https://gpuopen.com/reducing-vulkan-api-call-overhead/)

- vulkan function calls pass through several layers until the actual function is  executed
- looks at the disassembly to evaluate the cost of this (between 1-5%)
- and how to bypass many layers to reduce the overhead
