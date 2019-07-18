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

def timeCalculator(hoursDuration):
    startDate = datetime(1900, 1, 1)
    return startDate + timedelta(hours=hoursDuration)

fh = Dataset('D:/Ankit/big data/project/files/meanSurfaceTemp/meanOfAllMonth/air.mon.mean.v501.nc', 'r', format="NETCDF4")


lon = fh.variables['lon'][:]
lat = fh.variables['lat'][:]
time = fh.variables['time'][:]
meanTemp = fh.variables['air'][:]

rotation = 0.0
finalIndex = 1





proj = ccrs.Orthographic
dcrs = ccrs.PlateCarree()
yearlyMean = np.zeros((118,360,720),dtype=np.float64)
for index in range(0, len(time)): 
    currentDate = timeCalculator(time[index])
    yearlyMean[finalIndex-1,:,:] = np.add(yearlyMean[finalIndex-1,:,:],meanTemp[finalIndex-1,:,:])
    yearlyMean[yearlyMean <= -9.96921e+36] = None
    if currentDate.month == 12:
        # display results final
        yearlyMean[finalIndex-1,:,:] = [x/12 for x in yearlyMean[finalIndex-1,:,:]]
        yearlyMean[yearlyMean <= -9.96921e+35] = None
        fig, axes = plt.subplots(1, 3, figsize=(19.2, 10.8), sharex=True, sharey=True,subplot_kw=dict(projection=proj(0.,0.)))
        axFinal = axes.ravel()
        fig.suptitle('Global Yearly Mean Land Surface Temperature in °C', y=0.15,fontsize=18)
        plt.title(str(currentDate.year)+'                                                                                                                                                                                                             ')
        axFinal[0].set_global()
        axFinal[0].gridlines()
        axFinal[0].coastlines()
        axFinal[0].projection =proj((0. +rotation)%360,0.)
        
        im = axFinal[0].pcolormesh(lon, lat, yearlyMean[finalIndex-1,:,:],
                    cmap = plt.cm.hot_r,
                    transform = dcrs,vmin = -90, vmax = 60,
                    )
        
        
        axFinal[1].set_global()
        axFinal[1].gridlines()
        axFinal[1].coastlines()
        axFinal[1].projection = proj((120. +rotation)%360,0.)
        
        im = axFinal[1].pcolormesh(lon, lat, yearlyMean[finalIndex-1,:,:],
                    cmap = plt.cm.hot_r, #tab20c
                    transform = dcrs,vmin = -90, vmax = 60,
                    )
        
        
        axFinal[2].set_global()
        axFinal[2].gridlines()
        axFinal[2].coastlines()
        axFinal[2].projection = proj((240. +rotation)%360,0.)
    
        im = axFinal[2].pcolormesh(lon, lat, yearlyMean[finalIndex-1,:,:],
                    cmap = plt.cm.hot_r,
                    transform = dcrs,vmin = -90, vmax = 60,
                    )
        
        
        #fig.subplots_adjust(right=10)
        #cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
        cb = fig.colorbar(im, ax = axes.ravel().tolist(),
                              orientation = 'horizontal',
                          aspect = 50, shrink = 0.75,
                              )
        cb.ax.plot([0, 1], np.nanmean(yearlyMean[finalIndex-1,:,:]), 'w')
        #cb = fig.colorbar(im, cax=cbar_ax)
        #fig.tight_layout()
        plt.savefig('D:/project/files/image/test/' + str(finalIndex) + '.png') #str(new_date.date())+ str(new_date.time()).replace(':','')
        plt.close()
        finalIndex = finalIndex + 1
        rotation = (rotation + 10)%360
        

#assert timeCalculator(time[1415]) == datetime(2017, 12, 1), "Method timeCalculator is working"


