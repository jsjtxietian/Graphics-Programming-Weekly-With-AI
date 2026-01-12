2018-08-27: [Real-Time rendering’s next frontier: Adopting lessons from offline ray tracing to real-time ray tracing for practical pipelines](http://advances.realtimerendering.com/s2018/Pharr%20-%20Advances%20in%20RTR%20-%20Real-time%20Ray%20Tracing.pdf)

- start tracing rays where rasterizer has shortcomings
- explains how to tune Monte Carlo estimators to converge quicker by minimizing variance using different AO and spherical lights as examples
- shows the weakness of uniform random numbers and provides techniques to generate better distributions
- variance-driven sampling focus taking more samples where variance is high
