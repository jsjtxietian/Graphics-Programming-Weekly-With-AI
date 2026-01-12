2019-01-21: [Volume Rendering with WebGL](https://www.willusher.io/webgl/2019/01/13/volume-rendering-with-webgl)

- implementation of ray marching
- renders the back faces of the bounding volume to determine on which pixels raymarching needs to be done
- simplified absorption model, ignoring the scattering effects
- the vertex shader is used to calculate the ray direction and pass it to the pixel-shader
- lookup texture is used to color to the greyscale information from the 3D volume texture
