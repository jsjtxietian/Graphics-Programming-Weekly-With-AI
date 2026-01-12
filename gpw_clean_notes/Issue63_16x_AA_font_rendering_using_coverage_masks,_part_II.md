2018-11-13: [16x AA font rendering using coverage masks, part II](https://www.superluminal.eu/2018/11/12/16x-aa-font-rendering-using-coverage-masks-part-ii/)

- part 2 of the series on font rendering
- shows the artifacts a regular grid sampling pattern causes and how a rotated grid improves the edges of glyphs that contain straight lines
- explains how to sample the grid efficiently by splitting the rotation into one horizontal and one vertical skew
- able to optimize the sampling by precalculating lookup tables
