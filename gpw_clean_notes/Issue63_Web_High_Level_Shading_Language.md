2018-11-13: [Web High Level Shading Language](https://webkit.org/blog/8482/web-high-level-shading-language/)

- a new shading language, designed for use with WebGPU
- discusses the constraints of targeting the web, and the ability to convert to Metal, HLSL, and SPIR-V
- SPIR-V limitations also limit the expressiveness of WHLSL
- memory safety for arrays, getter and setter support
- does not support a preprocessor but instead uses a two-pass compilation model with specialization constants
- bindless binding model is not supported
