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
import calendar

def timeCalculator(hoursDuration):
    startDate = datetime(1900, 1, 1)
    return startDate + timedelta(hours=hoursDuration)

fh = Dataset('D:/project/files/meanEveryMonth/precip.mon.total.v501.nc', 'r', format="NETCDF4")


lon = fh.variables['lon'][:]
lat = fh.variables['lat'][:]
time = fh.variables['time'][:]
precip = fh.variables['precip'][:]

rotation = 0.0
finalIndex = 1





proj = ccrs.Orthographic
dcrs = ccrs.PlateCarree()

for index in range(0, len(time)): 
    
    # display results final
    fig, axes = plt.subplots(1, 3, figsize=(19.2, 10.8), sharex=True, sharey=True,subplot_kw=dict(projection=proj(0.,0.)))
    axFinal = axes.ravel()
    currentDate = timeCalculator(time[index])
    totalDays = calendar.monthrange(currentDate.year, currentDate.month)[1]
    totalPrecip = precip[index,:,:]
    totalPrecip[:] = [x/totalDays*10 for x in totalPrecip]
    totalPrecip[totalPrecip == -9.96921e+36] = None
    fig.suptitle('Global Monthly Mean Precipitation in mm', y=0.15,fontsize=18)
    plt.title(str(currentDate)+'                                                                                                                                                                                                             ')
    axFinal[0].set_global()
    axFinal[0].gridlines()
    axFinal[0].coastlines()
    axFinal[0].projection =proj((0. +rotation)%360,0.)
    
    im = axFinal[0].pcolormesh(lon, lat, precip[index,:,:],
                cmap = plt.cm.tab20c,
                transform = dcrs,vmin = 0, vmax = 50,
                )
    

    axFinal[1].set_global()
    axFinal[1].gridlines()
    axFinal[1].coastlines()
    axFinal[1].projection = proj((120. +rotation)%360,0.)
    
    im = axFinal[1].pcolormesh(lon, lat, precip[index,:,:],
                cmap = plt.cm.tab20c, #tab20c
                transform = dcrs,vmin = 0, vmax = 50,
                )
    
    
    axFinal[2].set_global()
    axFinal[2].gridlines()
    axFinal[2].coastlines()
    axFinal[2].projection = proj((240. +rotation)%360,0.)
    
    im = axFinal[2].pcolormesh(lon, lat, precip[index,:,:],
                cmap = plt.cm.tab20c,
                transform = dcrs,vmin = 0, vmax = 50,
                )
    
    
    #fig.subplots_adjust(right=10)
    #cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
    cb = fig.colorbar(im, ax = axes.ravel().tolist(),
                          orientation = 'horizontal',
                          aspect = 50, shrink = 0.75,
                          )
    #cb = fig.colorbar(im, cax=cbar_ax)
    #fig.tight_layout()
    plt.savefig('D:/project/files/image/meanPrecipitationMonthly/'+ str(finalIndex) + '.png') #str(new_date.date())+ str(new_date.time()).replace(':','')
    plt.close()
    finalIndex = finalIndex + 1
    rotation = (rotation + 10)%360


#assert timeCalculator(time[1415]) == datetime(2017, 12, 1), "Method timeCalculator is working"


