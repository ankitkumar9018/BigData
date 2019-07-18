# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 18:05:24 2019

@author: ankit kumar
"""

from netCDF4 import Dataset
import calendar
from datetime import datetime, timedelta

def timeCalculator(hoursDuration):
    startDate = datetime(1900, 1, 1)
    return startDate + timedelta(hours=hoursDuration)

#https://www.esrl.noaa.gov/psd/data/gridded/data.UDel_AirT_Precip.html
fh = Dataset('D:/Ankit/big data/project/files/preciption/meanEveryMonth/precip.mon.total.v501.nc', 'r', format="NETCDF4")


lon = fh.variables['lon'][:]        #longitude
lat = fh.variables['lat'][:]        #latitude
time = fh.variables['time'][:]      #time is expressed in hours since 1900
precip = fh.variables['precip'][:]  #precipitation

#mothlyMeanTotal = precip.mean(axis = 2).mean(axis =1)
t = list(range(1900,2018))

yearlyMean = []
yearlyTotal = []
maxPrecip = []
maxPrecipYearly = []
meanValue = 0
totalValue = 0
for index in range(0, len(time)): 
    currentDate = timeCalculator(time[index])
    totalDays = calendar.monthrange(currentDate.year, currentDate.month)[1]
#    meanValue = meanValue + mothlyMeanTotal[index]/totalDays*10
#    totalValue = meanValue + mothlyMeanTotal[index]*10
    b = precip[index]
    b = b[b.mask == False]
    a = b.ravel()
    ind = a.argsort()[-100:][::-1]          #takes top 100 values
    maxPrecip = a[ind]
    total = sum(maxPrecip)
    totalValue = totalValue + total/totalDays*10

    if currentDate.month == 12:
        totalValue = totalValue/12        
        maxPrecipYearly.append(totalValue)
        totalValue = 0

import matplotlib.pyplot as plt
plt.plot(t, maxPrecipYearly)
plt.title('Maximum ')

#assert timeCalculator(time[1415]) == datetime(2017, 12, 1), "Method timeCalculator is working"


