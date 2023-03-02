# Makefile for Sphinx documentation

# You can set these variables from the command line.
SPHINXBUILD   = python -m sphinx -T -E
BUILDDIR      = build
SOURCEDIR     = docs

.PHONY: default clean view html

default: html

all: html

view:
	open build/html/index.html

clean:
	-rm -r $(BUILDDIR)

html:
	$(SPHINXBUILD) -b html -d $(BUILDDIR)/doctrees -D language=en $(SOURCEDIR) $(BUILDDIR)/html
