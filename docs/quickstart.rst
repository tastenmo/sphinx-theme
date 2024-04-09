===============
Quickstart
===============

The repository of basic sphinx theme is hosted on forgejo_.

*********************************
Adding the theme to your project
*********************************

1. Add the theme to your pyproject.toml file as a dependency:
   
   .. code:: toml

      [tool.poetry.dependencies]
      ...
      sphinx-theme = { git = "https://forge.escad.de/forgejo/sphinx-docs/sphinx-theme.git" }
      ...


2. Update the `html_theme` in your `conf.py`.
   
   .. code:: python

      html_theme = "sphinx_theme"



3. Your Sphinx documentation's HTML pages will now be generated with this theme! 🎉

*****************************
Install the package with pip
*****************************
A package is available on our PyPI-Registry. Find available versions on the registry_.

To install the package with pip, run the following command:

.. code:: powershell

   pip install --index-url https://forge.escad.de/forgejo/api/packages/sphinx-docs/pypi/simple/ sphinx-theme

.. _forgejo: https://forge.escad.de/forgejo/sphinx-docs/sphinx-theme.git

.. _registry: https://forge.escad.de/forgejo/sphinx-docs/-/packages