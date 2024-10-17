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
	dot -Tsvg igraphviz_flowcharts/dot_files/getting_started_hpc_flowchart.dot > igraphviz_flowcharts/generated_images/getting_started_hpc_flowchart.svg
	python ./igraphviz_flowcharts/remove_tooltip.py
	$(SPHINXBUILD) -b html -d $(BUILDDIR)/doctrees -D language=en $(SOURCEDIR) $(BUILDDIR)/html
