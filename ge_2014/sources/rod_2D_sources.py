import meep as mp

def rod_2D_sources(fc,twidth,sx,sy,pml_thickness):
        center = mp.Vector3(-sx/2.0 + pml_thickness,0,0)
        size = mp.Vector3(0,sy,0)
        sources = [mp.Source(mp.GaussianSource(
                                        frequency=fc,
                                        width=twidth,
                                        is_integrated=True
                                        ),
                                center=center,
                                size=size,
                                component=mp.Ey,
        )]
        return sources
