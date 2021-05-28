"""
Unit and regression test for the molecool package.
"""

# Import package, test suite, and other packages as needed
import molecool
import pytest
import sys
import numpy as np

def test_molecool_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "molecool" in sys.modules

def test_calculate_distance():
    """ testing that calculate distance the function calculates what we expect"""
    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 1, 0])

    expected_distance = 1
    calculated_distance = molecool.calculate_distance(r1, r2)
    assert expected_distance == calculated_distance


def test_calculate_angle():
    """ testing that calculates the angle """
    r1 = np.array([0, 0, -1])
    r2 = np.array([0, 0, 0])
    r3 = np.array([1, 0, 0])

    expected_angle = np.pi / 2

    assert expected_angle == molecool.calculate_angle(r1, r2, r3, degrees=False)

def test_build_bond_list():
    coordinates = np.array([
      [1, 1, 1], 
      [2.4, 1, 1],
      [-0.4, 1, 1],
      [1, 1, 2.4],
      [1, 1, -0.4]])

    bonds = molecool.build_bond_list(coordinates)
    ### there should be 4 bonds
    assert len(bonds) == 4
   
    for bond_length in bonds.values():
        assert bond_length == 1.4


def test_molecular_mass():
    ''' function to test calculate_molecular_mass function  '''
    symbols = ['C', 'H', 'H', 'H', 'H']

    calculated_mass = molecool.calculate_molecular_mass(symbols)
    actual_mass = 16.04

    assert pytest.approx(actual_mass, abs=1e-2) == calculated_mass 
