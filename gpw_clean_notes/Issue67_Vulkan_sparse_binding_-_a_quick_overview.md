2018-12-17: [Vulkan sparse binding - a quick overview](http://asawicki.info/news_1698_vulkan_sparse_binding_-_a_quick_overview.html)

- explains sparse binding and residency
- sparse binding lifts the requirement that resource memory needs to be fully continuous in memory. Instead, memory is managed with pages that can be mapped at non-continues offsets
- sparse residency lifts the requirement that the complete resource needs to mapped. For example, only parts of a texture atlas could be mapped
