2024-07-30: [H-PLOC: Super-fast, high-quality BVH construction](https://gpuopen.com/download/publications/HPLOC.pdf)

- the paper presents an approach to BVH construction based on the parallel locally
- ordered clustering approach (PLOC) and PLOC++
- shows how to implement the algorithm in a single kernel launch
- explains a method to convert the binary BVH into wide BVHs where each parent can have an N number of child nodes
