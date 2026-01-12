2018-12-03: [glsl-reduce](https://github.com/google/graphicsfuzz/blob/master/docs/glsl-reduce-walkthrough.md)

- the walkthrough explains how to use GLSL-reduce to simplify a GLSL shader and preserve certain conditions such as a crash or invalid output
- this is achieved with an interestingness test script
- the script expresses what is considered to be interesting, such as specific compiler crash, high memory usage, long compile time, etc
- presents the problem of bug slippage, this happens when a reduced shader generates a problem, but it's not the same problem as in the original shader
