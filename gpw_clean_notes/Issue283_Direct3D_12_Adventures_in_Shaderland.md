2023-04-15: [Direct3D 12: Adventures in Shaderland](https://godotengine.org/article/d3d12-adventures-in-shaderland)

- the article describes how Godot converts SPIR-V shaders to DXIL for D3D12
- covers the  old approaches (SPIRV-Cross) and why it was replaced with using Mesa’s NIR approach
- discusses what SPIR-V Specialization constants are and how a patchable DXIL is created to allow the approach with D3D12
