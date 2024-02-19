# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Interview Prepare'
copyright = '2024, chentzj'
author = 'chentzj'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_theme_options = {

    # Set the name of the project to appear in the navigation.
    'nav_title': 'Interview Prepare',
    'body_max_width': '100%',

    # Set you GA account ID to enable tracking
    #'google_analytics_account': 'UA-136029994-1',

    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    #'base_url': 'https://yolov5-optimization.readthedocs.io/en/latest/',

    # Set the color and the accent color
    # Remember to update static/css/material_custom.css when this is updated.
    # Set those colors in layout.html.
}

html_static_path = ['_static']

# -- Options for EPUB output
epub_show_urls = 'footnote'
