# What's this then?

It's the first time I ever wrote unit tests. Yes, ever. BE GENTLE.

# Right but like, what?

Specifically, it's an exercise (referred to as "bear_river_fish" internally) issued as part of the Python coursework for a software development course. The point was to practice writing not just functions and classes, but also unit tests to check functionality. Ideally, you'd write the functions to the tests to an extent, rather than writing functions blindly and then trying to wrangle them into tests, with the idea being that this should produce more efficient code.

The files `setup.md` and `task.md` are all that were provided to us at the start of this particular exercise. The former gives a nudge in the right direction by getting things started off, and the actual objectives are laid out (as usual) in the latter.

There is no frontend here. It's just a bunch of classes with functions inside them which are tested by corresponding unit test modules in a separate package. The main classes are in `src` and the tests are in `tests`; to run the tests, you just execute `run_tests.py` from a terminal. That's about it.

The model was an "ecosystem" (a term which arguably implies significantly greater complexity than the actual task at hand) made up of a river containing fish which are consumed by bears. Each of those three main elements is defined by a class module in the `src` package.

I tried to hold myself back from getting too carried away with any daft experimental nonsense on this occasion, mostly due to limited time, and have mostly restricted my tomfoolery to giving things stupid names that entertain me. Count yer blessings.