2018-10-31: [Existing BC7 codecs don't handle textures with decorrelated alpha channels well](http://richg42.blogspot.com/2018/10/bc7-with-decorrelated-alpha.html)

- shows that BC7 encoders produce compression artifacts when the alpha channel is unrelated to the RGB channels
- presents a heuristic to decide what BC7 mode to use on a per-block basis to improve the compression
