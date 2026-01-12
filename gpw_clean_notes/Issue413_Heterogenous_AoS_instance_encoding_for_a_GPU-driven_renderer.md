2025-10-20: [Heterogenous AoS instance encoding for a GPU-driven renderer](https://zino2201.substack.com/p/heterogenous-aos-instance-encoding)

- presents a per-instance encoding technique for GPU-driven rendering with varying instance data requirements
- instances use type discriminants to allow different memory layouts within a unified buffer
- reduces memory bandwidth and footprint by eliminating unused fields
- allows different instance types to coexist efficiently in the same buffer
