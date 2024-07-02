import json

def lookup_static_data(track):
    trackFile = open('trackData.json')
    staticTrackData = json.load(trackFile)
    trackDataInput = f'{track}'
    trackData = staticTrackData[trackDataInput]
    partDataFile = open('partData.json')
    partData = json.load(partDataFile)    
    fuelFile = open('fuelData.json')
    staticfuelData = json.load(fuelFile)
    fuelData = staticfuelData[trackDataInput]

    return trackData,partData,fuelData

def lookup_tyre_suppliers(tyreId):
    
    tyreSuppliers = {
        '1': 'Pipirelli',
        '9': 'Avonn',
        '2': 'Yokomama',
        '3': 'Dunnolop',
        '8': 'Contimental',
        '4': 'Badyear',
        '7': 'Hancock',
        '5': 'Michelini',
        '6': 'Bridgerock'
    }
    tyreSupplier = tyreSuppliers[f'{tyreId}']
    
    return tyreSupplier