2019-04-20: [A tour of Granite’s Vulkan backend – Part 2](http://themaister.net/blog/2019/04/17/a-tour-of-granites-vulkan-backend-part-2/)

- presents how memory, object lifetime and command buffers are managed
- resource lifetime is bound to a frame context
- frame context tracks which resources can be deleted once the frame has been consumed
