import meep as mp
from ..units import constants
from ..sources.rod_2D_sources import rod_2D_sources
from ..geometries.rod_2D_geometries import rod_2D_geometries

rod_2D_sources_fc = 415.863*constants.THz
rod_2D_geometries_width_x = 10.0*constants.nm
rod_2D_geometries_height_y = 80.0*constants.nm

def rod_2D_simulation(resolution, padding,pml_thickness,background_index, source_width):


    sim = rod_2D_simulation_homo(resolution,padding,pml_thickness,background_index,source_width)
  
    geometries = rod_2D_geometries(width_x=rod_2D_geometries_width_x,
                                    height_y=rod_2D_geometries_height_y)
    sim.geometry = geometries
    
    return sim


def rod_2D_simulation_homo(resolution, padding,pml_thickness,background_index, source_width):


    sxy = 2*padding+2*pml_thickness
    cell = mp.Vector3(sxy,sxy,0)
    pml_layers = [mp.PML(thickness=pml_thickness)]

    sources = rod_2D_sources(rod_2D_sources_fc,
                            source_width,
                            sxy,
                            sxy,
                            pml_thickness
                            )

    sim = mp.Simulation(cell,
                        resolution,
                        sources=sources,
                        boundary_layers=pml_layers,
                        default_material=mp.Medium(index=background_index),
                        dimensions=2)
    
    return sim