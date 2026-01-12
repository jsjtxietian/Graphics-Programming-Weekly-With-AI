2018-08-27: [Material Advances in Call of Duty: WWII](http://advances.realtimerendering.com/s2018/MaterialAdvancesInWWII.pptx)

- normal and gloss mipmapping
- using a shortened normals technique
- normals are shortened based on the glossiness
- how to combine different textures to add detail to a base texture
- material surface occlusion
- reformulation of Ambient Occlusion that adds indirect lighting in the occluded parts of the material
- adds micro-shadowing from material occlusion into the direct-lighting component
- indirect specular occlusion, using 3D Environment BrdfLut, 3rd dimension is cone angle
- multi-scattering diffuse BRDF utilizing an approximation stored in a 2D LUT
