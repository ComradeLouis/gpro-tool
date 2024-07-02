import requests
from staticData import lookup_tyre_suppliers
from dotenv import load_dotenv
import os

def get_next_track():
    endpoint = f"{path}TrackProfile"
    headers = {"Authorization": f"Bearer {token}"}
    trackProfile = requests.get(endpoint, headers=headers).json()
    
    trackName = trackProfile['trackName']
    trackPower = trackProfile['power']
    trackAccel = trackProfile['accel']
    trackHandl = trackProfile['handl']
    raceDistance = trackProfile['raceDistance']
    raceLaps = trackProfile['laps']
    pitTime = trackProfile['timeInOutPits']
    
    trackData = {"trackName":trackName,"power":trackPower,"accel":trackAccel,"handling":trackHandl,"raceDistance":float(raceDistance),"laps":raceLaps,"pitTime":pitTime}

    return trackData

def get_driver_info():
    endpoint = f"{path}DriProfile"
    headers = {"Authorization": f"Bearer {token}"}
    driProfile = requests.get(endpoint, headers=headers).json()
    
    concentration = driProfile['concentration']
    talent = driProfile['talent']
    aggro = driProfile['aggressiveness']
    exp = driProfile['experience']
    TI = driProfile['techInsight']
    stam = driProfile['stamina']
    weight = driProfile['weight']
    
    driverData = {"concentration":concentration,"talent":talent,"aggressiveness":aggro,"experience":exp,"techInsight":TI,"stamina":stam,"weight":weight}
    
    return driverData

def get_qualy_and_race_data():
    endpoint = f"{path}Practice"
    headers = {"Authorization": f"Bearer {token}"}
    raceData = requests.get(endpoint, headers=headers).json()
    
    weather = raceData['weather']
    carPower = float(raceData['carPower'])
    carAccel = float(raceData['carAccel'])
    carHandl = float(raceData['carHandl'])
    lvlChassis = float(raceData['lvlChassis'])
    usaChassis = float(raceData['usaChassis'])
    lvlBrakes = float(raceData['lvlBrakes'])
    usaBrakes = float(raceData['usaBrakes'])
    lvlCooling = float(raceData['lvlCooling'])
    usaCooling = float(raceData['usaCooling'])
    lvlElectronics = float(raceData['lvlElectronics'])
    usaElectronics = float(raceData['usaElectronics'])
    lvlEngine = float(raceData['lvlEngine'])
    usaEngine = float(raceData['usaEngine'])
    lvlFWing = float(raceData['lvlFWing'])
    usaFWing = float(raceData['usaFWing'])
    lvlRWing = float(raceData['lvlRWing'])
    usaRWing = float(raceData['usaRWing'])
    lvlGear = float(raceData['lvlGear'])
    usaGear = float(raceData['usaGear'])
    lvlSidepods = float(raceData['lvlSidepods'])
    usaSidepods = float(raceData['usaSidepods'])
    lvlSusp = float(raceData['lvlSusp'])
    usaSusp = float(raceData['usaSusp'])
    lvlUnderbody = float(raceData['lvlUnderbody'])
    usaUnderbody = float(raceData['usaUnderbody'])
    
    carValues = {"carPower":carPower,"carAccel":carAccel,"carHandling":carHandl}
    partLevels = {"chassis":lvlChassis,"brakes":lvlBrakes,"cooling":lvlCooling,"electronics":lvlElectronics,"engine":lvlEngine,"FWing":lvlFWing,"RWing":lvlRWing,"gear":lvlGear,"sidepods":lvlSidepods,"susp":lvlSusp,"underbody":lvlUnderbody}
    partWear = {"chassis":usaChassis,"brakes":usaBrakes,"cooling":usaCooling,"electronics":usaElectronics,"engine":usaEngine,"FWing":usaFWing,"RWing":usaRWing,"gear":usaGear,"sidepods":usaSidepods,"susp":usaSusp,"underbody":usaUnderbody}
    
    carData = {"carValues":carValues,"carPartLevels":partLevels,"carPartWear":partWear}
    
    return carData,weather

def get_office_data():
    endpoint = f"{path}office"
    headers = {"Authorization": f"Bearer {token}"}
    officeData = requests.get(endpoint, headers=headers).json()
    
    tyreSupplierId = officeData['tyreSupplierId']
    
    tyreSupplier = lookup_tyre_suppliers(tyreSupplierId)
    season = officeData['seasonNb']
    race = officeData['raceNb']
    
    officeResponse = {
        'tyreSupplier':tyreSupplier,
        'season':season,
        'race':race
    }
    
    return officeResponse

load_dotenv()
token = os.getenv('token')
path = "https://gpro.net/gb/backend/api/v2/"