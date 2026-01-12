2022-02-11: [A Shader Trick](http://the-witness.net/news/2022/02/a-shader-trick/)

- the article discusses a problem with effects caused by loss of floating-point precision when game-time is growing
- presents a method to reset periodic timers cleanly and still allow for continuous motion
- the suggested solution uses integer multipliers with required precision to make resetting motions natural from an effect tweaking perspective
