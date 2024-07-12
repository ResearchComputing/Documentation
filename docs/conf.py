# from recommonmark.parser import CommonMarkParser

project = "Research Computing\nUniversity of Colorado Boulder"

master_doc = 'index'

# source_parsers = {
#     '.md': CommonMarkParser,
# }

# extensions = [
#     'sphinx_markdown_tables'
# ]

extensions = ['myst_parser']

# source_suffix = ['.rst', '.md']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

html_theme = 'sphinx_book_theme'

html_static_path = ['_static']
