from lxml import etree
import os 

def remove_xlink_title_replace(svg_file):
    # Load SVG file
    tree = etree.parse(svg_file)
    root = tree.getroot()

    # Get all namespaces
    namespaces = root.nsmap

    ns = {}

    # put namespaces into a different form that is easier to query 
    for prefix, uri in namespaces.items():
        if prefix == None:
            ns['svg'] = {'svg': uri}
        else:
            ns[prefix] = {prefix: uri}

    temp = ns['xlink']['xlink']
    
    # Remove xlink:title attributes
    for elem in root.xpath('//@xlink:title', namespaces=ns['xlink']):
        elem.getparent().attrib.pop("{" + temp + "}title")

    # Remove all <title> tags
    for title in root.xpath('//svg:title', namespaces=ns['svg']):
        title.getparent().remove(title)

    # Save modified SVG
    tree.write(svg_file)

# specify directory path where SVGs are located (relative to makefile)
svg_dir_path="./igraphviz_flowcharts/generated_images"

for filename in os.listdir(svg_dir_path):
    if filename.endswith('.svg'):
        file_path = os.path.join(svg_dir_path, filename)

        remove_xlink_title_replace(file_path)

