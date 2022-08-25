import meep as mp
from nano_optics_materials.ge_2014 import Metal_1


def rod_2D_geometries(width_x, height_y):
    geometries = [mp.Block(size = mp.Vector3(width_x,height_y)
                ,material=Metal_1)]
    return geometries