# Adding a flowchart (graph) to documentation 

Although there exists a Graphviz extension for Sphinx, it is not adequate. For example, it does not allow 
you to easily modify the background color of the graphs or make them transparent. Additionally, removing 
built-in functionality like tooltips is not possible. To make these flowcharts as customizable as possible, 
we build all flowcharts using `dot`, the main software used for standard Graphviz graphs. The software `dot`
will then generate an SVG image that is highly customizable. The major drawback to this is that we have to 
create these flowcharts according to a specific structure. Below we provide key items that must be completed 
when integrating a flowchart into the documentation. 

1. All flowcharts (graphs) should be created from a `.dot` file. For more information on creating `.dot` files, 
please see [Graphviz's documentation](https://graphviz.org/doc/info/lang.html). 

2. All `.dot` files must be put in the path `graphviz_flowcharts/dot_files` and must have an extension of `.dot`.
    - This is incredibly important because there are automatic routines that will generate an SVG for you and put it 
    in the directory `graphviz_flowcharts/generated_images`.

3. To reference a flowchart you have created within the documentation, you should point to the file under 
`graphviz_flowcharts/generated_images` (using a relative path) and import it as a raw file using rst. For example, 
in `docs/getting_started/navigating_docs.md` we reference the HPC flowchart as follows: 
````
```{eval-rst}
.. raw:: html
    :file: ../../graphviz_flowcharts/generated_images/getting_started_hpc_flowchart.svg
```
````

4. You can make graph nodes clickable and once clicked, navigate to a page. However, this must be in a specific format. 
For example, to create a node with label `CURC Policies` that opens a new page that links to our internal documentation, you 
would add a node `policies` with the following format. 
```
policies [label="CURC Policies", href="../additional-resources/policies.html", target="_blank", id="clickable"];
```
    - Note that the provided `href` MUST BE a relative path from the file you are referencing the SVG from AND you must 
    use `.html` NOT `.md`.
    - The `href` must be in this style so that our custom check can ensure that a reference exists. 

5. So that styling of the flowcharts is consistent with all other documentation, we suggest the following be included in 
your dot file:
```
bgcolor="transparent";
ranksep="0.5 equally";
graph [id="doc-flowchart"];
node [fontname="Verdana", fontsize="12", color="#CFB87C", style="filled", fillcolor="#121212", penwidth="2", fontcolor="white"];
edge [color="#CFB87C", fillcolor="#121212", penwidth="1.5"];
```