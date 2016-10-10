#! /usr/bin/env python
#
#    this will test various imports used in the notebooks
#    and report what notebook cannot function
#

import os, sys, math

try:
    print("OK Welcome to testing. We use python3")
except:
    # print "We need python3"
    sys.exit(1)

try:
    if os.path.exists("01-intro.ipynb"):
        print("OK in the correct notebooks directory")
    else:
        print("FAIL not in right notebooks directory")
        sys.exit(1)
except:
    print("FAIL")
    
try:
    import numpy as np
    import numpy.ma as ma
    import scipy
    print("OK numpy and scipy")
except:
    print("FAIL numpy/scipy missing: see 03-arrays")
    sys.exit(2)

try:
    import matplotlib
    import matplotlib.pyplot as plt
    print("OK matplotlib")
except:
    print("FAIL matplotlib: see 04-plotting")
    sys.exit(2)

    

try:
    from astropy.io import fits
    print("OK astropy")
except:
    print("FAIL astropy missing: see n6503-case1")
    sys.exit(3)

try:
    sample = '../data/ngc6503.cube.fits'
    hdu = fits.open(sample)
    print("OK sample data %s present" % sample)
except:
    print("FAIL sample data %s absent: see n6503-case1" % sample)
    sys.exit(4)

try:
    from spectral_cube import SpectralCube
    print("OK spectral_cube")
except:
    print("FAIL spectral_cube absent: see n6503-case2")
    sys.exit(5)

try:
    import radio_beam
    print("OK radio_beam")
except:
    print("FAIL radio_beam absent: see n6503-case2")
    sys.exit(6)

          
