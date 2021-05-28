"""
comments about molecule.py
"""

# from the measure.py module import the function calculate_distance
import numpy as np
from .measure import calculate_distance
from .atom_data import atomic_weights

def build_bond_list(coordinates, max_bond=1.5, min_bond=0):

    # Find the bonds in a molecule (set of coordinates) based on distance criteria.
    bonds = {}
    num_atoms = len(coordinates)

    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds

def calculate_molecular_mass(symbols):
    """Calculate the mass of a molecule.
   
    Parameters
    ----------
    symbols : list
        A list of elements.
   
    Returns
    -------
    mass : float
        The mass of the molecule
    """
    molecular_mass = 0.0
    for atom in symbols:
        molecular_mass += atomic_weights[atom]
    
    return molecular_mass



def calculate_center_of_mass(symbols, coordinates):
    """Calculate the center of mass of a molecule.
    
    The center of mass is weighted by each atom's weight.
    
    Parameters
    ----------
    symbols : list
        A list of elements for the molecule
    coordinates : np.ndarray
        The coordinates of the molecule.
    
    Returns
    -------
    center_of_mass: np.ndarray
        The center of mass of the molecule.
 
    Notes
    -----
    The center of mass is calculated with the formula
    
    .. math:: \\vec{R}=\\frac{1}{M} \\sum_{i=1}^{n} m_{i}\\vec{r_{}i}
    
    """
    ### make sure symbols and coordinates have the same length!
    assert len(symbols) == len(coordinates)

    ### compute total mass
    M = calculate_molecular_mass(symbols)  
    ### make sure mass is greater than 0
    assert M > 0.0

    ### initialize R vector
    R = np.array([0.,0.,0.])
    ### loop through coordinates and symbols list
    for i in range(0, len(symbols)):
        # get mass of atom i
        m_i = atomic_weights[symbols[i]]
        # add mass-weighted coordinate of atom i to R
        R += 1/M * m_i * coordinates[i,:]

    # return center of mass!
    return R
