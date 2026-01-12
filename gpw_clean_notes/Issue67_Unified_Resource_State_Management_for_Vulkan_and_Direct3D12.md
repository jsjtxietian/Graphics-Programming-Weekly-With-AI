2018-12-17: [Unified Resource State Management for Vulkan and Direct3D12](http://diligentgraphics.com/2018/12/09/resource-state-management/)

- explains the state management system implemented for the Diligent Engine
- resources states are exposed on D3D12 style semantic for barriers
- allows mixing of automatic and manual explicit state management
- the developer can choose to disable automatic transitions on a per resource basis
- can switch on a per-resource basis at any time during the frame
