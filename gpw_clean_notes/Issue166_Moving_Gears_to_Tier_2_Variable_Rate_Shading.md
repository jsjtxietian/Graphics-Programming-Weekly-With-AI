2021-01-14: [Moving Gears to Tier 2 Variable Rate Shading](https://devblogs.microsoft.com/directx/gears-vrs-tier2/)

- the article presents how VRS tier 2 shading was integrated into Gears
- uses the previous frame color buffer results to run a Sobel edge detection compute shader to detect the shading rate
- a conservative VRS allows systems to opt-in for special quality if required
- contains advice on optimizations for VRS tile texture generation
- additionally provides guidance on how to estimate performance using Tier 1
- provides performance numbers for the savings from different render passes
