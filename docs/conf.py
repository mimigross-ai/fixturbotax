import os
import sys

# Path setup
sys.path.insert(0, os.path.abspath('.'))

# Project information
project = 'Fix Turbotax'
author = 'Mark Lane'
release = '1.0'

# General configuration
extensions = []

templates_path = ['_templates']
exclude_patterns = []

# HTML output
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# ✅ Bing Webmaster Verification (WORKING METHOD)
def setup(app):
    app.add_config_value('bing_verification', '', 'html')
    app.add_js_file(None)  # dummy call to ensure hook runs
    app.add_css_file(None)

    app.connect("html-page-context", add_meta_tag)

def add_meta_tag(app, pagename, templatename, context, doctree):
    meta_tag = '<meta name="msvalidate.01" content="FF8C76044EE58DBA322585596FD8260D" />'
    if "metatags" in context:
        context["metatags"] += meta_tag
