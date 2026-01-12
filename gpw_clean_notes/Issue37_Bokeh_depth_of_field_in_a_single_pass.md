2018-05-06: [Bokeh depth of field in a single pass](http://tuxedolabs.blogspot.ca/2018/05/bokeh-depth-of-field-in-single-pass.html?m=1)

- shows the steps leading up the final implementation
- uses a fixed weight for all contributing samples. If sample doesn't contribute, blend in the current average color instead
- clamping sample size when sample is further away then the center sample. This makes sure out of focus background do not blur into in-focus foreground objects
