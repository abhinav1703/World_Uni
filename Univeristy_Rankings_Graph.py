import pandas as pd
import matplotlib.pyplot as plt

times_data = pd.read_csv('timesData.csv', delimiter=",")
shanghai_data = pd.read_csv('shanghaiData.csv', delimiter=",")
center_world_data = pd.read_csv('cwurData.csv', delimiter=",")

University_Name = 'Massachusetts Institute of Technology'
university_times=[]
for i in range(len(times_data)):
    if times_data['university_name'][i]==University_Name:
        university_times.append(times_data.iloc[i])

university_shanghai=[]
for i in range(len(shanghai_data)):
    if shanghai_data['university_name'][i]==University_Name:
        university_shanghai.append(shanghai_data.iloc[i])

university_center_world=[]
for i in range(len(center_world_data)):
    if center_world_data['institution'][i]==University_Name:
        university_center_world.append(center_world_data.iloc[i])

y_times, y_shanghai, y_center_world = [],[],[]
for i in range(len(university_times)):
    y_times.append(university_times[i][0])
for i in range(len(university_shanghai)):
    y_shanghai.append(university_shanghai[i][0])
for i in range(len(university_center_world)):
    y_center_world.append(university_center_world[i][0])

x_times, x_shanghai, x_center_world = [],[],[]
for i in range(len(university_times)):
    x_times.append(university_times[i][-1])
for i in range(len(university_shanghai)):
    x_shanghai.append(university_shanghai[i][-1])
for i in range(len(university_center_world)):
    x_center_world.append(university_center_world[i][-1])

plt.plot(x_times,y_times,'r',label='Times Higher Education World University Rankings')
plt.plot(x_shanghai,y_shanghai,'g',label='Shanghai Rankings')
plt.plot(x_center_world,y_center_world,'b',label='Center for World University Rankings')
plt.legend(loc='lower left',prop={'size':10})
plt.gca().invert_yaxis()
plt.title(University_Name+' Rankings Over Time')
plt.show()
