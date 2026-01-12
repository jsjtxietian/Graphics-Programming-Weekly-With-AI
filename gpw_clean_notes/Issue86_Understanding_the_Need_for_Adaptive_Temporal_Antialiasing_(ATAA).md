2019-05-24: [Understanding the Need for Adaptive Temporal Antialiasing (ATAA)](https://news.developer.nvidia.com/understanding-the-need-for-adaptive-temporal-antialiasing/)

- proposed antialiasing technique combines rasterization with ray tracing
- uses ray tracing to collect extra samples when information from previous frames is not available
- run FXAA on the fast moving parts on the edges of the screen to reduce cost
