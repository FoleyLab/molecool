"""
molecool
A python package for analyzing and visualizing molecular files.  For molssi workshop.
"""

# Add imports here
from .functions import canvas, zen
from .measure import calculate_distance, calculate_angle
from .molecule import build_bond_list, calculate_molecular_mass, calculate_center_of_mass
from .visualize import draw_bond_histogram, draw_molecule

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
