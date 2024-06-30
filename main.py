from getData import *
from staticData import *

trackInfo = get_next_track()
driverInfo = get_driver_info()
carData,weather = get_qualy_and_race_data()
trackData,partData = static_data_lookup(trackInfo['trackName'])
