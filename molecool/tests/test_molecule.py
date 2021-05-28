""" 
Tests for the molecule module
"""

import pytest
import molecool
import numpy as np

def test_molecular_mass():
    ''' function to test calculate_molecular_mass function  '''
    symbols = ['C', 'H', 'H', 'H', 'H']

    calculated_mass = molecool.calculate_molecular_mass(symbols)
    actual_mass = 16.04

    assert pytest.approx(actual_mass, abs=1e-2) == calculated_mass

def test_center_of_mass():
    symbols = np.array(['C', 'H', 'H', 'H', 'H'])
    coordinates = np.array([[1.,1.,1.], [2.4,1.,1.], [-0.4, 1., 1.], [1., 1., 2.4], [1., 1., -0.4]])
#
    center_of_mass = molecool.calculate_center_of_mass(symbols, coordinates)

    expected_center = np.array([1.,1.,1.])
#
    assert np.array_equal(center_of_mass, expected_center)
