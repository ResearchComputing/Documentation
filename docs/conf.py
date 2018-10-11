from recommonmark.parser import CommonMarkParser

project = "University of Colorado Boulder\nResearch Computing"

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']
