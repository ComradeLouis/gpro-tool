from getData import *

trackInfo = get_next_track()
driverInfo = get_driver_info()
carData,weather = get_qualy_and_race_data()

print(trackInfo)
print(driverInfo)
print(carData)
print(weather)