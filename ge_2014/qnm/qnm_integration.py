import numpy as np
import h5py
from pathlib import Path
import meep as mp
from ..simulation.rod_2D_simulation import rod_2D_simulation_homo, rod_2D_simulation
from ..simulation.rod_2D_simulation import rod_2D_sources_fc
from ..units import constants as units

def time_window(t,gammac):
    """
    Right hand factor in integral of eqn 5 from
    Ge, Rong-Chun, and S. Hughes. 
    “Design of an Efficient Single Photon Source from a Metallic Nanorod Dimer: A Quasi-Normal Mode Finite-Difference Time-Domain Approach.” 
    Optics Letters 39, no. 14 (July 15, 2014): 4235. https://doi.org/10.1364/OL.39.004235.

    choose toff=4pi/gammac
            toff/twin**2 = gammac

    """
    toff=4*np.pi/gammac
    twin = np.sqrt(toff/gammac)
    return np.exp(-(t-toff)**2 / (2*twin**2))


def output_scattered(file_total:Path,file_homo:Path, output_file:Path =Path('./output_scattered.h5')):
    assert file_homo.exists()
    assert file_total.exists()
    try:
        f_scattered = h5py.File(output_file,'w')
        f_total = h5py.File(file_total)
        f_homo = h5py.File(file_homo)
        for key in f_total.keys():
            f_scattered[key] = f_total[key][:] - f_homo[key][:]
        f_scattered.close()
        f_total.close()
        f_homo.close()
    except:
        print("ERROR LOADING FILE!")
    

def qnm_integral(t,Escatter,wc,gammac):
    """
        eqn 5 from
        Ge, Rong-Chun, and S. Hughes. 
        “Design of an Efficient Single Photon Source from a Metallic Nanorod Dimer: A Quasi-Normal Mode Finite-Difference Time-Domain Approach.” 
        Optics Letters 39, no. 14 (July 15, 2014): 4235. https://doi.org/10.1364/OL.39.004235.
    """
    np.exp(x=1.0j*wc*t)*time_window(t,gammac)

def make_sample_homo(time_after:int,output_homo:Path = Path('./output_homo.h5')):
    """
    A samplehomo...geneous case with no scatterer.
    """
    resolution = 20
    padding = 4.0
    nb =1.5
    pml_thickness = 1.0/rod_2D_sources_fc
    source_width = 6*units.fs #smoothing

    sim_homo = rod_2D_simulation_homo(resolution=resolution,
                            padding=padding,
                            pml_thickness=pml_thickness,
                            background_index=nb,
                            source_width=source_width)
    sim_homo.init_sim()
    sim_homo.run(mp.at_every(.1, mp.to_appended(output_homo.stem, mp.output_efield_y,mp.output_efield_x)),until_after_sources=time_after)


def make_sample_total(time_after:int,output_total:Path = Path('./output_total.h5')):
    """
    A sample case with scatterer present.
    """
    resolution = 20
    padding = 4.0
    nb =1.5
    pml_thickness = 1.0/rod_2D_sources_fc
    source_width = 6*units.fs #smoothing

    sim = rod_2D_simulation(resolution=resolution,
                            padding=padding,
                            pml_thickness=pml_thickness,
                            background_index=nb,
                            source_width=source_width)
    sim.init_sim()
    sim.run(mp.at_every(.1, mp.to_appended(output_total.stem, mp.output_efield_y,mp.output_efield_x)),until_after_sources=time_after)
