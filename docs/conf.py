# For a full list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

project = 'cnest'
copyright = '2022, E. Castedo Ellerman'
author = 'E. Castedo Ellerman'

extensions = [
    'myst_parser'
]

templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

