2018-11-17: [Modern graphics abstraction and real-time ray tracing](https://www.ea.com/seed/news/syysgraph-2018-modern-graphics-abstractions-real-time-ray-tracing)

- overview of architecture
- multiple render backends are supported at the same time
- all GPU resources are referred to by a handle, resources can exist on multiple GPUs
- overview of the high-level command system that is recorded and translated into native API command buffers
- render graph system graph construction and execution
- how to deal with multiple GPUs
- virtual GPU system allows emulation of a multi GPU setup using a single GPU
- proxy backend routes rendering calls to a remote machine for execution
- a brief look at machine learning in a render graph architecture
- overview of the asset pipeline
- overview of hybrid rendering pipeline and how transparent shadows have been implemented using DirectX Raytracing
- discussing open problems with ray tracing
