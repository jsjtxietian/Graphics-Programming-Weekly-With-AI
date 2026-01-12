2019-10-29: [Flow Control on PowerVR – Optimising Shaders](https://www.imgtec.com/blog/flow-control-on-powervr-optimising-shaders/)

- presents an overview of the difference between static and dynamic branching
- dynamic is a lot more expensive of PowerVR hardware
- shows examples of problematic cases with dynamic branching
- presents an extension that can be used to make the dynamic branch a lot more performant if all threads agree on a condition
