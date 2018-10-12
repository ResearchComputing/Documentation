from recommonmark.parser import CommonMarkParser

project = "University of Colorado Boulder\nResearch Computing"

master_doc = 'index'

source_parsers = {
    '.md': CommonMarkParser,
}

extensions = [
    'sphinx_markdown_tables',
]

source_suffix = ['.rst', '.md']
