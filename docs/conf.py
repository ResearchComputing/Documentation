project = "Research Computing\nUniversity of Colorado Boulder"

master_doc = 'index'

extensions = ['myst_parser', 'sphinx_copybutton', 'sphinx.ext.graphviz', 'sphinx_design', 'sphinx.ext.extlinks']
graphviz_output_format = 'svg'

myst_enable_extensions = ["colon_fence", "attrs_inline", "attrs_block", "tasklist", "substitution"]
myst_enable_checkboxes = True

myst_substitutions = {
    'trailhead_SUs': '2,000',
    'boulder_ascent_SUs': '350,000', 
    'boulder_ascent_SU_group_limit': '1.4 M', 
    'boulder_peak_SUs': '6,000,000', 
    'rmacc_ascent_SUs': '100,000',
    'alpine_total_compute_nodes': '455', 
    'alpine_total_cores': '28,080',
    'alpine_total_cpu_nodes': '402',
    'alpine_total_128_core_cpu_nodes': '16',
    'alpine_total_64_core_cpu_nodes': '309',
    'alpine_total_48_core_cpu_nodes': '28',
    'alpine_total_32_core_cpu_nodes': '49',
    'alpine_total_mi100_gpu_nodes': '8',
    'alpine_total_a100_gpu_nodes': '12',
    'alpine_total_l40_gpu_nodes': '3',
    'alpine_total_himem_1TB_cpu_nodes': '22',
    'alpine_total_himem_2TB_cpu_nodes': '2',
    'alpine_csu_total_compute_nodes': '77',
    'alpine_csu_total_48_core_compute_nodes': '28',
    'alpine_csu_total_32_core_compute_nodes': '49',
    'alpine_amc_total_reg_64_core_nodes': '26', 
    'alpine_amc_total_himem_1TB_cpu_nodes': '2',  
    'alpine_amc_total_himem_2TB_cpu_nodes': '2',  
    'alpine_amc_total_a100_gpu_nodes': '4',  
    'alpine_amc_total_l40_gpu_nodes': '2'
}

source_suffix = {
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

html_context = {
   "default_mode": "dark"
}