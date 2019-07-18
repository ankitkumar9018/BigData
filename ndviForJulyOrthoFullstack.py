# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 18:05:24 2019

@author: ankit kumar
"""


from netCDF4 import Dataset
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
from datetime import datetime, timedelta
from matplotlib.colors import LogNorm
import cartopy.crs as ccrs
import os,glob

folder_path = 'D:/Ankit/big data/project/files/ndvi'




#startDate = datetime(1981, 1, 1)
#new_date = startDate + timedelta(21) #timedelta(hours=9)
#print (new_date)
rotation = 0.0
finalIndex = 1
year = 1981
for filename in glob.glob(os.path.join(folder_path, '*.*')):
    #print(filename.replace('\\',"/"))

    

    startDate = datetime(year, 7, 1)
    new_date = startDate
    fh = Dataset(filename.replace('\\',"/"), 'r', format="NETCDF4")


    lon = fh.variables['longitude'][:]
    lat = fh.variables['latitude'][:]
    time = fh.variables['time'][:]
    ndvi = fh.variables['NDVI'][:]
    # Get some parameters for the Stereographic Projection
    #lon_0 = lon.mean()
    #lat_0 = lat.mean()
    
    print('starting processing '+ str(filename.replace('\\',"/").split('/')[6]))
    fh.close()
    
    for index in range(0, len(time)): 
    
        norm = LogNorm(1, 100)
        proj = ccrs.Orthographic
        dcrs = ccrs.PlateCarree()
        
        # display results final
        fig, axes = plt.subplots(1, 3, figsize=(19.2, 10.8), sharex=True, sharey=True,subplot_kw=dict(projection=proj(0.,0.)))
        axFinal = axes.ravel()
        fig.suptitle('Global NDVI', y=0.15,fontsize=18)
        plt.title(str(new_date)+'                                                                                                                                                                                                             ')
        axFinal[0].set_global()
        axFinal[0].gridlines()
        axFinal[0].coastlines()
        axFinal[0].projection =proj((0. +rotation)%360,0.)
        
        im = axFinal[0].pcolormesh(lon, lat, ndvi[index,:,:],
                    cmap = plt.cm.viridis_r,
                    transform = dcrs, vmin = -1, vmax = 1,
                    )
        
        
        axFinal[1].set_global()
        axFinal[1].gridlines()
        axFinal[1].coastlines()
        axFinal[1].projection = proj((120. +rotation)%360,0.)
        
        im = axFinal[1].pcolormesh(lon, lat, ndvi[index,:,:],
                    cmap = plt.cm.viridis_r,
                    transform = dcrs,vmin = -1, vmax = 1,
                    )
        
        
        axFinal[2].set_global()
        axFinal[2].gridlines()
        axFinal[2].coastlines()
        axFinal[2].projection = proj((240. +rotation)%360,0.)
        
        im = axFinal[2].pcolormesh(lon, lat, ndvi[index,:,:],
                    cmap = plt.cm.viridis_r,
                    transform = dcrs, vmin = -1, vmax = 1,
                    )
        
        
        #fig.subplots_adjust(right=10)
        #cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
        cb = fig.colorbar(im, ax = axes.ravel().tolist(),
                          orientation = 'horizontal',
                          aspect = 50, shrink = 0.75,
                          )
        
        plt.savefig('D:/Ankit/big data/project/files/image/ndvi/'+ str(finalIndex) + '.png') #str(new_date.date())+ str(new_date.time()).replace(':','')
        # Add a colorbar and title, and then show the plot.
        plt.close()
        finalIndex = finalIndex + 1
        #new_date = new_date + timedelta(hours=6)
        rotation = (rotation + 20)%360
        print('percentage Complete for '+ str(filename.replace('\\',"/").split('/')[6])+' : '+str(index/len(time)*100))
    year = year + 1
    print('ending processing '+ str(filename.replace('\\',"/").split('/')[6]))