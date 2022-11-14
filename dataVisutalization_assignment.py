# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 09:18:19 2022

@author: USER
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# read file RealGDP12112022.csv
RealGDP = pd.read_csv('RealGDP12112022.csv',header=0,usecols=[0,2,3,4,5,6])
RealGDP.columns = ['Year','Agriculture','CropProduction','Livestock','Forestry','Fishing']
get_rows = RealGDP.head(5)
print (get_rows)
print()
"""
Line plot showing the four different Agricultural activities such as 
CropProduction, Livestock, Forestry and Fishing from 1981 to 1985 with labels
"""
def line_plot(x_axis,holder,xticks,label,title):
    plt.figure(figsize=(10,5))
    for i in range(len(holder)):
        plt.plot(x_axis,holder[i],label=label[i])
    plt.legend()
    plt.xticks(x_axis,xticks)
    plt.title(title,fontsize=10)
    plt.show()
    
x_axis =get_rows.index
holder = [get_rows['CropProduction'],get_rows['Livestock'],get_rows['Forestry'],get_rows['Fishing']]
xticks = ['1981','1982','1983','1984','1985']
label = ['CropProduction', 'Livestock', 'Forestry', 'Fishing']
title = 'A line plot of CropProduction, Livestock, Forestry and Fishing from 1981 to 1985'

line_plot(x_axis,holder,xticks,label,title)

"""
pie chart of four different Agricultural activities such as 
CropProduction, Livestock, Forestry and Fishing from 1981 to 1985 with labels
where 0 represent 1981,1 represent 1982,2 represent 1983,3 represent 1984
and 4 represent 1985
"""
def subplot_pie_chart(x_axis,label,title):
    plt.figure(figsize=(17,10))
    for i in range(len(x_axis)):
        plt.subplot(2,2,i+1).set_title(title[i])
        plt.pie(x_axis[i],labels=label)
    plt.show()
    
x_axis = [get_rows['CropProduction'],get_rows['Livestock'],get_rows['Forestry'],get_rows['Fishing']]
label = get_rows.index
title = ['CropProduction','Livestock','Forestry','Fishing']

subplot_pie_chart(x_axis,label,title)

"""
Bar Chart showing the total number of acres harvested between  2012 to 2020 of Avocados
"""
avocados= pd.read_csv('cali_avocados.csv',header=1,skipfooter=350, usecols=[0,4,5,7,8])
avocados.columns = ['Year', 'County', 'Harvested Acres','Price','Production'] 
print(avocados)
print()
#This is to remove the missing value
avocados1 = avocados.drop(labels=[0, 13],axis=0)
print(avocados1)
print()
Year_group =avocados1.groupby('Year')[['Harvested Acres','Price','Production']].sum()
print(Year_group)
print()

def bar_chart(x_axis, holder,title):
    plt.figure(figsize=(10,5))
    plt.bar(x_axis,holder)
    plt.title(title, fontsize=10)
    plt.show()
    return

x_axis = Year_group.index
holder = Year_group['Harvested Acres']
title = 'A Bar Chart showing the total number of acres harvested between  2012 to 2020 of Avocados'
bar_chart(x_axis,holder,title)


