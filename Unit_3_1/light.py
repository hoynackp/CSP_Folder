import matplotlib.pyplot as plt

path = 'data_files/light_sensor.csv'

time_list = []
r_list = []
g_list = []
b_list = []
with open(path) as f:
    data = (f.read()).split('\n')
for line in data[1:]:
    vals = line.split(',')
    time_list.append(float(vals[0]))
    r_list.append(float(vals[1]))
    g_list.append(float(vals[2]))
    b_list.append(float(vals[3]))

fig, graph = plt.subplots(3,1)
graph[0].plot(time_list, r_list, color='red')
graph[1].plot(time_list, g_list, color='green')
graph[2].plot(time_list, b_list, color='blue')
plt.xlabel('Time (Seconds)')
plt.ylabel('Color (nms)')
plt.suptitle('Red, Green, Blue Colors over time')
plt.grid()
plt.show()