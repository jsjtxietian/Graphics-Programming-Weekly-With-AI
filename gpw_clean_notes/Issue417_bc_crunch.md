2025-11-17: [bc_crunch](https://github.com/Geolm/bc_crunch)

- tiny dependency-free C99 library (~700 LOC) for lossless compression of GPU-compressed texture blocks (BC1, BC3, BC4, BC5)
- exploits spatial patterns, endpoint deltas, and Morton-ordered indices specific to BC formats achieving compression ratios of 1.5x-6x
- features deterministic bit-exact reconstruction with no malloc or external dependencies
