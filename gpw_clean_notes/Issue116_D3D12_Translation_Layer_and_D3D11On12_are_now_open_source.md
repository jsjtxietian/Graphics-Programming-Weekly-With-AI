2020: [D3D12 Translation Layer and D3D11On12 are now open source](https://devblogs.microsoft.com/directx/d3d12-translation-layer-and-d3d11on12-are-now-open-source/)

- Microsoft open-sourced two layers to help to port to D3D12
- [D3D12 Translation Layer](https://github.com/microsoft/D3D12TranslationLayer) helps mapping from D3D11 style APIs to D3D12 style
- Resource binding, renaming, sub-allocation, pooling, and deferred destruction
- Batching and threading
- Residency management
- [D3D11On12](https://github.com/microsoft/D3D11On12) is implemented on top of the previous layer and contains the D3D11 specific aspects
