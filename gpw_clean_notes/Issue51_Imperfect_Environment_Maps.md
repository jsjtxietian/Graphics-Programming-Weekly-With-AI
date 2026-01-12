2018-08-12: [Imperfect Environment Maps](https://www.gamedev.net/blogs/entry/2265286-imperfect-environment-maps/)

- using ideas from imperfect shadow map point-cloud rendering to implement reflections
- generates a point cloud around the track
- screen space pixels that are close to points of the point cloud transfer their color onto the points
- the point cloud is then projected onto a sphere around the car and used as an environment map to add reflections on the cars
