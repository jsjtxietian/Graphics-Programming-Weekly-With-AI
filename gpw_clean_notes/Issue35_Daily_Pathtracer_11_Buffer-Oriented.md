2018-04-22: [Daily Pathtracer 11: Buffer-Oriented](http://aras-p.info/blog/2018/04/19/Daily-Pathtracer-11-Buffer-Oriented/)

- current approach recursively processes a single ray until it terminates
- new approach calculates each step for all rays in seperate passes
- memory read seems to be limiting factor, shows a few optimizations for that
