2021-05-13: [Shader translation benchmark on Dota2/Metal](https://gfx-rs.github.io/2021/05/09/dota2-msl-compilation.html)

- the blog post presents a performance comparison of Naga (rust based shader translation library) vs. SPIRV-Cross in Dota2
- measures CPU time taken for shader translation in Dota2 from SPIRV to MSL (Metal shading language)
- takes around 1ms per shader stage
