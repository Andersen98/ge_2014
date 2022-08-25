import meep as mp
from ..units import units
from ..sources.rod_2D_sources import rod_2D_sources
from ..geometries.rod_2D_geometries import rod_2D_geometries

rod_2D_sources_fc = 415.863*units.THz
rod_2D_geometries_width_x = 10.0*units.nm
rod_2D_geometries_height_y = 80.0*units.nm

def rod_2D_simulation(resolution, padding,pml_thickness,background_index, source_width):


    sxy = 2*padding+2*pml_thickness
    cell = mp.Vector3(sxy,sxy,0)
    pml_layers = [mp.PML(thickness=pml_thickness)]
    
    geometries = rod_2D_geometries(width_x=rod_2D_geometries_width_x,
                                    height_y=rod_2D_geometries_height_y)

    sources = rod_2D_sources(rod_2D_sources_fc,
                            source_width,
                            sxy,
                            sxy,
                            pml_thickness
                            )

    sim = mp.Simulation(cell,
                        resolution,
                        geometries,
                        sources,
                        boundary_layers=pml_layers,
                        default_material=mp.Medium(index=background_index),
                        dimensions=2)
    
    return sim