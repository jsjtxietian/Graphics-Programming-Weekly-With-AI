2019-09-19: [Non-linear sphere tracing for rendering deformed signed distance fields](https://cs.dartmouth.edu/~wjarosz/publications/seyb19nonlinear.html)

- the paper presents a method that allows SDFs to be combined with techniques such as linear skinning
- this is achieved by calculating a triangle mesh hull for the SDF, applying the transformation to the hull and using this to trace
- tracing linearly in transformed space follows a non-linear trace in untransformed space
