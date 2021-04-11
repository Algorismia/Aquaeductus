reader=zathura

all: informe

informe: 
	xelatex informe.tex
	xelatex informe.tex

view: informe
	$(reader) informe.pdf

clean:
	rm -rf *.aux *.toc *.log *.out *.lof
