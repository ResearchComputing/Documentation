project = "Research Computing\nUniversity of Colorado Boulder"

master_doc = 'index'

extensions = ['myst_parser', 'sphinx_copybutton', 'sphinx_tabs.tabs']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

html_theme = 'sphinx_book_theme'

myst_heading_anchors=6

html_static_path = ['_static']
html_css_files = ["custom.css"]

html_theme_options = {
   "logo": {
      "image_light": "_static/Research_Computing_black_letters.png",
      "image_dark": "_static/Research_Computing_white_letters.png",
   }, 
   "repository_url": "https://github.com/ResearchComputing/Documentation",
   "use_repository_button": True,
}