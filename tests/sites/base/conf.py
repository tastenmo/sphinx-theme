"""Test conf file."""

# -- Project information -----------------------------------------------------

project = "PyData Tests"
copyright = "2020, Pydata community"
author = "Pydata community"

root_doc = "index"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []
html_theme = "sphinx_theme"
html_logo = "_static/REscad.svg"
html_copy_source = True
html_sourcelink_suffix = ""

# Base options, we can add other key/vals later
html_theme_options = {"navigation_with_keys": False,

    "source_repository": "https://github.com/tastenmo/sphinx-theme",
    "source_branch": "main",
    "source_directory": "tests/sites/base/",
#    "announcement": "This is a <em>unreleased</em> test version!",

}


html_sidebars = {
    "**": ["sidebar/scroll-start.html",
#        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/navigation.html",
#        "sidebar/ethical-ads.html",
        "sidebar/scroll-end.html",],
    
    
    "section1/index": ["sidebar/scroll-start.html",
#        "sidebar/brand.html",
#        "sidebar/search.html",
        "sidebar/navigation.html",
#        "sidebar/ethical-ads.html",
        "sidebar/scroll-end.html",]
        
        }
