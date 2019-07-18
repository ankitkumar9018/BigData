# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 18:05:24 2019

@author: ankit kumar
"""

from netCDF4 import Dataset
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

#https://www.esrl.noaa.gov/psd/cgi-bin/db_search/DBListFiles.pl?did=192&tid=74533&vid=20
fh = Dataset('D:/Ankit/big data/project/files/surface temp/air.sig995.2018.nc', 'r', format="NETCDF4")


lon = fh.variables['lon'][:]    #longitude
lat = fh.variables['lat'][:]    #latitude
time = fh.variables['time'][:]  #time is recorded 4 times daily for whole year
temp = fh.variables['air'][:]   #temperature  


# =============================================================================
# Basic Plot of Data
# =============================================================================

plt.imshow(temp[0,:,:])


# =============================================================================
# Orthographic Plot of Data
# =============================================================================
from matplotlib import pyplot as pl
from matplotlib.colors import LogNorm
import cartopy.crs as ccrs

norm = LogNorm(1, 100)
proj = ccrs.Orthographic
dcrs = ccrs.PlateCarree()


fg = pl.figure(2, (19.2, 10.8))
ax = pl.axes(projection = proj(0.,0.))
ax.set_global()
ax.gridlines()
ax.coastlines()
im = ax.pcolormesh(lon, lat, temp[0,:,:],
        cmap = pl.cm.viridis_r,
        transform = dcrs,
        )
cb = fg.colorbar(im, ax = ax,
        orientation = 'horizontal',
        aspect = 50, shrink = 0.75,
        )
cb.set_label('Precipitation rate [mm/h]')
pl.show()




































