# Now you can look for references in the HTML or by analyzing the Markdown directly
# For example, to find all links
import re

md_file_path = "./docs/access/logging-in.md"

# Load the Markdown file
with open(md_file_path, 'r') as file:
    content = file.read()

# Regular expression to find all links in the Markdown
links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)

# Extracting references and printing them
for link_text, link in links:
    
    if "?tabset-" in link:

        print(f'Text: {link_text}, URL: {link}')

        link_parts = re.split(r'[?=#]', link)

        if "tabset" not in link_parts[0]:
            path = link_parts[0]
            tabset_name = link_parts[1]
            tab_name = link_parts[2]
            tabsec_name = link_parts[3]
        else:
            path = None
            tabset_name = link_parts[0]
            tab_name = link_parts[1]
            tabsec_name = link_parts[2]

        # list of items to look for in file
        look_for_list = [":sync-group: " + tabset_name, ":sync: " + tab_name, "(" + tabsec_name + ")="]


        if path:
            with open(md_file_path + path , 'r') as file:
                temp_content = file.read()

            # check that tabset_name, tab_name, and tabsec_name all exist in file
            include_check = all(s in temp_content for s in look_for_list)
        else:

            # check that tabset_name, tab_name, and tabsec_name all exist in file
            include_check = all(s in content for s in look_for_list)

        if include_check:
            print("They exist!")
        else:
            print(f"One of the following tab references DO NOT EXIST in file: {look_for_list}")
