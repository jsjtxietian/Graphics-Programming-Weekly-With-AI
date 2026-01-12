2025-08-11: [AMD releases Vulkan support for Dense Geometry Format](https://gpuopen.com/learn/dense-geometry-format-amd-vulkan-extension/)

- introduces VK_AMDX_dense_geometry_format, a provisional Vulkan extension for using pre-compressed DGF data in acceleration structure builds
- eliminates performance and memory costs of separate decoding steps by providing DGF data directly to the GPU
- improves BLAS build time and reduces memory footprint on hardware with native DGF support
