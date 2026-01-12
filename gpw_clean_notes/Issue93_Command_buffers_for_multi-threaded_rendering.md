2019-07-16: [Command buffers for multi-threaded rendering](http://alinloghin.com/articles/command_buffer.html)

- explains a renderer architecture that separates command generation from execution
- commands have an associated sort key that is used to determine the execution order
- shows how to handle materials, resource updates and some advice for debugging such a system
