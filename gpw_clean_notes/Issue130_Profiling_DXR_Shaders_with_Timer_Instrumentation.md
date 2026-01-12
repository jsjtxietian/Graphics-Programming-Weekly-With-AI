2020: [Profiling DXR Shaders with Timer Instrumentation](https://devblogs.nvidia.com/profiling-dxr-shaders-with-timer-instrumentation/)

- new Nvidia extension for D3D12 that provides shaders the possibility to query timestamps from within a shader
- the article explains how to use this technique to visualize the performance of TraceRay( ... ) with a heatmap
- shows how to enable the extension in C++ and how to integrate it into a shader
- comparable to the [VK_KHR_shader_clock](https://www.khronos.org/registry/vulkan/specs/1.2-extensions/man/html/VK_KHR_shader_clock.html) extension
