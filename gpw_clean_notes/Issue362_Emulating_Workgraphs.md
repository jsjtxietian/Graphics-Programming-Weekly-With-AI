Unknown Date: [Emulating Workgraphs](https://github.com/HansKristian-Work/vkd3d-proton/blob/workgraphs/docs/workgraphs.md)

- the document explains how vkd3d-proton decides to emulate Vulkan Workgraphs using ExecuteIndirect
- discusses different trade-offs and design decisions made
- presents how the implementation compares against native implementations on both Nvidia and AMD
- many workloads are currently more efficient using this emulation code path than the native driver version
