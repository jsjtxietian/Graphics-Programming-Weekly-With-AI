2019-09-29: [Strand-based Hair Rendering in Frostbite](http://advances.realtimerendering.com/s2019/hair_presentation_final.pdf)

- the presentation shows the new WIP hair rendering system
- a realtime system that is based on hair stands instead of cards
- strands are rasterized into shadow and deep opacity maps
- for performance reasons, a visibility buffer is written, and a sample deduplication pass is applied
- shading is done in a screen space pass
- shows how the different shading components have been implemented
