import requests

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
    carPower = raceData['carPower']
    carAccel = raceData['carAccel']
    carHandl = raceData['carHandl']
    lvlChassis = raceData['lvlChassis']
    usaChassis = raceData['usaChassis']
    lvlBrakes = raceData['lvlBrakes']
    usaBrakes = raceData['usaBrakes']
    lvlCooling = raceData['lvlCooling']
    usaCooling = raceData['usaCooling']
    lvlElectronics = raceData['lvlElectronics']
    usaElectronics = raceData['usaElectronics']
    lvlEngine = raceData['lvlEngine']
    usaEngine = raceData['usaEngine']
    lvlFWing = raceData['lvlFWing']
    usaFWing = raceData['usaFWing']
    lvlRWing = raceData['lvlRWing']
    usaRWing = raceData['usaRWing']
    lvlGear = raceData['lvlGear']
    usaGear = raceData['usaGear']
    lvlSidepods = raceData['lvlSidepods']
    usaSidepods = raceData['usaSidepods']
    lvlSusp = raceData['lvlSusp']
    usaSusp = raceData['usaSusp']
    lvlUnderbody = raceData['lvlUnderbody']
    usaUnderbody = raceData['usaUnderbody']
    
    carValues = {"carPower":carPower,"carAccel":carAccel,"carHandling":carHandl}
    partLevels = {"chassis":lvlChassis,"brakes":lvlBrakes,"cooling":lvlCooling,"electronics":lvlElectronics,"engine":lvlEngine,"FWing":lvlFWing,"RWing":lvlRWing,"gear":lvlGear,"sidepods":lvlSidepods,"susp":lvlSusp,"underbody":lvlUnderbody}
    partWear = {"chassis":usaChassis,"brakes":usaBrakes,"cooling":usaCooling,"electronics":usaElectronics,"engine":usaEngine,"FWing":usaFWing,"RWing":usaRWing,"gear":usaGear,"sidepods":usaSidepods,"susp":usaSusp,"underbody":usaUnderbody}
    
    carData = {"carValues":carValues,"carPartLevels":partLevels,"carPartWear":partWear}
    
    return carData,weather

token = "eyJ0eXAiOiJKV1QiLCAiYWxnIjoiSFMyNTYifQ.eyJpZCI6IDEwNDM4OTIsImNyZWF0ZWQiOiJTYXQgSnVuIDI5IDIzOjIxOjMxIFVUQyswMjAwIDIwMjQifQ.Wqt-mFt01J8FEVRwNB12JIQ8vNLe0Mx_eSXK2nXFy_0"
path = "https://gpro.net/gb/backend/api/v2/"