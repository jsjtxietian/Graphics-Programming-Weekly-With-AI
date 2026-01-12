2018-04-22: [Post-processing effects on optimization mobile gaming](https://community.arm.com/graphics/b/blog/posts/post-processing-effects-on-mobile-optimization-and-alternatives)

- uses a texture based and camera facing quad approach instead of a post-processing bloom
- lighting for terrain rendered into a low-res light map, sampled per-fragment
- terrain is rendered at 720p, up-scaled to 1080p
