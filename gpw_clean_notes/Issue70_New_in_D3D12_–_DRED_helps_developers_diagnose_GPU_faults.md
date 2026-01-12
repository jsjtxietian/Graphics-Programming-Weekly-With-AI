2019-01-28: [New in D3D12 – DRED helps developers diagnose GPU faults](https://blogs.msdn.microsoft.com/directx/2019/01/24/dred/)

- D3D12 adds support for DRED (device removed extended data) in the latest windows insider preview build
- writes an auto-incrementing counter after each render-operation into memory that is persistent across device removed events
- this allows the GPU progress to be inspected during post-mortem analysis
- the overhead is around 2 to 5 % for a frame of a AAA game, therefore defaults to off and needs to be enabled explicitly
- additionally allows better tracking of page faults
- tries to detect access to recently deleted objects
- shows the API to enable and how to use it to enable and inspect provided data
