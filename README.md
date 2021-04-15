<h1 align="center">
  Aquaeductus assignment
</h1>

## Abstract 🗒️:
Given a set of points (p), a maximum height of an aquaeduct (h)  and a beta and alpha cost variables, gives the minimum cost of the possible aqueduct and if it doesn't exists, prints impossible.

The solution is based on the [principle of optimality of Bellman](https://en.wikipedia.org/wiki/Bellman_equation), which involves dynamic programming. The big oh notation of this algorithm is of O(n^3).

If you would like to know more about how it works, I would totally recommend reading the report of this assignment, which is found on the documentation folder of this repo.

## Project structure 📁:

``` 
├── cpp                 --> cpp code (iterative version)
├── documentation       --> report of the assignment in .pdf and .tex
├── graphic-sampling    --> files for getting the graph data
├── python              --> python code (iterative and recursive version)
├── README.md
└── test                --> test files
```

## Running tests 🏃:

### Python

For python, if you want to run the tests (for the iterative version) and the code analysis tool (for the recursive and iterative version) do:

``` 
    $ make test
```

If you would like to run only the tests:

``` 
    $ make onlytest
```

If you would like to run only the code analysis tool (pylint) without docstring warnings (because the code is self-explanatory without comments):
``` 
    $ make pylint
```

For default, the Makefile uses python as his interpreter. If you would like to change it to other like for example
[pypy3](https://www.pypy.org/) (which runs a lot faster than python3) , you can do it changing the Makefile variable to pypy3.

``` bash
interpreter=pypy3
```

If you want to run the **RECURSIVE** tests, do:
``` 
    $ make recursive
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
