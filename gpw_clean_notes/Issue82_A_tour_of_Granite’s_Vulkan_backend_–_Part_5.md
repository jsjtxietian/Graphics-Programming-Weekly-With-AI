2019-04-27: [A tour of Granite’s Vulkan backend – Part 5](http://themaister.net/blog/2019/04/27/a-tour-of-granites-vulkan-backend-part-5/)

- presents how render passes are expressed in the user-facing API
- shows how layout transition for external dependencies are handled
- separate logic for user-created, WSI images and transient images
- suggests that barriers should be treated at a higher level inside a frame graph architecture
