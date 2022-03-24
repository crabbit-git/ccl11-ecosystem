# Testing Recap

**Lesson Duration: 30 minutes**

### Learning Objectives

- Recap testing
- Know how to set up directories for testing
- Know how to write a test

## Recap

So we will be doing `unit testing`. Unit testing is a level of software testing where small individual components of code (often a method) are testing.

We do this by using the built in `unittest` module in Python.

Our unit tests are written in a separate file to our main code and usually saved in a separate directory.

So let's set up our directory structure for the lab.

## Setting up directories and files

```bash
# Terminal

mkdir eco_system
mkdir eco_system/src
mkdir eco_system/tests
touch run_tests.py
```

To run our tests we'll run the `run_tests.py` file. But first let's add some code to this file.

```python

# run_tests.py

import unittest


if __name__ == '__main__':
    unittest.main()

```

Now let's say we have a Bear class that we need to test.

We'll create a file for the class and a file for the test.

```bash
touch src/bear.py
touch tests/bear_test.py
```

Let's add some initial boilerplate code to bear_test.py

```python
# tests/bear_test.py

import unittest
from src.bear import Bear

class TestBear(unittest.TestCase):
    pass
```

And we'll import the `bear_test` file into our `run_tests.py`

```python
# run_tests.py

import unittest
from tests.bear_test import TestBear

if __name__ == '__main__':
    unittest.main()

```

Ok so now we should be good to run our `run_tests.py` file.

```bash
# Terminal

python3 run_tests.py

```

## Setup method

Remember to use a `setUp` method. For example:


```python
# tests/bear_test.py

import unittest
from src.bear import Bear

class TestBear(unittest.TestCase):

    def setUp(self): # NEW
      self.bear = Bear("Yogi", "grizzly") # NEW

```

Let's add our first test. We can expect it to fail. Our job then is to get it to pass!

```python
# tests/bear_test.py

import unittest
from src.bear import Bear

class TestBear(unittest.TestCase):

    def setUp(self):
      self.bear = Bear("Yogi", "grizzly")

    def test_bear_has_name(self): # New
      self.assertEqual("Yogi", self.bear.name) # NEW

```

Run the tests again!

```bash
# Terminal

python3 run_tests.py

```

## Conclusion

That's us set up a basic structure for our project. For clarity, it's conventional to have one test file for each class. This is not a strict rule but it makes sense if it's possible.

NOTE: The unittest.TestCase class has several methods available as well as assertEqual. If you type ```self.``` inside a test method, VSCode will give you a list of methods you can use. Sometimes you might want to check if something is None, for example.
