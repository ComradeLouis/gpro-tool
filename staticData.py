import json

def lookup_static_data(track):
    trackFile = open('dataFiles/trackData.json')
    staticTrackData = json.load(trackFile)
    trackDataInput = f'{track}'
    trackData = staticTrackData[trackDataInput]
    partDataFile = open('dataFiles/partData.json')
    partData = json.load(partDataFile)    
    fuelFile = open('dataFiles/fuelData.json')
    staticfuelData = json.load(fuelFile)
    fuelData = staticfuelData[trackDataInput]

    return trackData,partData,fuelData

def lookup_tyre_data(tyreId):
    
    tyreFile = open('dataFiles/tyreSupplierData.json')
    tyreSuppliers = json.load(tyreFile)
    tyreData = tyreSuppliers[f'{tyreId}']
    
    return tyreData

def lookup_tyre_life(tyreDurability):
    
    durabilityFile = open('dataFiles/tyreDurabilityData.json')
    durabilityData = json.load(durabilityFile)
    tyreDurabilityData = durabilityData[f'{tyreDurability}']
    
    return tyreDurabilityData

def lookup_wear_coeffs(trackWear,raceTemp,raceHumidity,tyre):
    tempFile = open('dataFiles/tempData.json')
    tempData = json.load(tempFile)
    trackData = {
        'Very Low':'1.085',
        'Low':'0.914',
        'Medium':'0.816',
        'High':'0.745',
        'Very High':'0.665'
    }
    humFile = open('dataFiles/humData.json')
    humData = json.load(humFile)
    ctData = {
        'hard':'0.004',
        'rain':'0.004',
        'medium':'0.003',
        'soft':'0.0021',
        'xsoft':'0.0012'
    }
    
    tempCoeff = float(tempData[f'{raceTemp}'])
    trackCoeff = float(trackData[f'{trackWear}'])
    humCoeff = float(humData[f'{raceHumidity}'])
    ctCoeff = float(ctData[f'{tyre}'])
    
    return tempCoeff,trackCoeff,humCoeff,ctCoeff

def lookup_car_wear_coeffs(track):
    carFile = open('dataFiles/trackWearData.json')
    wearData = json.load(carFile)
    
    trackWear = wearData[f'{track}']
    
    return trackWear