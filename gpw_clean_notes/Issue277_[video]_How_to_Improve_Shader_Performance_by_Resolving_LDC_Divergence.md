2023: [[video] How to Improve Shader Performance by Resolving LDC Divergence](https://www.youtube.com/watch?v=HSsPJ4qK6AU)

- the video discusses the problem of non-uniform constant loads within a single wrap
- shows how to use Nvidia NSight to identify the problem
- discusses in detail how to correlate counters, latency, and instruction traces
- using Structured Buffers instead of Constant Buffers will be able to resolve the problem once identified
