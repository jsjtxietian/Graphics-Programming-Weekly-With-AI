2018-11-04: [large scale ambient occlusion: eliminating light leaks](https://www.dsdambuster.com/blog/lsao-part-2)

- presents how to reduce light leaks in a large scale global illumination system
- each geometry is associated with markup information about visibility zones
- GI light data is only applied if two pieces of geometry are in the same visibility zone or are visible through connected portals
