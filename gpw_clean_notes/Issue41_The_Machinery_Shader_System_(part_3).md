2018-06-06: [The Machinery Shader System (part 3)](http://ourmachinery.com/post/the-machinery-shader-system-part-3/)

- shader authors can define variations of shaders with a number of systems
- each system can inject code/resources/constants into the shader
- a material allows specifications of which shaders belong together, which systems they use and allows to insert command at the correct time in the Frame
- all of the resulting shaders get a shared resource binder and constant buffer to reduce
