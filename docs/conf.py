from recommonmark.parser import CommonMarkParser

project = "Research Computing\nUniversity of Colorado Boulder"

master_doc = 'index'

source_parsers = {
    '.md': CommonMarkParser,
}

extensions = [
    'sphinx_markdown_tables',
]

source_suffix = ['.rst', '.md']
