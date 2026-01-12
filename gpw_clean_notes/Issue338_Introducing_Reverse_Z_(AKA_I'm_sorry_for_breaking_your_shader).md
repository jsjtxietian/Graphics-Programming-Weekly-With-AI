2024-05-05: [Introducing Reverse Z (AKA I'm sorry for breaking your shader)](https://godotengine.org/article/introducing-reverse-z)

- the Godot engine is switching the definition of near/far plane, with the near plane now mapping to a depth of 1 and the far plane to 0
- this post explains common patterns that are affected by this change
- additionally provides links to explain why this new mapping allowed significantly improved depth buffer precision
