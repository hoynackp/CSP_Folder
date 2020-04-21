import matplotlib.pyplot as plt

path = 'data_files/sound_testing.csv'

time_list = []
sound_c = []
sound_a = []
with open(path) as f:
    data = (f.read()).split('\n')
for line in data[1:]:
    vals = line.split(',')
    time_list.append(float(vals[0]))
    sound_c.append(float(vals[1]))
    sound_a.append(float(vals[2]))

plt.plot(time_list, sound_c, color='blue')
plt.plot(time_list, sound_a, color='red')
plt.xlabel('Time (Seconds)')
plt.ylabel('Decibels')
plt.suptitle('Morse Code Graph')
plt.grid()
plt.show()