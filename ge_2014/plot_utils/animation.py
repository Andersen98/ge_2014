import numpy as np
from pathlib import Path
import h5py
import matplotlib.pyplot as plt
from skimage import img_as_float

def h5_time_series_png(input_file:Path,key:str,output_folder:Path = Path('./img_out/')):
    try:
        f= h5py.File(input_file)
        dset = f[key]
        plt.axis("off")
        num_time_steps = dset.shape[-1]
        for i in range(num_time_steps):
            image =dset[:,:,i]
            filename_out = 'frame_{0:07}.png'.format(i)
            plt.imsave(Path(output_folder,filename_out),image)
            
    except:
        print('Error')