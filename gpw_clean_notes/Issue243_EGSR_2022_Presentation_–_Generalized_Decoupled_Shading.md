2022-07-06: [EGSR 2022 Presentation – Generalized Decoupled Shading](https://www.oxidegames.com/2022/07/egsr-2022-presentation-generalized-decoupled-shading/)

- the paper discusses a decoupled shading implementation that separates rasterization from shading by shading pixels before they are rasterized
- presents how it determines what pixels will need to be shaded
- what space to allocate for storing the shading results and how to execute the shading
- discusses strengths and weaknesses of the approach
- presents performance comparisons against a forward shading implementation
- it additionally covers numerous considerations that are required for a robust implementation
