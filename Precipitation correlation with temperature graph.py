# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 19:35:49 2019

@author: 123456
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 18:37:15 2019

@author: 123456
"""

from netCDF4 import Dataset
from datetime import datetime, timedelta

def timeCalculator(hoursDuration):
    startDate = datetime(1900, 1, 1)
    return startDate + timedelta(hours=hoursDuration)

fh = Dataset('D:/BD project/project/files/meanOfAllMonth/air.mon.mean.v501.nc', 'r', format="NETCDF4")


lon = fh.variables['lon'][:]
lat = fh.variables['lat'][:]
time = fh.variables['time'][:]
meanTemp = fh.variables['air'][:]




mothlyMeanTotal = meanTemp.mean(axis = 2).mean(axis =1)


yearlyMean = []
trimYearlyMeanTemp = []
meanValue = 0
for index in range(0, len(time)): 
    currentDate = timeCalculator(time[index])
    meanValue = meanValue + mothlyMeanTotal[index]
    if currentDate.month == 12:
        # display results final
        meanValue = meanValue/12
        yearlyMean.append(meanValue)
        if currentDate.year > 1980 and currentDate.year<2016:
            trimYearlyMeanTemp.append(meanValue)
        meanValue = 0
        
        
#prep
        

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

trimYearlyMeanPrecip = []
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
        if currentDate.year > 1980 and currentDate.year<2016:
            trimYearlyMeanPrecip.append(meanValue)
        meanValue = 0

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


# Data for plotting
t = list(range(1981,2015))
v = list(yearlyMeanPrecip)
#assert timeCalculator(time[1415]) == datetime(2017, 12, 1), "Method timeCalculator is working"


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


# Data for plotting
t = list(range(1981,2016))
s = list(trimYearlyMeanTemp)
#s = np.array([400, 397, 395, 392, 390, 389, 387, 386, 383, 381, 379, 377, 375, 373, 370, 369, 368, 365, 363, 362, 360, 358, 357, 356, 355, 354, 353, 351, 348, 347, 345, 344, 342, 341, 340])
fig, ax = plt.subplots()
ax.plot(t, s)
model = LinearRegression()

ax.set(xlabel='time (s)', ylabel='Mean Temperature (C)',
       title='Mean Yearly Tempreture, from 1900 to 2018 every Year')
ax.grid()

import pylab
x = t
v = s

pylab.plot(x,y,'o', label = 'Data Points', color = 'b')

# calc the trendline
z = np.polyfit(x, y, 6)
p = np.poly1d(z)
pylab.plot(x,p(x),"r--", linewidth = 3, label = 'trend line')
# the line equation:
plt.legend(loc = 'upper left')
print("y=%.6fx+(%.6f)"%(z[0],z[1]))

fig.savefig("test.png")
plt.show() 



t = list(range(1981,2016))
color = 'tab:blue'
s = list(trimYearlyMeanTemp)
fig, ax1 = plt.subplots()
ax1.plot(x,v)
ax2 = ax1.twinx()
ax2.grid()
ax1.set_xlabel('time (s)')
ax1.set_ylabel('Mean Temperature (C)', color=color)
ax1.tick_params(axis='y' , labelcolor=color)
ax1.plot(x , v , color=color)
plt.legend('y' , loc = 'upper left')
color = 'tab:red'
ax2.set_ylabel('Precipitation', color=color)
#ax2.plot(x , s , color=color)
ax2.tick_params(axis='y' , labelcolor=color)
ax2.set_title('Precipitation and Mean Temprature Relation')
#pylab.plot(x,y,'o', label = 'Data Points', color = 'b')
#
## calc the trendline
#z = np.polyfit(x, v, 2)
#p = np.poly1d(z)
#pylab.plot(x,p(x),"r--", linewidth = 3, label = 'trend line')
## the line equation:
#plt.legend(loc = 'upper left')
ax2.plot(x,v[::-1], color=color)
#plt.legend('y' , 'r', loc = 'upper left')


r = np.corrcoef(trimYearlyMeanTemp[::-1],v)
plt.scatter(trimYearlyMeanTemp[::-1],v)
plt.title('Percipitation Vs Temp Pearson Coefficient = '+ str(r[0][1]))
plt.ylabel('Percipitation')
plt.xlabel('Temperature')