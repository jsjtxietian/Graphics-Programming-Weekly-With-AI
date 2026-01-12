2019-11-10: [On Histogram-Preserving Blending for Randomized Texture Tiling](http://jcgt.org/published/0008/04/02/)

- the paper presents a modification of histogram-preserving tiling algorithm discussed in [issue 45](https://www.jendrikillner.com/post/graphics-programming-weekly-issue-45/)
- it removes the lengthy 3D optimal transport preprocessing step and replaces it with per-channel lookup tables
- aims to reduce clipping and ghosting artifacts
- provides multiple blend modes that treat quality for performance
