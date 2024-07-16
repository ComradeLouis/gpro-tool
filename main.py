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
setupAndFuel = {'setup': setup, 'tyres': tyreLife}
carPartWear = calculate_part_wear(trackInfo,driverInfo,carData)
totalLoss,raceTCD = calculate_time_loss(trackInfo,weather,fuelRequired)
stratLoss,bestStrat = calculate_best_strategy(fuelRequired,tyreLife,trackInfo,weather,fuelPerLap)

#write output json files
create_outputs(trackInfo,officeData,setupAndFuel,carPartWear,totalLoss,bestStrat,stratLoss)