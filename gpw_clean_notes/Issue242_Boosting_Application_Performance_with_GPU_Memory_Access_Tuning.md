2022-06-30: [Boosting Application Performance with GPU Memory Access Tuning](https://developer.nvidia.com/blog/boosting-application-performance-with-gpu-memory-access-tuning/)

- the article presents how to improve compute shader performance when workloads are memory limited
- presents how to detect if a CUDA shader runs into register limits
- it additionally shows how CUDA launch bounds (promises on work sizes) can give the compiler more information for more aggressive optimizations
