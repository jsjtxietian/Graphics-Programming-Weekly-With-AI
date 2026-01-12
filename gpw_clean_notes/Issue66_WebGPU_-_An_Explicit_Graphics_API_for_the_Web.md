2019: [WebGPU - An Explicit Graphics API for the Web](https://docs.google.com/presentation/d/1URnqb1Vuf2jPieHnt_eqXsPV_Es9Oog00_8LKZUdo6g/edit#slide=id.p)

- review of problems with classical APIs (OpenGL) and motivations for the creation of WebGPU
- presentation about Dawn, WebGPU implementation from Google
- splits into render passes that insert resource transitions between passes automatically
- how numerical fences are implemented (Monotonically increasing values indicate a timestamp in GPU execution history)
- considerations for implementations using cross-process communication
