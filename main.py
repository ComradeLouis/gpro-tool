from getData import *
from staticData import *
from calculationEngine import *
from createFiles import *

#get data from GPRO API
trackInfo = get_next_track()
driverInfo = get_driver_info()
carData,weather = get_qualy_and_race_data()
trackData,partData,fuelData = lookup_static_data(trackInfo['trackName'])
officeData = get_office_data()

#calculate setup, fuel/tyre usage and part wear
setup = (calculate_setup(driverInfo,carData,weather,trackData,partData))
fuelRequired,fuelPerLap,tyreLife = (find_fuel_and_tyre_usage(fuelData,carData,trackInfo,weather,officeData))
setupAndFuel = {'setup': setup, 'fuel': fuelRequired, 'fuelPerLap': fuelPerLap,'raceDistance': trackInfo['raceDistance'],'tyres': tyreLife}
carPartWear = calculate_part_wear(trackInfo,driverInfo,carData)

#write output json files
setup_file = f"{trackInfo['trackName']}_R{officeData['race']}_setup.json"
setup_path = f'output/S{officeData['season']}_setups'
write_json(setup_path,setup_file,setupAndFuel)
wear_file = f"{trackInfo['trackName']}_R{officeData['race']}_wear.json"
wear_path = f'output/S{officeData['season']}_wear'
write_json(wear_path,wear_file,carPartWear)