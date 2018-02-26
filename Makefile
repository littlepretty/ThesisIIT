PDFLATEX=pdflatex
LATEX=latex
BIBTEX=bibtex
DVI2PDF=dvipdf
PS2PDF=ps2pdf
UNAME:=$(shell uname -s)
ifeq ($(UNAME),Linux)
	VIEWER=xdg-open
endif
ifeq ($(UNAME), Darwin)
	VIEWER=open -a Preview
endif

NAME=main

.PHONY: clean, view

conf:
	$(LATEX)    $(NAME).tex
	$(BIBTEX)   $(NAME).aux
	$(LATEX)    $(NAME).tex
	$(LATEX)    $(NAME).tex
	$(DVI2PDF)  $(NAME).dvi

view: conf
	$(VIEWER) $(NAME).pdf
	rm *.log *.aux *.blg *.bbl *.lof *.lot *.dvi *.toc
	#rm *-eps-converted-to.pdf
	#pdffonts main.pdf

clean:
	rm *.log *.aux *.dvi *.out *.blg *.bbl *.ps *.bak
