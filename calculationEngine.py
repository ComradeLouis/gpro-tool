import math
from staticData import *

def calculate_setup(driverInfo,carData,weather,trackData,partData):
    
    sessions = ['q1','q2']
    qualifyingSetup = []
    
    for i in sessions:
        
        session = f'{i}Temp'
        sessionWeather = f'{i}Weather'
        setup_offset_wings = (partData['wings'][0]*weather[session])+(partData['wings'][1]*carData['carPartWear']['FWing'])+(partData['wings'][2]*driverInfo['talent'])+(partData['wings'][3]*((carData['carPartLevels']['FWing']+carData['carPartLevels']['RWing'])/2))+(partData['wings'][4]*carData['carPartLevels']['chassis'])+(partData['wings'][5]*carData['carPartLevels']['underbody'])
        setup_offset_engine = (partData['engine'][0]*weather[session])+(partData['engine'][1]*carData['carPartWear']['engine'])+(partData['engine'][2]*driverInfo['aggressiveness'])+(partData['engine'][3]*driverInfo['experience'])+(partData['engine'][4]*carData['carPartLevels']['engine'])+(partData['engine'][5]*carData['carPartLevels']['cooling'])
        setup_offset_brakes = (partData['brakes'][0]*weather[session])+(partData['brakes'][1]*carData['carPartWear']['brakes'])+(partData['brakes'][2]*driverInfo['talent'])+(partData['brakes'][3]*carData['carPartLevels']['brakes'])+(partData['brakes'][4]*carData['carPartLevels']['electronics'])
        setup_offset_gear = (partData['gear'][0]*weather[session])+(partData['gear'][1]*carData['carPartWear']['gear'])+(partData['gear'][2]*driverInfo['concentration'])+(partData['gear'][3]*carData['carPartLevels']['gear'])+(partData['gear'][4]*carData['carPartLevels']['electronics'])
        setup_offset_susp = (partData['susp'][0]*weather[session])+(partData['susp'][1]*carData['carPartWear']['susp'])+(partData['susp'][2]*driverInfo['experience'])+(partData['susp'][3]*driverInfo['weight'])+(partData['susp'][4]*carData['carPartLevels']['susp'])+(partData['susp'][5]*carData['carPartLevels']['chassis'])+(partData['susp'][6]*carData['carPartLevels']['underbody'])

   
        if weather[sessionWeather] == 'Rain':
            setup_offset_wings = setup_offset_wings + (partData['wings'][6]*weather[session]) + partData['wings'][7]
            setup_offset_engine = setup_offset_engine + (partData['engine'][6]*weather[session]) + partData['engine'][7]
            setup_offset_brakes = setup_offset_brakes + (partData['brakes'][5]*weather[session]) + partData['brakes'][6]
            setup_offset_gear = setup_offset_gear + (partData['gear'][5]*weather[session]) + partData['gear'][6]
            setup_offset_susp = setup_offset_susp + (partData['susp'][7]*weather[session]) + partData['susp'][8]
    
        Qsetup = {
            'wings': math.ceil(trackData['wings']+setup_offset_wings),
            'engine': math.ceil(trackData['engine']+setup_offset_engine),
            'brakes': math.ceil(trackData['brakes']+setup_offset_brakes),
            'gear': math.ceil(trackData['gear']+setup_offset_gear),
            'susp': math.ceil(trackData['susp']+setup_offset_susp)
        }
        
        qualifyingSetup.append(Qsetup)
    
    Q1_setup = qualifyingSetup[0]
    Q2_setup = qualifyingSetup[1]
    
    qualySetup = {
        'Q1': Q1_setup,
        'Q2': Q2_setup
    }
    
    raceTemp = (float(weather['raceQ1TempLow']+weather['raceQ1TempHigh']+weather['raceQ3TempLow']+weather['raceQ2TempHigh']+weather['raceQ4TempLow']+weather['raceQ4TempHigh'])/6)
    wetPercent = (float(weather['raceQ1RainPLow']+weather['raceQ1RainPHigh']+weather['raceQ3RainPLow']+weather['raceQ2RainPHigh']+weather['raceQ4RainPLow']+weather['raceQ4RainPHigh'])/6)
    
    setup_offset_wings = (partData['wings'][0]*raceTemp)+(partData['wings'][1]*carData['carPartWear']['FWing'])+(partData['wings'][2]*driverInfo['talent'])+(partData['wings'][3]*((carData['carPartLevels']['FWing']+carData['carPartLevels']['RWing'])/2))+(partData['wings'][4]*carData['carPartLevels']['chassis'])+(partData['wings'][5]*carData['carPartLevels']['underbody'])
    setup_offset_engine = (partData['engine'][0]*raceTemp)+(partData['engine'][1]*carData['carPartWear']['engine'])+(partData['engine'][2]*driverInfo['aggressiveness'])+(partData['engine'][3]*driverInfo['experience'])+(partData['engine'][4]*carData['carPartLevels']['engine'])+(partData['engine'][5]*carData['carPartLevels']['cooling'])
    setup_offset_brakes = (partData['brakes'][0]*raceTemp)+(partData['brakes'][1]*carData['carPartWear']['brakes'])+(partData['brakes'][2]*driverInfo['talent'])+(partData['brakes'][3]*carData['carPartLevels']['brakes'])+(partData['brakes'][4]*carData['carPartLevels']['electronics'])
    setup_offset_gear = (partData['gear'][0]*raceTemp)+(partData['gear'][1]*carData['carPartWear']['gear'])+(partData['gear'][2]*driverInfo['concentration'])+(partData['gear'][3]*carData['carPartLevels']['gear'])+(partData['gear'][4]*carData['carPartLevels']['electronics'])
    setup_offset_susp = (partData['susp'][0]*raceTemp)+(partData['susp'][1]*carData['carPartWear']['susp'])+(partData['susp'][2]*driverInfo['experience'])+(partData['susp'][3]*driverInfo['weight'])+(partData['susp'][4]*carData['carPartLevels']['susp'])+(partData['susp'][5]*carData['carPartLevels']['chassis'])+(partData['susp'][6]*carData['carPartLevels']['underbody'])
    
    Race_setup_dry = {
        'wings': math.ceil(trackData['wings']+setup_offset_wings),
        'engine': math.ceil(trackData['engine']+setup_offset_engine),
        'brakes': math.ceil(trackData['brakes']+setup_offset_brakes),
        'gear': math.ceil(trackData['gear']+setup_offset_gear),
        'susp': math.ceil(trackData['susp']+setup_offset_susp)
    }
   
    setup_offset_wings = setup_offset_wings + (partData['wings'][6]*raceTemp) + partData['wings'][7]
    setup_offset_engine = setup_offset_engine + (partData['engine'][6]*raceTemp) + partData['engine'][7]
    setup_offset_brakes = setup_offset_brakes + (partData['brakes'][5]*raceTemp) + partData['brakes'][6]
    setup_offset_gear = setup_offset_gear + (partData['gear'][5]*raceTemp) + partData['gear'][6]
    setup_offset_susp = setup_offset_susp + (partData['susp'][7]*raceTemp) + partData['susp'][8]
    
    Race_setup_wet = {
        'wings': math.ceil(trackData['wings']+setup_offset_wings),
        'engine': math.ceil(trackData['engine']+setup_offset_engine),
        'brakes': math.ceil(trackData['brakes']+setup_offset_brakes),
        'gear': math.ceil(trackData['gear']+setup_offset_gear),
        'susp': math.ceil(trackData['susp']+setup_offset_susp)
    }
    
    raceSetup = {
        'Dry Race': Race_setup_dry,
        'Rain Chance': wetPercent,
        'Wet Race': Race_setup_wet
    }
    
    setup = {
        'Qualy': qualySetup,
        'Race': raceSetup
    }
    
    return setup

def find_fuel_and_tyre_usage(fuelData,carData,trackInfo,weather,officeData):
    engineLvl = str(int(carData['carPartLevels']['engine']))
    fuelCoeff = float(fuelData[engineLvl])
    fuelConsumption = fuelCoeff*1.05
    fuelReq = math.ceil(fuelConsumption * trackInfo['raceDistance'])
    fuelReqPerLap = fuelReq/trackInfo['laps']
    tyreDurability = officeData['tyreData']['durability']
    tyreDurabilityData = lookup_tyre_life(tyreDurability)
    tyreLife = []
    tyres = ['xsoft','soft','medium','hard','rain']
    raceTemp = math.ceil((weather['raceQ1TempLow']+weather['raceQ1TempHigh']+weather['raceQ3TempLow']+weather['raceQ2TempHigh']+weather['raceQ4TempLow']+weather['raceQ4TempHigh'])/6)
    raceHumidity = math.ceil((weather['raceQ1HumLow']+weather['raceQ1HumHigh']+weather['raceQ3HumLow']+weather['raceQ2HumHigh']+weather['raceQ4HumLow']+weather['raceQ4HumHigh'])/6)
    trackWear = trackInfo['tyreWear']
    CTRisk = ['0','10','20','30','40','50','60','70','80','90','100']
    CTTyreLife = {}
    
    for CT in CTRisk:
        calcTyreLife = {}
        for tyre in tyres:
            baseTyreLife = float(tyreDurabilityData[tyre])       
            trackCoeff,tempCoeff,humCoeff,ctCoeff = lookup_wear_coeffs(trackWear,raceTemp,raceHumidity,tyre)
            wearCoeff = trackCoeff*tempCoeff*humCoeff*(1-(int(CT)*ctCoeff))
            maxTyreLife = math.floor(baseTyreLife*wearCoeff)
            calcTyreLife[f'{tyre}'] = maxTyreLife
        CTTyreLife[f'{CT}'] = calcTyreLife 
        tyreLife = CTTyreLife
    
    return fuelReq,fuelReqPerLap,tyreLife

def calculate_part_wear(trackInfo,driverInfo,carInfo):
    
    trackWearData = lookup_car_wear_coeffs(trackInfo['trackName'])
    CTRisk = ['0','10','20','30','40','50','60','70','80','90','100']
    partWear = []
    CTPartWear = {}
    
    
    for CT in CTRisk:
        calcPartWear = {}
        for part in trackWearData:
            partLevel = float(carInfo['carPartLevels'][f'{part}'])
            partCoeff = (1145*partLevel**0 - 2125.6369047224*partLevel**1 + 1957.20783726254*partLevel**2 - 1010.67708331277*partLevel**3 + 311.290798604758*partLevel**4 - 58.2916666654791*partLevel**5 + 6.49131944431256*partLevel**6 - 0.394345238087242*partLevel**7 + 0.0100446428569394*partLevel**8)/10000
            trackCoeff = trackWearData[f'{part}']
            driverCoeff = (1+(driverInfo['concentration']*0.0008))*(1+(driverInfo['talent']*0.0004))*(1+(driverInfo['experience']*0.0006))*(1+(driverInfo['stamina']*0.0002))
            aggCoeff = (1+(driverInfo['aggressiveness']*0.0006))
            CTCoeff = 1 + (float(CT)*partCoeff)
            partWear = math.ceil((trackCoeff*aggCoeff*CTCoeff)/driverCoeff)
            calcPartWear[f'{part}'] = partWear
        CTPartWear[f'{CT}'] = calcPartWear
        partWear = CTPartWear
    
    return partWear

def calculate_TCD(track,weather):
    
    k = lookup_k_value(track)
    Q1Temp = weather['q1Temp']
    Q2Temp = weather['q2Temp']
    raceTemp = math.ceil((weather['raceQ1TempLow']+weather['raceQ1TempHigh']+weather['raceQ3TempLow']+weather['raceQ2TempHigh']+weather['raceQ4TempLow']+weather['raceQ4TempHigh'])/6)
    
    temps = [Q1Temp,Q2Temp,raceTemp]
    TCDSession = []
    
    for temp in temps:
        calcTCD = (50-float(temp))*k
        TCDSession.append(calcTCD)
        
    Q1TCD = TCDSession[0]
    Q2TCD = TCDSession[1]
    raceTCD = TCDSession[2]
    
    TCD = {
        'Q1':Q1TCD,
        'Q2':Q2TCD,
        'Race':raceTCD
    }
    
    return TCD

def calculate_time_loss(trackInfo,weather,fuelRequired):
    
    TCD = calculate_TCD(trackInfo['trackName'],weather)
    raceTCD = TCD['Race']
    lapLength = trackInfo['raceDistance']/float(trackInfo['laps'])
    lapLossCoeff = lapLength*0.0041181841
    tyreLoss = {}
    tyreTyreLoss = {}
    fuelLoss = {}
    fuelCalcLoss = {}
    stopLoss = {}
    stopCalcLoss = {}
    
    tyreCoeffs = {
        'xsoft':1,
        'soft':2,
        'medium':3,
        'hard':4,
        'rain':4
    }
    
    tyres = ['xsoft','soft','medium','hard','rain']
    
    for tyre in tyres:
        calcTyreLoss = raceTCD*float(tyreCoeffs[f'{tyre}'])*float(trackInfo['laps'])
        if tyre == 'rain':
            calcTyreLoss = raceTCD*float(tyreCoeffs[f'{tyre}']) + 2.718*float(trackInfo['laps'])
        tyreTyreLoss[f'{tyre}'] = calcTyreLoss
        tyreLoss = tyreTyreLoss
    
    stops = [1,2,3,4]
    
    for stop in stops:
        calcFuelLoss = ((lapLossCoeff*fuelRequired)/(1+float(stop)))*((float(trackInfo['laps']))/(1+float(stop))*(1+float(stop)))
        fuelCalcLoss[f'{stop}'] = calcFuelLoss
        fuelLoss = fuelCalcLoss
        calcStopLoss = (float(trackInfo['pitTime'])*float(stop)) + (25*float(stop))
        stopCalcLoss[f'{stop}'] = calcStopLoss
        stopLoss = stopCalcLoss
        
    totalLoss = {
        'tyres': tyreLoss,
        'fuel': fuelLoss,
        'stops': stopLoss
    }
    
    return totalLoss

def calculate_best_strategy(fuelRequired,tyreLife,trackInfo,weather,fuelPerLap):
    
    totalLoss = calculate_time_loss(trackInfo,weather,fuelRequired)
    tyreLoss = totalLoss['tyres']
    fuelLoss = totalLoss['fuel']
    stopLoss = totalLoss['stops']
    raceLaps = float(trackInfo['laps'])
    chosenStopLoss = {}
    stratLoss = []
    
    stops = [1,2,3,4]
    tyres = ['xsoft','soft','medium','hard','rain']
    CTRisk = ['0','10','20','30','40','50','60','70','80','90','100']
    
    for stop in stops:
        chosenCTLoss = {}
        stintLaps = math.ceil(raceLaps/(stop+1))
        stintLength = (stintLaps/raceLaps)*trackInfo['raceDistance']
        calcStopLoss = stopLoss[f'{stop}']
        calcFuelLoss = fuelLoss[f'{stop}']
        for CT in CTRisk:
            chosenTyreLoss = {}
            for tyre in tyres:
                chosenTyreLife = tyreLife[f'{CT}'][f'{tyre}']
                calcTyreLoss = tyreLoss[f'{tyre}']
                calcCTTyreStopLoss = calcTyreLoss + calcFuelLoss + calcStopLoss
                if stintLength > chosenTyreLife:
                    calcCTTyreStopLoss = 1e7
                chosenTyreLoss[f'{tyre}'] = calcCTTyreStopLoss
            chosenCTLoss[f'{CT}'] = chosenTyreLoss
        chosenStopLoss[f'{stop}'] = chosenCTLoss
        stratLoss = chosenStopLoss
   
    timeLoss = 1e7
    reversedCTRisk = CTRisk[::-1]
    
    for stop in stops:
       stintLaps = math.ceil(raceLaps/(stop+1))
       stintFuel = math.ceil(stintLaps*fuelPerLap)
       for CT in reversedCTRisk:
           for tyre in tyres:
               stratTimeLoss = stratLoss[f'{stop}'][f'{CT}'][f'{tyre}']
               if stratTimeLoss < timeLoss:
                   timeLoss = stratTimeLoss
                   bestStrat = {'Time':timeLoss,'Stops':stop,'CT':CT,'Tyres':tyre,'Laps per stint':stintLaps,'Fuel per stint':stintFuel}
                
   
    return stratLoss,bestStrat