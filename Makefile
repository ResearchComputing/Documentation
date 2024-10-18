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
	dot -Tsvg $(IGRAPH_PATH)/dot_files/getting_started_hpc_flowchart.dot > $(IGRAPH_PATH)/generated_images/getting_started_hpc_flowchart.svg
	dot -Tsvg $(IGRAPH_PATH)/dot_files/getting_started_cloud_flowchart.dot > $(IGRAPH_PATH)/generated_images/getting_started_cloud_flowchart.svg
	python $(IGRAPH_PATH)/remove_tooltip.py
	$(SPHINXBUILD) -b html -d $(BUILDDIR)/doctrees -D language=en $(SOURCEDIR) $(BUILDDIR)/html
