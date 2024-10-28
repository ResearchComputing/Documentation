import re
import os 
import pathlib


def check_tab_reference(md_path):

    # Load the Markdown file
    with open(md_path, 'r') as file:
        content = file.read()

    # Regular expression to grab all items that are Markdown syntax for references 
    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)

    # For each cross-reference identified, ensure that the tab references actually exist in the specified file
    for link_text, link in links:
        
        if "?tabset-" in link:

            print(f"Checking the following reference from {md_path}")
            print(f'Text: {link_text}, URL: {link} \n')

            # remove html in reference name and use md instead 
            link = link.replace('html', 'md')

            # split apart reference to get individual parts
            link_parts = re.split(r'[?=#]', link)

            # assign appropriate parts so they can be checked 
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

                checked_file = os.path.join(md_file_path.parent, path)

                # if there is a path in the reference, open the file
                with open(checked_file , 'r') as file:
                    temp_content = file.read()

                # check that tabset_name, tab_name, and tabsec_name all exist in file
                include_check = all(s in temp_content for s in look_for_list)
            else:

                checked_file = md_path

                # check that tabset_name, tab_name, and tabsec_name all exist in file
                include_check = all(s in content for s in look_for_list)

            # throw an error if the tab references do not exist 
            if not include_check:
                raise RuntimeError(f"One of the following tab references DO NOT EXIST in {checked_file}: {look_for_list}")

def find_markdown_files(dir):
    return list(pathlib.Path(dir).rglob('*.md'))

# get all markdown files in docs and check them for correct tab references 
current_directory = pathlib.Path.cwd()
markdown_files = find_markdown_files(current_directory)

for md_file_path in markdown_files:
    check_tab_reference(md_file_path)