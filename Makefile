# Makefile for Sphinx documentation

# You can set these variables from the command line.
SPHINXBUILD   = python -m sphinx -T -E
BUILDDIR      = build
SOURCEDIR     = docs
IGRAPH_PATH   = ./igraphviz_flowcharts
.PHONY: default clean view html

default: html

all: html

view:
	open build/html/index.html

clean:
	-rm -r $(BUILDDIR)

html:
	source "${IGRAPH_PATH}/create_svg.sh"
	python $(IGRAPH_PATH)/remove_tooltip.py
	python check_tab_ref.py 
	$(SPHINXBUILD) -b html -d $(BUILDDIR)/doctrees -D language=en $(SOURCEDIR) $(BUILDDIR)/html
