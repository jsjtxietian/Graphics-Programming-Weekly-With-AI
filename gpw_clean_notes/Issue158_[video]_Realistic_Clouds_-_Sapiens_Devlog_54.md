2020: [[video] Realistic Clouds - Sapiens Devlog 54](https://www.youtube.com/watch?v=M-0lr6HzjZ4&feature=youtu.be)

- the dev vlog explains how the 2D billboard based clouds are implemented
- cloud volumes are generated in Blender, directional light information is baked into textures using single color lights along the principal coordinate system axis
- these directions are blended at runtime to integrate into the in-game PBR lighting system
