2021-06-21: [VK_EXT_multi_draw released for Vulkan](https://rg3.name/202106210630.html)

- a new Vulkan extension that adds vkCmdDrawMultiEXT vkCmdDrawMultiIndexedEXT
- these allow applications to provide an array of draw call arguments in CPU visible memory
- for uses cases where applications would call vkCmdDraw multiple times in a loop without changing state
- tests indicate that a doubling of draw call processing rate can be observed
