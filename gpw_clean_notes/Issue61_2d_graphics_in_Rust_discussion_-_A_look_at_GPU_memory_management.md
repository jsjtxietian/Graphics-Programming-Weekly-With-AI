2018-10-31: [2d graphics in Rust discussion - A look at GPU memory management](https://nical.github.io/posts/rust-2d-graphics-02.html)

- discusses considerations when designing memory components for use with gfx-hal (rust graphics API abstraction)
- proposes not to use a general purpose allocator but instead to implement simple allocator components and combine them into context-aware allocators on a higher level
