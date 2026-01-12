2021-08-12: [Optimizing DX12 Resource Uploads to the GPU Using CPU-Visible VRAM](https://developer.nvidia.com/blog/optimizing-dx12-resource-uploads-to-the-gpu-using-cpu-visible-vram/)

- the article presents a new D3D12 Nvidia extension that enables a developer to allocate CPU-Visible VRAM memory directly
- this allows developers to write directly into VRAM from the GPU
- explains what tools are available to detect cases where it would be beneficial
- additionally shows how to detect possible performance problems caused by reading from the CPU
