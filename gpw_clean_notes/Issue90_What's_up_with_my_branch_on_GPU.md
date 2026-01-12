2019-06-24: [What's up with my branch on GPU?](https://aschrein.github.io/jekyll/update/2019/06/13/whatsup-with-my-branches-on-gpu.html)

- explains how branching on GPUs is commonly implemented
- explains what divergence is, impact on performance and how to reduce it
- GPUs use an execution mask to hide results from inactive threads
- shows how this looks in GCN ISA and AVX512
