#import required libraries
import pandas as pd
from pandas import DataFrame as df
import matplotlib.pyplot as plt
import numpy as np
#arrange the state of india from higest number of states to lower
#reading only the columns with name as State name District name Population
census11= pd.read_csv('india-districts-census-2011.csv' ,
                      usecols = ['State name','District name','Population'])
#initalized required list and dataframe
All_States=[]
Dist_Count =[]
Statewise_population=[]
df = pd.DataFrame()
# creating a list without reoccurance of any state name. 
[All_States.append(x) for x in census11['State name'] if x not in All_States]
# sorted states in india from lowest to highest number of district in a state
for i in All_States:
    Census_of_each_state = census11.loc[census11['State name'] == i]
    District_count = Census_of_each_state['District name'].count() 
    Pop_count = Census_of_each_state['Population'].sum() 
    #print(" %s ="%i, Census_of_each_state['District name'].count())
    Dist_Count.append(District_count)
    Statewise_population.append(Pop_count)
df.insert(loc=0, column='State', value=All_States)
df.insert(loc=1, column='District count', value=Dist_Count)
df.insert(loc=2, column='Statewise_population', value=Statewise_population)
sort_df= df.sort_values(by=['District count'])
print(sort_df)
#Total India Population
total_pop =np.sum(Statewise_population) 
print("Total_india_population _in 2011:",total_pop)
#make a bar charts for statewise district population comparision
def plot_all_state(State):
    for i in State:
        State_name= census11.loc[census11['State name'] == i]
        fig = plt.figure()
        ax = fig.add_axes([1,1,4,4])
        ax.bar(State_name['District name'],State_name['Population'])
        ax.set_title(i + ' District wise Population-2011')
        ax.set_xlabel('District name')
        ax.set_ylabel('Population')
        ax.legend(labels=['Men', 'Women'])
        plt.show()
plot_all_state(All_States)
#plot
fig = plt.figure()
ax = fig.add_axes([1,1,4,4])
ax.bar(df['State'],df['Statewise_population'])
ax.set_title('Statewise Population of India-2011')
ax.set_xlabel('State')
ax.set_ylabel('Population')
#ax.legend(labels=['Men', 'Women'])
plt.show()
