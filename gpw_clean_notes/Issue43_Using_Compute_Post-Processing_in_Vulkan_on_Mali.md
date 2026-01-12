2018-06-15: [Using Compute Post-Processing in Vulkan on Mali](https://community.arm.com/graphics/b/blog/posts/using-compute-post-processing-in-vulkan-on-mali)

- how to use two Vulkan queues to enable optimal scheduling for compute-shader based post-processing
- discussion how fragment → compute can introduce bubbles on the hardware
- uses two software queues with semaphore synchronization to overlap early work in the frame of the following frame with the post-processing work of the previous frame
