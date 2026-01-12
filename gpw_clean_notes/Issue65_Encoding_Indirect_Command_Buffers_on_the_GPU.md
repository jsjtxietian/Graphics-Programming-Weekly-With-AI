2018-12-03: [Encoding Indirect Command Buffers on the GPU](https://developer.apple.com/documentation/metal/advanced_command_setup/encoding_indirect_command_buffers_on_the_gpu)

- a sample that explains how to use Metal to generate render commands on the GPU
- implements GPU culling only to issue rendering commands for visible meshes and remove empty draws
- the final command buffer submission is controlled from the CPU
