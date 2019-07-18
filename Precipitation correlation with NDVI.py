# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 20:13:47 2019

@author: 123456
"""


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
 
# Data for plotting
timeArrayNdvi = np.array([2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000, 1999, 1998, 1997 ,1996 ,1995 ,1994 , 1993, 1992, 1991, 1990, 1989, 1988, 1987, 1986, 1985, 1984, 1983, 1982])
NDVIMeanValues = ndvivaluestxt #we got this value from other code
#s = np.array([400, 397, 395, 392, 390, 389, 387, 386, 383, 381, 379, 377, 375, 373, 370, 369, 368, 365, 363, 362, 360, 358, 357, 356, 355, 354, 353, 351, 348, 347, 345, 344, 342, 341, 340])



#Temp#####################

#from netCDF4 import Dataset
#from datetime import datetime, timedelta
#
#def timeCalculator(hoursDuration):
#    startDate = datetime(1900, 1, 1)
#    return startDate + timedelta(hours=hoursDuration)
#
#fh = Dataset('D:/BD project/project/files/meanOfAllMonth/air.mon.mean.v501.nc', 'r', format="NETCDF4")
#
#
#lon = fh.variables['lon'][:]
#lat = fh.variables['lat'][:]
#time = fh.variables['time'][:]
#meanTemp = fh.variables['air'][:]
#
#
#
#
#mothlyMeanTotal = meanTemp.mean(axis = 2).mean(axis =1)
#
#
#yearlyMean = []
#trimYearlyMeanTempForNDVI = []
#meanValue = 0
#for index in range(0, len(time)): 
#    currentDate = timeCalculator(time[index])
#    meanValue = meanValue + mothlyMeanTotal[index]
#    if currentDate.month == 12:
#        # display results final
#        meanValue = meanValue/12
#        yearlyMean.append(meanValue)
#        if currentDate.year > 1981 and currentDate.year<2016:
#            trimYearlyMeanTempForNDVI.append(meanValue)
#        meanValue = 0


from netCDF4 import Dataset
import calendar

def timeCalculator(hoursDuration):
    startDate = datetime(1900, 1, 1)
    return startDate + timedelta(hours=hoursDuration)

fh = Dataset('D:/BD project/project/files/meanEveryMonth/precip.mon.total.v501.nc', 'r', format="NETCDF4")


lon = fh.variables['lon'][:]
lat = fh.variables['lat'][:]
time = fh.variables['time'][:]
precip = fh.variables['precip'][:]

mothlyMeanTotal = precip.mean(axis = 2).mean(axis =1)

trimYearlyMeanPrecipForNDVI = []
yearlyMeanPrecip = []
yearlyTotal = []
meanValue = 0
totalValue = 0
for index in range(0, len(time)): 
    currentDate = timeCalculator(time[index])
    totalDays = calendar.monthrange(currentDate.year, currentDate.month)[1]
    meanValue = meanValue + mothlyMeanTotal[index]/totalDays*10
    totalValue = meanValue + mothlyMeanTotal[index]*10
    if currentDate.month == 12:
        # display results final
        meanValue = meanValue/12
        yearlyMeanPrecip.append(meanValue)
        yearlyTotal.append(totalValue)
        if currentDate.year > 1981 and currentDate.year<2016:
            trimYearlyMeanPrecipForNDVI.append(meanValue)
        meanValue = 0
        
        
r = np.corrcoef(trimYearlyMeanPrecipForNDVI,NDVIMeanValues)
plt.scatter(trimYearlyMeanPrecipForNDVI,NDVIMeanValues)
plt.title('NDVI Vs Perciptation Pearson Coefficient = '+ str(r[0][1]))
plt.ylabel('NDVI')
plt.xlabel('Perciptation')
        