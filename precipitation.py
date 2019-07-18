# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 18:05:24 2019

@author: ankit kumar
"""

from netCDF4 import Dataset
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
from matplotlib.colors import LogNorm
from datetime import datetime, timedelta

def timeCalculator(hoursDuration):
    startDate = datetime(1900, 1, 1)
    return startDate + timedelta(hours=hoursDuration)

fh = Dataset('D:/Ankit/big data/project/files/preciption/meanEveryMonth/precip.mon.total.v501.nc', 'r', format="NETCDF4")


lon = fh.variables['lon'][:]
lat = fh.variables['lat'][:]
time = fh.variables['time'][:]
precip = fh.variables['precip'][:]

# Get some parameters for the Stereographic Projection
lon_0 = lon.mean()
lat_0 = lat.mean()


fh.close()

# Plot the field using Basemap.  Start with setting the map
# projection using the limits of the lat/lon data itself:
fig=plt.figure(figsize=(12, 8) )

# Miller projection:
m=Basemap(projection='mill',lat_ts=10,llcrnrlon=lon.min(), \
  urcrnrlon=lon.max(),llcrnrlat=lat.min(),urcrnrlat=lat.max(), \
  resolution='c')


# convert the lat/lon values to x/y projections.

x, y = m(*np.meshgrid(lon,lat))

# plot the field using the fast pcolormesh routine 
# set the colormap to jet.
norm = LogNorm(1, 100)
m.pcolormesh(x,y,precip[455, :, :],shading='flat',cmap=plt.cm.jet)
m.colorbar(location='right')

# Add a coastline and axis values.

m.drawcoastlines()
#m.fillcontinents()
#m.drawmapboundary()
m.drawparallels(np.arange(-90.,90.,30.),labels=[1,0,0,0])
m.drawmeridians(np.arange(-180.,180.,60.),labels=[0,0,0,1])

# Add a colorbar and title, and then show the plot.

assert timeCalculator(time[1415]) == datetime(2017, 12, 1), "Method timeCalculator is working"





