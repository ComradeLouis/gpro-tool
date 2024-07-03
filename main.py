from getData import *
from staticData import *
from calculationEngine import *
from createFiles import *

trackInfo = get_next_track()
driverInfo = get_driver_info()
carData,weather = get_qualy_and_race_data()
trackData,partData,fuelData = lookup_static_data(trackInfo['trackName'])
officeData = get_office_data()

setup = (calculate_setup(driverInfo,carData,weather,trackData,partData))
fuelRequired,tyreLife = (find_fuel_and_tyre_usage(fuelData,carData,trackInfo,weather,officeData))
setupAndFuel = {'setup': setup, 'fuel': fuelRequired, 'tyres': tyreLife}
setup_file = f"{trackInfo['trackName']}_R{officeData['race']}_setup.json"
setup_path = f'S{officeData['season']}_setups'
write_json(setup_path,setup_file,setupAndFuel)