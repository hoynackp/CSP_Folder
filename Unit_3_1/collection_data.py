import gdx
gdx = gdx.gdx()

gdx.open_usb()
gdx.select_sensors([5,6,7])
gdx.start(1000)


for i in range(5):
    measurements = gdx.read()
    if measurements == None: 
        break 
    print(measurements)


gdx.stop()
gdx.close()