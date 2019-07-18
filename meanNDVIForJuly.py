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

folder_path = 'D:/BD project/project/files/ndvi'




#startDate = datetime(1981, 1, 1)
#new_date = startDate + timedelta(21) #timedelta(hours=9)
#print (new_date)
rotation = 0.0
finalIndex = 1
year = 1981 #2013
yearlyMean = []
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
    
    #print('starting processing '+ str(filename.replace('\\',"/").split('/')[6]))
    fh.close()
    yearlyMean.append(ndvi.mean(axis = 2).mean(axis =1)[0])
    year = year + 1
   # print('ending processing '+ str(filename.replace('\\',"/").split('/')[6]))
   
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


# Data for plotting
t = list(range(1981,2014))
s = list(yearlyMean)
#s = np.array([400, 397, 395, 392, 390, 389, 387, 386, 383, 381, 379, 377, 375, 373, 370, 369, 368, 365, 363, 362, 360, 358, 357, 356, 355, 354, 353, 351, 348, 347, 345, 344, 342, 341, 340])
fig, ax = plt.subplots()
ax.plot(t, s)
model = LinearRegression()

ax.set(xlabel='time (s)', ylabel='NDVI (INDEX)',
       title='NDVI Yearly , from 1981 to 2014 every Year')
ax.grid()

import pylab
x = t
y = s

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