# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 18:05:24 2019

@author: ankit kumar
"""

from netCDF4 import Dataset
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
import os,glob

#https://www.esrl.noaa.gov/psd/thredds/catalog/Datasets/cmap/catalog.html
folder_path = 'D:/Ankit/big data/project/files/surface temp'
index = 1
for filename in glob.glob(os.path.join(folder_path, '*.*')):
    #print(filename.replace('\\',"/"))



    fh = Dataset(filename.replace('\\',"/"), 'r', format="NETCDF4")


    lon = fh.variables['lon'][:]
    lat = fh.variables['lat'][:]
    time = fh.variables['time'][:]
    temp = fh.variables['air'][:]
    
    # Get some parameters for the Stereographic Projection
    lon_0 = lon.mean()
    lat_0 = lat.mean()
    
    
    fh.close()
    
    # Plot the field using Basemap.  Start with setting the map
    # projection using the limits of the lat/lon data itself:
    fig=plt.figure(figsize=(12, 8))
    
    # Miller projection:
    m=Basemap(projection='mill',lat_ts=10,llcrnrlon=lon.min(), \
              urcrnrlon=lon.max(),llcrnrlat=lat.min(),urcrnrlat=lat.max(), \
              resolution='c')
    
    m = Basemap(projection='ortho',lon_0=-105,lat_0=40,resolution='l')
    # convert the lat/lon values to x/y projections.
    
    x, y = m(*np.meshgrid(lon,lat))
    
    # plot the field using the fast pcolormesh routine 
    # set the colormap to jet.
    
    m.pcolormesh(x,y,temp[0, :, :],shading='flat',cmap=plt.cm.jet, vmin = 220, vmax = 360)
    m.colorbar(location='right')
    
    # Add a coastline and axis values.
    
    m.drawcoastlines()
    #m.fillcontinents()
    #m.drawmapboundary()
    
    m.drawparallels(np.arange(-90.,90.,30.),labels=[1,0,0,0])
    m.drawmeridians(np.arange(-180.,180.,60.),labels=[0,0,0,1])
    plt.savefig('D:/Ankit/big data/project/files/image/temperature/'+ str(index) + '.png')
    # Add a colorbar and title, and then show the plot.
    index = index + 1
    plt.close()

#
#import matplotlib.pyplot as plt
#import cartopy.crs as ccrs
#
#plt.figure(figsize=(12, 8))
#ax = plt.axes(projection=ccrs.Orthographic())
#lccproj = ccrs.LambertConformal(central_latitude = 25, 
#                         central_longitude = 265, 
#                         standard_parallels = (25, 25))
#ax.contourf(lon,lat,temp[0, :, :])
#ax.coastlines(resolution='110m')
#
#ax.gridlines()
#
#
#
#import matplotlib.pyplot as plt
#import cartopy.crs as ccrs
#from cartopy.feature import OCEAN
#import warnings
#
#warnings.filterwarnings('ignore')
#
#projections = [ccrs.PlateCarree(-60), ccrs.AlbersEqualArea(-60), ccrs.TransverseMercator(-60), ccrs.Orthographic(-60, 30)]
#titles = ['Equirectangular projection', 
#          'Albers equal-area conic projection', 
#          'Transverse mercator projection', 
#          'Orthographic projection']
#
#fig, axes = plt.subplots(2, 2, subplot_kw={'projection': projections[0]}, figsize=(15,10))
#
#ny_lon, ny_lat = -75, 43
#
#for ax, proj, title in zip(axes.ravel(), projections, titles):
#    ax.projection = proj # Here we change projection for each subplot.
#    ax.set_title(title) # Add title for each subplot.
#    ax.set_global() # Set global extention
#    ax.coastlines() # Add coastlines
#    ax.add_feature(OCEAN) # Add oceans
#    ax.tissot(facecolor='r', alpha=.8, lats=np.arange(-90,90, 30)) # Add tissot indicatrisses
#    ax.plot(ny_lon, ny_lat, 'ko', transform=ccrs.Geodetic()) # Plot the point for the NY city
#    ax.text(ny_lon + 4, ny_lat + 4, 'New York', transform=ccrs.Geodetic()) # Label New York
#    ax.gridlines(color='.25', ylocs=np.arange(-90,90, 30)) # Ad gridlines
#plt.show()



