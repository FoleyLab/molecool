"""
functions.py
A python package for analyzing and visualizing molecular files.  For molssi workshop.

Handles the primary functions
"""

### new functions go brrrr
import os
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


def zen(with_attribution=True):
    quote = """Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex."""

    if with_attribution:
        quote += """ By Time Peters """

    print(quote)


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
