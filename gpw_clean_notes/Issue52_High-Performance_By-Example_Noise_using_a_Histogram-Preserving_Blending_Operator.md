2018-08-13: [High-Performance By-Example Noise using a Histogram-Preserving Blending Operator](https://www.highperformancegraphics.org/wp-content/uploads/2018/Papers-Session3/HPG2018_ByExampleNoise.pdf)

- slides for the technique discussed in [issue 45](https://www.jendrikillner.com/post/graphics-programming-weekly-issue-45/)
- explanation of problems with linear blending
- how contrast-preserving blending is able to mitigate some of these problems
- presents a histogram-preserving blending algorithm that has many use cases besides the introduced procedural texturing technique
- whenever you blend
- weighted data: use premultiplied blending
- data chosen randomly: use histogram-preserving blending
