2019-09-15: [The making of Gears 5: how the Coalition hit 60fps - and improved visual quality](https://www.eurogamer.net/amp/digitalfoundry-2019-gears-5-tech-interview)

- interview discussing the details of the Gear 5 implementation
- all post-processing and UI rendering is done post-upscaling in the output resolution
- using [Relaxed Cone Stepping](https://developer.nvidia.com/gpugems/GPUGems3/gpugems3_ch18.html) for extra details instead of parallax occlusion mapping
- a mix of shadow maps and ray-traced distance field shadows
