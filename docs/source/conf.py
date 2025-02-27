# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SphinxTest'
copyright = '2023, S. Faas'
author = 'S. Faas'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_thebe']

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

# Thebe configuration
thebe_config = {
    "binderUrl": "https://mybinder.org",  # For testing only
    "repository_url": "https://github.com/meneerfaas/sphinxtest",
    "repository_branch": "main",
    "selector": "div.highlight",
    "codemirror-config": {
        "theme": "eclipse",
        "electricChars": "true",
        "lineNumbers": "true",
        "indentWithTabs": "true",
        "indentUnit": 4,
    }
}
