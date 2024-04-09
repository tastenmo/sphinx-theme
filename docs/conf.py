# Configuration file for the Sphinx documentation builder.
#
# Full list of options can be found in the Sphinx documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from typing import Any, Dict

# add the demo python code to the path, so that it can be used to demonstrate
# source links
sys.path.append(os.path.abspath("./kitchen-sink/demo_py"))

# -- Project information -----------------------------------------------------
#

project = "basic sphinx theme"
copyright = "2024, ESCAD Automation GmbH"
author = "Martin Heubuch"

# -- General configuration ---------------------------------------------------
#

extensions = [
    # Sphinx's own extensions
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    # Our custom extension, only meant for Furo's own documentation.
    "sphinx_theme.sphinxext",
    # External stuff
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_inline_tabs",
]

# -- Options for extlinks ----------------------------------------------------
#

extlinks = {
    "pypi": ("https://pypi.org/project/%s/", "%s"),
}

# -- Options for intersphinx -------------------------------------------------
#

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}

# -- Options for TODOs -------------------------------------------------------
#

todo_include_todos = True

# -- Options for Markdown files ----------------------------------------------
#

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
myst_heading_anchors = 3

# -- Options for HTML output -------------------------------------------------
#

html_theme = "sphinx_theme"
html_title = "basic sphinx theme"
html_logo = "_static/REscad.svg"
language = "en"

html_static_path = ["_static"]
html_css_files = ["pied-piper-admonition.css"]

html_theme_options: Dict[str, Any] = {
    "footer_icons": [
        {
            "name": "forgejo",
            "url": "https://forge.escad.de/forgejo/sphinx-docs/sphinx-theme",
            "html": """
                <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24">
                <path fill="currentColor" d="M16.777 0a2.9 2.9 0 1 1-2.529 4.322H12.91a4.266 4.266 0 0 0-4.265 4.195v2.118a7.08 7.08 0 0 1 4.147-1.42l.118-.002h1.338a2.9 2.9 0 0 1 5.43 1.422a2.9 2.9 0 0 1-5.43 1.422H12.91a4.266 4.266 0 0 0-4.265 4.195v2.319A2.9 2.9 0 0 1 7.222 24A2.9 2.9 0 0 1 5.8 18.57V8.589a7.11 7.11 0 0 1 6.991-7.108l.118-.001h1.338A2.9 2.9 0 0 1 16.778 0M7.223 19.905a1.194 1.194 0 1 0 0 2.389a1.194 1.194 0 0 0 0-2.389m9.554-10.464a1.194 1.194 0 1 0 0 2.389a1.194 1.194 0 0 0 0-2.39m0-7.735a1.194 1.194 0 1 0 0 2.389a1.194 1.194 0 0 0 0-2.389"/>
                </svg>
            """,
            "class": "",
        },
    ],

    "source_edit_link": "https://forge.escad.de/forgejo/sphinx-docs/sphinx-theme/_edit/main/docs/{filename}",

}

html_sidebars = {
    "**": ["sidebar/scroll-start.html",
#        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/navigation.html",
#        "sidebar/ethical-ads.html",
        "sidebar/scroll-end.html",],
        
        }


if "READTHEDOCS" in os.environ:
    html_theme_options["announcement"] = (
        "This documentation is hosted on Read the Docs only for testing. Please use "
        "<a href='https://pradyunsg.me/furo/'>the main documentation</a> instead."
    )

# -- Options for theme development -------------------------------------------
# Make sure these are all set to the default values.

html_js_files = []
html_context: Dict[str, Any] = {}
# html_show_sphinx = False
# html_show_copyright = False
# html_last_updated_fmt = ""

RTD_TESTING = False
if RTD_TESTING or "FURO_RTD_TESTING" in os.environ:
    del html_theme_options["footer_icons"]

    html_css_files += [
        "https://assets.readthedocs.org/static/css/readthedocs-doc-embed.css",
        "https://assets.readthedocs.org/static/css/badge_only.css",
    ]
    html_js_files += [
        "readthedocs-dummy.js",
        "https://assets.readthedocs.org/static/javascript/readthedocs-doc-embed.js",
    ]
    html_context["READTHEDOCS"] = True
    html_context["current_version"] = "latest"
    html_context["conf_py_path"] = "/docs/"
    html_context["display_github"] = True
    html_context["github_user"] = "pradyunsg"
    html_context["github_repo"] = "furo"
    html_context["github_version"] = "main"
    html_context["slug"] = "furo"

FONT_AWESOME_TESTING = False
if FONT_AWESOME_TESTING:
    html_css_files += [
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
    ]

    html_theme_options["footer_icons"] = [
        {
            "name": "GitHub",
            "url": "https://github.com/pradyunsg/furo",
            "html": "",
            "class": "fa-brands fa-solid fa-github fa-2x",
        },
    ]
