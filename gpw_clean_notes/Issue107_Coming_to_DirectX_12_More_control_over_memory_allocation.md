2019-11-19: [Coming to DirectX 12: More control over memory allocation](https://devblogs.microsoft.com/directx/coming-to-directx-12-more-control-over-memory-allocation/)

- D3D12 is adding two new flags for memory heap creation
- D3D12_HEAP_FLAG_CREATE_NOT_RESIDENT, the heap is created non-resident state to enable EnqueueMakeResident to be used for heaps
- D3D12_HEAP_FLAG_CREATE_NOT_ZEROED enables an optimization that allows non-zeroed pages to be returned
