2019-11-04: [Coming to DirectX 12— Sampler Feedback: some useful once-hidden data, unlocked](https://devblogs.microsoft.com/directx/coming-to-directx-12-sampler-feedback-some-useful-once-hidden-data-unlocked/)

- the article presents the use-case of the streaming system and texture space shading
- sampler feedback is a hardware feature that allows D3D12 shaders to write to a texture which MIPS has been accessed
- FeedbackTexture2D is a new HLSL resource type to express it
- the granularity of the feedback map is user-controlled
