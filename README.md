<h1 align="center">
  Aquaeductus assignment
</h1>

## Abstract 🗒️:
Given a set of points (p), a maximum height of an aquaeduct (h)  and a beta and alpha cost variables, gives the minimum cost of the possible aqueduct and if it doesn't exists, prints impossible.

The solution is based on the [principle of optimality of Bellman](https://en.wikipedia.org/wiki/Bellman_equation), which involves dynamic programming. The Big O notation of this algorithm is of O(n^3).

If you would like to know more about how it works, I would totally recommend reading the report of this assignment, which is found in documentation/informe.pdf. Emphasize that the report is written in Catalan,
although it has enough visual resources to understand how everything was done.

## Project structure 📁:

``` 
├── cpp                 --> cpp code (iterative version)
├── documentation       --> report of the assignment in .pdf and .tex (just in case you want to contribute or read how some resources were done)
├── python              --> python code (iterative and recursive version)
├── README.md
└── test                --> test files
```

## Running tests 🏃:

### Python

If you want to run the tests (for the iterative version) and the code analysis tool (for the recursive and iterative version) do:

``` 
    $ make test
```

If you would like to run only the test of the iterative version:

``` 
    $ make iterative
```

If you want to run the **RECURSIVE** tests, do:
``` 
    $ make recursive
```

If you would like to run just the code analysis tool (pylint) without docstring warnings (because the code is self-explanatory without comments):
``` 
    $ make pylint
```

By default, the Makefile uses python as his interpreter. If you would like to change it to other like for example
[pypy3](https://www.pypy.org/) (which runs a lot faster than python3) , you can do it changing the Makefile variable to pypy3.

``` bash
interpreter=pypy3
```

### C++

For compiling the .cpp file with all the optimizations and warning checkers:

``` 
    $ make
```

For compiling and running the tests:

``` 
    $ make test
```
