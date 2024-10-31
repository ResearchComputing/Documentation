# This script looks through all ".dot" files in "igraphviz_flowcharts/dot_files"
# and uses igraphviz's dot command to generate an SVG of the dot file that 
# can be used within the documentation. 

# Assign arguments to variables
DIRECTORY="./igraphviz_flowcharts/dot_files"
EXTENSION="dot"

# Find and run the command on each file with the specified extension
find "$DIRECTORY" -type f -name "*.$EXTENSION" | while read -r file_path; do

    # get file name so we can generate SVG
    file_name=$(basename "$file_path" .dot) 
    echo "Processing file: $file_path"
    echo "$file_name"

    dot -Tsvg $file_path > ./igraphviz_flowcharts/generated_images/${file_name}.svg
done