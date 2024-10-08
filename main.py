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
totalWear = calculate_part_wear(trackInfo,driverInfo,carData)
totalLoss,raceTCD = calculate_time_loss(trackInfo,weather,fuelRequired)
sortedBestStrategies = calculate_best_strategy(fuelRequired,tyreLife,trackInfo,weather,fuelPerLap)

#get testing data
testingTrackInfo = get_testing_data()
testWear, testData = calculate_test_wear(testingTrackInfo,driverInfo,carData,fuelData,officeData)

#write output files
create_outputs(trackInfo,officeData,setupAndFuel,totalWear,totalLoss,sortedBestStrategies,testWear,testData)
print(f'Requests remaining this race: {testingTrackInfo['reqRemaining']}')