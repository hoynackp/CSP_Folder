import matplotlib.pyplot as plt

path = 'data_files/weather.csv'

date_list = []
actual_mean = []
actual_min = []
actual_max = []
actual_precip = []
record_min = []
record_max = []
days = 0
with open(path) as f:
    data = (f.read()).split('\n')
for line in data[1:]:
    vals = line.split(',')
    date_list.append(days)
    actual_mean.append(int(vals[1]))
    actual_min.append(int(vals[2]))
    actual_max.append(int(vals[3]))
    actual_precip.append(float(vals[10]))
    record_min.append(float(vals[6]))
    record_max.append(float(vals[7]))
    days += 1

fig, graph = plt.subplots(2,3)
graph[0][0].plot(date_list, actual_mean, color='blue')
graph[0][1].plot(date_list, actual_min, color='yellow')
graph[0][2].plot(date_list, actual_max, color='orange')
graph[1][0].plot(date_list, actual_precip, color='purple')
graph[1][1].plot(date_list, record_min, color='red')
graph[1][2].plot(date_list, record_max, color='green')
graph[1][0].set(ylabel='Inches')
plt.xlabel('Days since July 1')
plt.ylabel('Temperature')
plt.suptitle('Weather')
plt.show()