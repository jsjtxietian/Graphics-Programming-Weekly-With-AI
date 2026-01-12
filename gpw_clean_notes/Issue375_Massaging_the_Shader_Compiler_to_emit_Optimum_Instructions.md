2025-01-13: [Massaging the Shader Compiler to emit Optimum Instructions](https://martinfullerblog.wordpress.com/2025/01/13/massaging-the-shader-compiler-to-emit-optimum-instructions/)

- The blog post provides examples of how different HLSL implementations cause very different codegen results.
- Shows that unintuitive implementations can be required to allow the compiler to map to native instructions.
- Suggests that compiler pattern matching hinders performance and it could be beneficial to expose native instructions as intrinsics.
