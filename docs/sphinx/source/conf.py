import os
import sys

project = "Userspace Resource Manager"
author = "Qualcomm Technologies, Inc."
copyright = "Qualcomm Technologies, Inc. and/or its subsidiaries"
version = os.environ.get("DOC_VERSION", "latest")
release = version

extensions = [
    "breathe",
    "myst_parser",
    "sphinx.ext.autosectionlabel",
    "sphinx_rtd_theme",
]

breathe_projects = {
    "URM": os.path.abspath(os.path.join(os.path.dirname(__file__), "../../doxygen/xml")),
}
breathe_default_project = "URM"
breathe_default_members = ("members", "undoc-members")

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "navigation_depth": 4,
    "titles_only": False,
    "logo_only": False,
}

html_title = f"{project} API Documentation {version}"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

myst_enable_extensions = ["colon_fence", "deflist"]
myst_heading_anchors = 3

autosectionlabel_prefix_document = True

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

master_doc = "index"

# Make docs/UserGuide and docs/ available for include directives
sys.path.insert(0, os.path.abspath("../../.."))
