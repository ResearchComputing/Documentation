# Makefile for Sphinx documentation

# You can set these variables from the command line.
SPHINXBUILD   = python -m sphinx -T -E
BUILDDIR      = build
SOURCEDIR     = docs
GRAPH_PATH   = ./graphviz_flowcharts
.PHONY: default clean view html

default: html

all: html

view:
	open build/html/index.html

clean:
	-rm -r $(BUILDDIR)

html:
	source "${GRAPH_PATH}/create_svg.sh"
	python $(GRAPH_PATH)/remove_tooltip.py
	python custom_checks/check_dot_ref.py
	python custom_checks/check_tab_ref.py 
	$(SPHINXBUILD) -b html -d $(BUILDDIR)/doctrees -D language=en $(SOURCEDIR) $(BUILDDIR)/html
