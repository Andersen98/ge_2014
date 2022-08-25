import pytest
import numpy as np
import ge_2014.units.units as units

def test_unit_length():
    #should be micron
    np.testing.assert_almost_equal(units.meep_unit_length_si,1.0e-6)

def test_unit_frequency():
    #Test roughly that meep_unit_frequency_si=3*10**14
    np.testing.assert_almost_equal(units.meep_unit_frequency_si/2.99792e+14,
                                    1.0,decimal=4)

def test_unit_time():
    #unit time should roughly be 3.33333... fempto seconds
    np.testing.assert_almost_equal(units.meep_init_time_si, 3.33333e-15,
                                    decimal=4)


def test_fs():
    #fempto second should be around .3
    np.testing.assert_almost_equal(units.fs,.299792458 )

def test_THz():
    #THz should be around 1/300
    thz_target = 1/299.792458
    np.testing.assert_almost_equal(units.THz,thz_target)