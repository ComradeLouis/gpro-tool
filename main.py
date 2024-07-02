from getData import *
from staticData import *
from calculationEngine import *

trackInfo = get_next_track()
driverInfo = get_driver_info()
carData,weather = get_qualy_and_race_data()
trackData,partData = lookup_static_data(trackInfo['trackName'])
officeData = get_office_data()

setup = (calculate_setup(driverInfo,carData,weather,trackData,partData))
setup_file = open(f"{trackInfo['trackName']}_S{officeData['season']}_R{officeData['race']}_setup.json", "w")
