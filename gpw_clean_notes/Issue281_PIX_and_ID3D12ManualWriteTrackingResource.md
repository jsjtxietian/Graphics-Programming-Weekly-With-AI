2023-03-30: [PIX and ID3D12ManualWriteTrackingResource](https://devblogs.microsoft.com/pix/pix-and-id3d12manualwritetrackingresource/)

- the new API allows applications to disable the use of kernel WRITE_WATCH for CPU-visible GPU memory
- applications promise to track access and inform pix explicitly instead of relying on the OF
- this is required because of limitations in win10 and non-insider builds of windows 11 today that affect performance negatively
