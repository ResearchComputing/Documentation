# Adding a flowchart (graph) to documentation 

Although there exists an Graphviz extension for Sphinx, it is not adequate. For example, it does not allow 
you to easily modify the background color of the graphs or make them transparent. Additionally, removing 
built-in functionality like tooltips is not possible. To make these flowcharts as customizable as possible, 
we build all flowcharts using `dot`, the main software used for standard Graphviz graphs. The software `dot`
will then generate an SVG image that is highly customizable. The major drawback to this is that we have to 
create these flowcharts according to a specific structure. Below we provide key items that must be completed 
when integrating a flowchart into the documentation. 

1. All flowcharts (graphs) should be created from a `.dot` file. For more information on creating `.dot` files, 
please see [Graphviz's documentation](https://graphviz.org/doc/info/lang.html). 

2. All `.dot` files must be put in the path `.i`