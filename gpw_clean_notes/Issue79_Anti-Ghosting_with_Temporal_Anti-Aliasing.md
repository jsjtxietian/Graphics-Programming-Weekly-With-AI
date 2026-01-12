2019-04-07: [Anti-Ghosting with Temporal Anti-Aliasing](http://stevekarolewics.com/articles/anti-ghosting-taa.html)

- presents techniques used to alleviate ghosting in the TAA solution of "The Grand Tour Game"
- uses the stencil to mark object groups and does not blend between with history buffer pixels when the stencils differ
- uses per-pixel depth and velocity to disable TAA so as to further reduce ghosting on shadows
