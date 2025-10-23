project = "Research Computing\nUniversity of Colorado Boulder"

master_doc = 'index'

extensions = ['myst_parser', 'sphinx_copybutton', 'sphinx.ext.graphviz', 'sphinx_design', 'sphinx.ext.extlinks']
graphviz_output_format = 'svg'

myst_enable_extensions = ["colon_fence", "attrs_inline", "attrs_block", "tasklist", "substitution"]
myst_enable_checkboxes = True

myst_substitutions = {

   # Allocation specific substitutions 
   'trailhead_SUs': '2,000',
   'boulder_ascent_SUs': '350,000', 
   'boulder_ascent_SU_group_limit': '1.4 M', 
   'boulder_peak_SUs': '6,000,000', 
   'rmacc_ascent_SUs': '100,000',

   # Alpine compute total counts substitutions 
   'alpine_total_compute_nodes': '455', 
   'alpine_total_cores': '28,080',

   # Alpine cluster summary substitutions
   'alpine_total_256GB_cpu_nodes': '406',
   'alpine_total_gpu_nodes': '25',
   'alpine_total_hi_mem_cpu_nodes': '24',
   'ucb_alpine_total_nodes': '341',
   'amc_alpine_total_nodes': '37',
   'csu_alpine_total_nodes': '77',

   # Alpine hardware page, hardware summary section substitutions
   ## UCB contributions 
   'alpine_ucb_total_128_core_256GB_cpu_nodes': '16',
   'alpine_ucb_total_64_core_256GB_cpu_nodes': '283',
   'alpine_ucb_total_64_core_1TB_cpu_nodes': '8',
   'alpine_ucb_total_48_core_1TB_cpu_nodes': '12',
   'alpine_ucb_total_a100_gpu_nodes': '7',
   'alpine_ucb_total_mi100_gpu_nodes': '7',
   'alpine_ucb_total_gh200_gpu_nodes': '2',
   'alpine_ucb_total_acompile_nodes': '2',
   'alpine_ucb_total_64_core_256GB_cpu_nodes_atesting': '4',
   'alpine_ucb_total_atesting_a100_gpu_nodes': '1',
   'alpine_ucb_total_atesting_mi100_gpu_nodes': '1',
   'alpine_ucb_total_dtn_nodes': '4',
   ## AMC contributions
   'alpine_amc_total_64_core_256GB_cpu_nodes': '26', 
   'alpine_amc_total_64_core_1TB_cpu_nodes': '2',  
   'alpine_amc_total_128_core_2TB_cpu_nodes': '2',  
   'alpine_amc_total_a100_gpu_nodes': '4',  
   'alpine_amc_total_l40_gpu_nodes': '3',
   ## CSU contributions
   'alpine_csu_total_48_core_256GB_cpu_nodes': '28',
   'alpine_csu_total_32_core_256GB_cpu_nodes': '49',

   # Alpine hardware page, partition section substitutions
   'alpine_total_amilan_nodes': '386',
   'alpine_total_amilan128c_nodes': '16',
   'alpine_total_ami100_nodes': '7',
   'alpine_total_aa100_nodes': '11',
   'alpine_total_al40_nodes': '3',
   'alpine_total_amem_nodes': '24',
   'alpine_total_csu_nodes': '77',
   'alpine_total_amc_nodes': '37',
   'alpine_total_acompile_nodes': '2',
   'alpine_total_atesting_cpu_nodes': '4',
   'alpine_total_atesting_a100_nodes': '1',
   'alpine_total_atesting_mi100_nodes': '1',
   'alpine_total_dtn_nodes': '4',
   # Alpine Array Jobs
   'alpine_max_number_array_jobs' : '1,000'
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

copybutton_prompt_text = r'^\$ '
copybutton_prompt_is_regexp = True
