2021-01-14: [RenderDoc ‘Ref All Resources’ + Vulkan + Memory Aliasing = Beware](https://www.yosoygames.com.ar/wp/2021/01/renderdoc-ref-all-resources-vulkan-memory-aliasing-beware/)

- the post shows how aliased resources can cause problems when doing render doc captures
- aliased textures that are captured might need barrier transitions, which can corrupt other textures in the same memory range
