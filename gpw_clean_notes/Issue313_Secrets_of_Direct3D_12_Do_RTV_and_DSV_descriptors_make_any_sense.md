2023-11-13: [Secrets of Direct3D 12: Do RTV and DSV descriptors make any sense?](https://asawicki.info/news_1772_secrets_of_direct3d_12_do_rtv_and_dsv_descriptors_make_any_sense)

- the article provides an overview of the way D3D12 deals with resource descriptors
- presents how shaders use the RDNA2 instructions use the descriptor when sampling
- from there, shows how Render/Depth targets are different and only used from the CPU side
