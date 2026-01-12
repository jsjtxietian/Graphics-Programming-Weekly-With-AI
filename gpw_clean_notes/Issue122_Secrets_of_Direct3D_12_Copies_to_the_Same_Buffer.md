2020-03-05: [Secrets of Direct3D 12: Copies to the Same Buffer](https://asawicki.info/news_1722_secrets_of_direct3d_12_copies_to_the_same_buffer)

- the article presents multiple scenarios in D3D12 where manual barrier synchronization is required
- followed by a back-to-back copy into buffers that cannot be synchronized by barriers and shows the behavior observed on actual hardware
