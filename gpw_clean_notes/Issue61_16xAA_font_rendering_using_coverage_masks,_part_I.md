2018-11-03: [16xAA font rendering using coverage masks, part I](https://www.superluminal.eu/2018/10/29/16xaa-font-rendering-using-coverage-masks-part-i/)

- presents a technique for font rendering that operates on coverage instead of visibility
- this allows fonts to remain sharp when moving on the screen and at varying font sizes
- for each pixel in a glyph, a 4x4 sub-sample grid of visibility samples is calculated ahead of time
- explains how to use this coverage mask to implement font rendering
- covering how to sample the coverage mark correctly for axis-aligned font rendering
