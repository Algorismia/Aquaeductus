test := ../test
interpreter=pypy3

all: test

# pylint without docstring warnings (the code is self-explanatory without comment)
pylint:
	echo "pylint result:" 
	pylint --disable=missing-docstring aqueducte.py

testonly:
	for t in $(test)/*.in; do $(interpreter) aqueducte.py $$t > sortida; diff -q $(test)/`basename $$t .in`.ans sortida; done

test: testonly pylint

clean:
	rm -rf sortida
