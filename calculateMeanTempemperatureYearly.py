# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 18:05:24 2019

@author: ankit kumar
"""

from netCDF4 import Dataset
from datetime import datetime, timedelta

def timeCalculator(hoursDuration):
    startDate = datetime(1900, 1, 1)
    return startDate + timedelta(hours=hoursDuration)

#https://www.esrl.noaa.gov/psd/data/gridded/data.UDel_AirT_Precip.html
fh = Dataset('D:/Ankit/big data/project/files/meanSurfaceTemp/meanOfAllMonth/air.mon.mean.v501.nc', 'r', format="NETCDF4")


lon = fh.variables['lon'][:]         #longitude
lat = fh.variables['lat'][:]         #latitude
time = fh.variables['time'][:]       #time is expresed in hours since 1900(which is first date present)
meanTemp = fh.variables['air'][:]    #temperature (which is monthly mean temperature)


mothlyMeanTotal = meanTemp.mean(axis = 2).mean(axis =1) #this line of code calculates total mean of the whole globe and gives an array containg the value for various timeframe


yearlyMean = []     #this array stores yearly mean value
meanValue = 0       #this stores the total mean value of the whole world for each year 
for index in range(0, len(time)): 
    currentDate = timeCalculator(time[index])
    meanValue = meanValue + mothlyMeanTotal[index]
    if currentDate.month == 12:
        # display results final
        meanValue = meanValue/12
        yearlyMean.append(meanValue)
        meanValue = 0
        
#Unit Test Case
assert timeCalculator(time[1415]) == datetime(2017, 12, 1), "Method timeCalculator is working for End Date"

assert timeCalculator(time[0]) == datetime(1900, 1, 1), "Method timeCalculator is working for Start Date"

assert timeCalculator(time[221]) == datetime(1950, 1, 1), "Method timeCalculator should not work ideally"


