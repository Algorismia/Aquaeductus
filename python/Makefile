test := ../test
interpreter=python3

all: test

# pylint without docstring warnings (the code is self-explanatory without comment)
pylint:
	pylint --disable=missing-docstring aqueducte.py
	pylint --disable=missing-docstring aqueducte_recursive.py

iterative:
	for t in $(test)/*.in; do $(interpreter) aqueducte.py $$t > sortida; diff -q -w $(test)/`basename $$t .in`.ans sortida; done

recursive:
	for t in $(test)/*.in; do $(interpreter) aqueducte_recursive.py $$t > sortida; diff -q -w $(test)/`basename $$t .in`.ans sortida; done

test: iterative pylint

clean:
	rm -rf sortida
