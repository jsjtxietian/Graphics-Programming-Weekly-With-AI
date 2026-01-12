2022-03-01: [Vulkan SC: Overview - and how it is different from the Vulkan you already know](https://www.khronos.org/blog/vulkan-sc-overview)

- the article presents Vulkan for Safety-Critical applications
- presents how Vulkan SC 1.0 differes from Vulkan 1.2
- main differences are pipeline lading and more rigid memory allocation requirements
- all pipelines need to be compiled ahead of time into caches. No runtime compilation is allowed
- provides tools to inspect the compiler cache outputs
