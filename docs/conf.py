from recommonmark.parser import CommonMarkParser

project = "CURC Documentation"

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']
