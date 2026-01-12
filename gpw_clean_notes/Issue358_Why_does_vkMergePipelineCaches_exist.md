2024-09-19: [Why does vkMergePipelineCaches exist?](https://www.yosoygames.com.ar/wp/2024/09/why-does-vkmergepipelinecaches-exist/)

- the article discusses how Vulkan Pipeline caches operate
- presents how multiple threads creating pipeline create contention and how multiple caches can solve the problem
- additionally discusses which flags are required to create truly independent caches between threads
