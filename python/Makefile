test := ../test
interpreter=pypy3

test:
	for t in $(test)/*.in; do $(interpreter) aqueducte.py $$t > sortida; diff -q $(test)/`basename $$t .in`.ans sortida; done

clean:
	rm -rf sortida
