2019-03-08: [stable filtering  —  part 1](https://caseymuratori.com/blog_0035)

- explanation of half-pel filters
- shows properties of different filters common in video compression and how they perform when applied multiple times
- common filters are "unstable" when executed multiple times
- the feedback loop causes the results to be oversharpened until the results become unrecognizable
- presents a filter that does not have a feedback loop problem and converges to a slightly softened but stable result
