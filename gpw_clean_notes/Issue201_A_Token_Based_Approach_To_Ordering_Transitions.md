2021-09-17: [A Token Based Approach To Ordering Transitions](https://sakibsaikia.github.io/graphics/2021/09/16/A-Token-Based-Approach-To-Ordering-Transitions.html)

- the author suggests a method D3D12 state transition system for multithreaded command recording
- based around per-resource tokens that use CPU side fences to synchronize access to previous state transitions
