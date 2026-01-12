2021-05-02: [The case of the curiously slow shader](https://raphlinus.github.io/gpu/2021/04/28/slow-shader.html)

- the article presents a walkthrough how the author analyzed the slow shader performance on the GPU of the Pixel 4
- shows how to detect occupancy, get access to the assembly instructions
- ultimatly presents how reading the assembly showed the source of the performance problem, how it connects to shader memory model and how to possibly resolve it
