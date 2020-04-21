#color_sensor
import tkinter as tk
import random as rand
import gdx
gdx = gdx.gdx()

root = tk.Tk()
root.wm_geometry("1200x600")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black', 'white']

def rand_color():
    color = rand.choice(colors)
    color_label = tk.Label(root, text=('Your color is ' + color)).grid(row=0, column=1)
    canvas = tk.Canvas(root, width=300, height=300, bg=color).grid(row=1, column=1, rowspan=4)

def take_sample():
    gdx.open_usb()
    gdx.select_sensors([5,6,7])
    gdx.start(1000)
    for i in range(2):
        sample = gdx.read()
    red = sample[0]
    blue = sample[1]
    green = sample[2]
    print(sample)
    if 2.8>red>2.4 and .5>blue>.1 and 8.6>green>8.1:
        color_label = tk.Label(root, text='The color captured is: purple').grid(row=5, column=1)

    gdx.stop()
    gdx.close()



direction_label = tk.Label(root, text="Generate a color, then find that color").grid(row=0)
start_button = tk.Button(root, command = rand_color, text='Generate Color').grid(row=1)

sensor_label = tk.Label(root, text='Place sensor near color and click button').grid(row=2)
sensor_button = tk.Button(root, command=take_sample, text="Capture Color").grid(row=3)

color_label = tk.Label(root, text='The color captured is: ').grid(row=5, column=1)

root.mainloop()