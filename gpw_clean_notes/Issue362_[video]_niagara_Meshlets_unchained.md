Unknown Date: [[video] niagara: Meshlets unchained](https://www.youtube.com/watch?v=zROUBE5pLuI&t=6s)

- the video continues meshlet implementation and looks at task shader performance on AMD hardware
- starts with an overview of the technique implementation and presents the performance problem encountered using the AMD profiler
- explains how the driver implements task shaders and what causes the performance issue by patching the Linux drivers
- From there, implement a solution that uses compute shaders to cull meshlets instead of using task shaders
- presents performance and memory comparison against the native task shader solution
