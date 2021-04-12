CC=g++
CFLAGS=-pedantic -Wall  -O3
test := ../test

all: aqueducte

aqueducte: aqueducte.cpp
	$(CC) $(CFLAGS) -o $@ $^

test: aqueducte
	for t in $(test)/*.in; do ./aqueducte $$t > sortida; diff -q $(test)/`basename $$t .in`.ans sortida; done

clean:
	rm -rf aqueducte sortida
