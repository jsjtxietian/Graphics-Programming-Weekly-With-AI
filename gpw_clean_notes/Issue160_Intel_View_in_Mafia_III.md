2020-12-07: [Intel View in Mafia III](https://www.gamasutra.com/blogs/RaviTejaSanampudi/20201201/374488/Intel_View_in_Mafia_III.php)

- the article presents how the effect was implemented that allows objects to be colorized/silhouetted to make them pop out of the scene
- this is implemented by rendering AABB with per-object depth into a separate render target, marking tagged objects via stencil
- and using post-processing to apply the outline effect
