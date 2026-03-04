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
   'alpine_total_compute_nodes': '456', 
   'alpine_total_cores': '28,144',

   # Alpine cluster summary substitutions
   'alpine_total_256GB_cpu_nodes': '406',
   'alpine_total_gpu_nodes': '25',
   'alpine_total_hi_mem_cpu_nodes': '24',
   'ucb_alpine_total_nodes': '342',
   'amc_alpine_total_nodes': '37',
   'csu_alpine_total_nodes': '77',

   # Alpine hardware page general substitutions
   'alpine_standard_ram_per_core': '3.8',

   # Alpine hardware page, hardware summary section substitutions
   ## UCB contributions 
   'alpine_ucb_total_128_core_256GB_cpu_nodes': '16',
   'alpine_ucb_total_64_core_256GB_cpu_nodes': '284',
   'alpine_ucb_total_64_core_1TB_cpu_nodes': '8',
   'alpine_ucb_total_48_core_1TB_cpu_nodes': '12',
   'alpine_ucb_total_a100_gpu_nodes': '7',
   'alpine_ucb_total_mi100_gpu_nodes': '7',
   'alpine_ucb_total_gh200_gpu_nodes': '2',
   'alpine_ucb_total_acompile_nodes': '2',
   'alpine_ucb_total_64_core_256GB_cpu_nodes_atesting': '2',
   'alpine_ucb_total_atesting_a100_gpu_nodes': '1',
   'alpine_ucb_total_atesting_mi100_gpu_nodes': '1',
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
   'alpine_total_amilan_nodes': '403',
   'alpine_total_ami100_nodes': '7',
   'alpine_total_aa100_nodes': '11',
   'alpine_total_al40_nodes': '3',
   'alpine_total_amem_nodes': '24',
   'alpine_total_acompile_nodes': '2',
   'alpine_total_atesting_cpu_nodes': '2',
   'alpine_total_atesting_a100_nodes': '1',
   'alpine_total_atesting_mi100_nodes': '1',

   # Alpine Array Jobs
   'alpine_max_number_array_jobs' : '1,000',

   # Petalibrary substitutions
   # Note: the below values currently cannot be used in the tier table 
   # due to limitations in how variables can be integrated
   # into html. Therefore, the variables below are published
   # here for future reference, and to remind us to manually
   # update pl_tier_table.html when these values change.

   "pl_fy26_cu_data_rate_active": "$45",
   "pl_fy26_cu_data_rate_archive": "$25",
   "pl_fy26_cu_data_rate_active_archive": "$70",
   "pl_fy26_cu_data_rate_archive_dr": "$41",
   "pl_fy26_ext_data_rate_active": "$115",
   "pl_fy26_ext_data_rate_archive": "$75",
   "pl_fy26_ext_data_rate_active_archive": "N/A",
   "pl_fy26_ext_data_rate_archive_dr": "N/A",
   "pl_initial_allocation_request_limit_active": "200 T",
   "pl_initial_allocation_request_limit_archive": "200 T",
   "pl_initial_allocation_request_limit_active_archive": "200 T",
   "pl_initial_allocation_request_limit_archive_dr": "200 T"

}

source_suffix = {
    '.txt': 'markdown',
    '.md': 'markdown',
}

html_theme = 'sphinx_book_theme'

myst_heading_anchors=6

html_static_path = ['_static']
html_css_files = ["custom.css"]
templates_path = ['_templates']

html_theme_options = {
   "logo": {
      "image_light": "_static/Research_Computing_black_letters.png",
      "image_dark": "_static/Research_Computing_white_letters.png",
   }, 
   "repository_url": "https://github.com/ResearchComputing/Documentation",
   "use_repository_button": True, 
}

html_sidebars = {
    "**": [
        "navbar-logo.html",
        "sbt-sidebar-announcement.html", 
        "icon-links.html",
        "search-button-field.html",
        "sbt-sidebar-nav.html",
    ]
}

html_context = {
   "default_mode": "dark",
}

copybutton_prompt_text = r'^\$ '
copybutton_prompt_is_regexp = True
