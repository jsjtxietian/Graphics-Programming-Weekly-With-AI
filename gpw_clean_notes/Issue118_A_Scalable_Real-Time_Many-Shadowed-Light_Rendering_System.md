Unknown Date: [A Scalable Real-Time Many-Shadowed-Light Rendering System](https://drive.google.com/file/d/19EHLJAfqQECjRRShHyS3mHrg4XFxpCOx/view)

- Siggraph presentation showcasing a shadow system that enables thousands of shadowed-lights in large environments
- uses a fixed size shadow map pool, each light allocates it's the target size
- splits dynamic and static shadows, using conservative filtering for the highly sparse dynamic shadows
- presents several techniques for compression, filtering and an overview of performance
