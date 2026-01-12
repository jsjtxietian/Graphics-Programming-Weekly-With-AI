2023-11-05: [Finding Real Polynomial Roots on GPUs](https://momentsingraphics.de/GPUPolynomialRoots.html)

- the article discusses the implementation details of an efficient method to compute roots of Polynomial functions with high degrees
- presents an overview of the underlying method (Bracketed Newton bisection) and the implementation issues related to performance and precisions
- shows how to use Nvidia's Nsight to identify the performance issues and how to resolve the register spilling problem to improve performance significantly
