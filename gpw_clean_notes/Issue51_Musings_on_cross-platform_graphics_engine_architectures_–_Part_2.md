2018-08-09: [Musings on cross-platform graphics engine architectures – Part 2](http://www.gijskaerts.com/wordpress/?p=112)

- breaks down the engine into two separate related concepts, Resource and Command management
- discusses how to interact with resources
- introduces the idea of state scopes to prevent state leaking
- commands are recorded into engine specific command buffers that are later converted into the API specific format
