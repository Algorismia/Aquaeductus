CC=g++
CFLAGS=-pedantic -Wall  -O3
test := ../test

all: aqueducte

aqueducte: aqueducte.cpp
	$(CC) $(CFLAGS) -o $@ $^

test: aqueducte
	for t in $(test)/*.in; do ./aqueducte $$t > sortida; diff -q $(test)/`basename $$t .in`.ans sortida; done

graphic:
	for x in $(ls ../graphic-sampling/*.in | sort -t '-' -n -k4); do time ./aqueducte $x >> temps ; echo $x ; done

clean:
	rm -rf aqueducte sortida
