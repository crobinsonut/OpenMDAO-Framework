import time
import os
import numpy as np

import stl
from ffd_axisymetric import Body, Shell
from stl_group import STLGroup


class PlugNozzleGeometry(STLGroup): 

    def __init__(self): 
        super(PlugNozzleGeometry,self).__init__()

        this_dir, this_filename = os.path.split(stl.__file__)
        
        plug_file = os.path.join(this_dir, 'test', 'nozzle', 'plug.stl')
        plug = stl.STL(plug_file)
        cowl_file = os.path.join(this_dir, 'test', 'nozzle', 'cowl.stl')
        cowl = stl.STL(cowl_file)
        
        n_c = 10
        body = Body(plug,controls=n_c) #just makes n_C evenly spaced points
        shell = Shell(cowl,cowl.copy(),n_c,n_c)

        self.add(body,name="plug")
        self.add(shell,name="cowl")


if __name__=="__main__": 
    pn = PlugNozzleGeometry()

    print pn.list_parameters()




