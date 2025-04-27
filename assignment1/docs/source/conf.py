# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Cogar Autonomous waiters in a sushi restaurant'
# copyright = '''2025
#                Hafiz Abdul Hayee  
#                Remi Gondoub Waoga Zongo 
#                Fabio Tarditi'''
author = '''Hafiz Abdul Hayee  
            Remi Gondoub Waoga Zongo 
            Fabio Tarditi'''

group_name = 'M'
Topic= 'Tpoic 2'

release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinxcontrib.ros']

templates_path = ['_templates']
exclude_patterns = []

language = 'English'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']







import os
import sys
sys.path.insert(0, os.path.abspath('../../scripts'))

extensions = [
    
]

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']