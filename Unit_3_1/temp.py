import matplotlib.pyplot as plt

path = 'data_files/raw_data_311.csv'

time_list = []
temp1_list = []
temp2_list = []
with open(path) as f:
    data = (f.read()).split('\n')
for line in data[1:]:
    vals = line.split(',')
    time_list.append(int(vals[0])) 
    temp1_list.append(float(vals[1]))
    temp2_list.append(float(vals[2]))
print(time_list)
print(temp1_list)
print(temp2_list)

plt.plot(time_list, temp1_list, color='blue')
plt.plot(time_list, temp2_list, color='red')
plt.xlabel('Time (seconds)')
plt.ylabel('Temperature (Celsius)')
plt.suptitle('Graph')
plt.grid()
plt.show()