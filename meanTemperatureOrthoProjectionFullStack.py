# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 18:05:24 2019

@author: ankit kumar
"""

from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import cartopy.crs as ccrs

#method to calculate
def timeCalculator(hoursDuration):
    startDate = datetime(1900, 1, 1)
    return startDate + timedelta(hours=hoursDuration)

#https://www.esrl.noaa.gov/psd/data/gridded/data.UDel_AirT_Precip.html
fh = Dataset('D:/Ankit/big data/project/files/meanSurfaceTemp/meanOfAllMonth/air.mon.mean.v501.nc', 'r', format="NETCDF4")


lon = fh.variables['lon'][:]        #longitude
lat = fh.variables['lat'][:]        #latitude
time = fh.variables['time'][:]      #time is expresed in hours since 1900(which is first date present)
meanTemp = fh.variables['air'][:]   #temperature (which is monthly mean temperature)

rotation = 0.0 #rotation
finalIndex = 1 #index to monitor files





proj = ccrs.Orthographic
dcrs = ccrs.PlateCarree()

for index in range(0, len(time)): 
    
    # display results final
    fig, axes = plt.subplots(1, 3, figsize=(19.2, 10.8), sharex=True, sharey=True,subplot_kw=dict(projection=proj(0.,0.)))
    axFinal = axes.ravel()
    fig.suptitle('Global Mean Land Surface Temperature in °C', y=0.15,fontsize=18)
    plt.title(str(timeCalculator(time[index]))+'                                                                                                                                                                                                             ')
    axFinal[0].set_global()
    axFinal[0].gridlines()
    axFinal[0].coastlines()
    axFinal[0].projection =proj((0. +rotation)%360,0.)
    
    im = axFinal[0].pcolormesh(lon, lat, meanTemp[index,:,:],
                cmap = plt.cm.hot_r,
                transform = dcrs,vmin = -90, vmax = 60,
                )
    

    axFinal[1].set_global()
    axFinal[1].gridlines()
    axFinal[1].coastlines()
    axFinal[1].projection = proj((120. +rotation)%360,0.)
    
    im = axFinal[1].pcolormesh(lon, lat, meanTemp[index,:,:],
                cmap = plt.cm.hot_r, #tab20c
                transform = dcrs,vmin = -90, vmax = 60,
                )
    
    
    axFinal[2].set_global()
    axFinal[2].gridlines()
    axFinal[2].coastlines()
    axFinal[2].projection = proj((240. +rotation)%360,0.)
    
    im = axFinal[2].pcolormesh(lon, lat, meanTemp[index,:,:],
                cmap = plt.cm.hot_r,
                transform = dcrs,vmin = -90, vmax = 60,
                )
    
    
    #fig.subplots_adjust(right=10)
    #cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
    cb = fig.colorbar(im, ax = axes.ravel().tolist(),
                          orientation = 'horizontal',
                          aspect = 50, shrink = 0.75,
                          )
    #cb = fig.colorbar(im, cax=cbar_ax)
    #fig.tight_layout()
    plt.savefig('D:/Ankit/big data/project/files/image/meanTemperature/' + str(finalIndex) + '.png') #str(new_date.date())+ str(new_date.time()).replace(':','')
    plt.close()
    finalIndex = finalIndex + 1
    rotation = (rotation + 10)%360


#assert timeCalculator(time[1415]) == datetime(2017, 12, 1), "Method timeCalculator is working"


