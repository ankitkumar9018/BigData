# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 18:05:24 2019

@author: ankit kumar
"""
#Importimg libraries
from netCDF4 import Dataset
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
import os,glob

#https://www.esrl.noaa.gov/psd/cgi-bin/db_search/DBListFiles.pl?did=192&tid=74533&vid=20
folder_path = 'D:/Ankit/big data/project/files/surface temp'    #reading the whole folder where the data is present
index = 1                                                       #Calculating index of the file being saved
for filename in glob.glob(os.path.join(folder_path, '*.*')):

    fh = Dataset(filename.replace('\\',"/"), 'r', format="NETCDF4")


    lon = fh.variables['lon'][:]    #longitude
    lat = fh.variables['lat'][:]    #latitude
    time = fh.variables['time'][:]  ##time is recorded 4 times daily for whole year
    temp = fh.variables['air'][:]   #temperature  
    
    fh.close()                      #closing the file
    
    # Plot the field using Basemap.  Start with setting the map
    # projection using the limits of the lat/lon data itself:
    fig=plt.figure(figsize=(12, 8))
    
    # Miller projection:
    m=Basemap(projection='mill',lat_ts=10,llcrnrlon=lon.min(), \
              urcrnrlon=lon.max(),llcrnrlat=lat.min(),urcrnrlat=lat.max(), \
              resolution='c')
    
    
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







