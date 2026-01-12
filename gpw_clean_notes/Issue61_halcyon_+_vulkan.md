2018-11-04: [halcyon + vulkan](https://www.ea.com/seed/news/khronos-munich-2018-halcyon-vulkan)

- presents an architecture overview of the engine
- render backends are implemented as DLLs that can be reloaded at runtime
- multiple backends can be loaded at the same time
- resource handle system that allows the same resource to point to physical instances on multiple GPUs
- GPU work is recorded into an abstract command stream that is later compiled into API specific format
- render graph system that manages resource transitions, lifetimes, and execution order
- showcase of shader binding model
- using HLSL spaces concept to separate between update frequencies
- explanation how the HLSL resource binding model was emulated with SPIR-V using shader patching
