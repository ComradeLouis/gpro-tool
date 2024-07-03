import math
from staticData import lookup_tyre_life, lookup_wear_coeffs

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

   
        if weather[sessionWeather] == 'Wet':
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
    tyreDurability = officeData['tyreData']['durability']
    tyreDurabilityData = lookup_tyre_life(tyreDurability)
    tyreLife = []
    tyreCompoundLife = []
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
# todo - function to calculate first three coeffs - decision on CT coeff neede:
# =
# *LOOKUP(F9,TyreData!H21:H25,TyreData!I21:I25) TRACK COEFF
# *LOOKUP(B3,TyreData!D28:D78,TyreData!E28:E78) TEMP COEFF
# *LOOKUP(B4,TyreData!H28:H128,TyreData!I28:I128) HUM COEFF
# *(1-I9*LOOKUP(G9,TyreData!D21:D24,TyreData!E21:E24))))) CT COEFF
#
# iterate the above based on all tyre types, and return kms till 100%.
    
    return fuelReq,tyreLife