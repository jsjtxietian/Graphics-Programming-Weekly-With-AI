2022-04-11: [My personal hell of translating DXIL to SPIR-V – part 4](https://themaister.net/blog/2022/04/11/my-personal-hell-of-translating-dxil-to-spir-v-part-4/)

- the article presents a detailed look at how different D3D12 ConstantBuffer patterns are mapped into SPIR-V
- shows how the patterns are mapped onto the hardware in RDNA2 ISA
- discusses how non-uniform resource influences the code generation
- additionally discusses quirks/limitations of ByteAddressBuffers and RWStructuredBuffer
