2018-05-21: [Game Math: Swing-Twist Interpolation (…Sterp?)](http://allenchou.net/2018/05/game-math-swing-twist-interpolation-sterp/)

- slerp between two orientations takes the shortest path on a 4D hypersphere
- author wants the shortest arc in 3D instead
- decomposes rotation into swing and twist operations
- these are interpolated independently and concatenated to form the final rotation
