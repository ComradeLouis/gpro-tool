import math

def calculate_setup(driverInfo,carData,weather,trackData,partData):
        
    setup_offset_wings = (partData['wings'][0]*weather['q1Temp'])+(partData['wings'][1]*carData['carPartWear']['FWing'])+(partData['wings'][2]*driverInfo['talent'])+(partData['wings'][3]*((carData['carPartLevels']['FWing']+carData['carPartLevels']['RWing'])/2))+(partData['wings'][4]*carData['carPartLevels']['chassis'])+(partData['wings'][5]*carData['carPartLevels']['underbody'])
    setup_offset_engine = (partData['engine'][0]*weather['q1Temp'])+(partData['engine'][1]*carData['carPartWear']['engine'])+(partData['engine'][2]*driverInfo['aggressiveness'])+(partData['engine'][3]*driverInfo['experience'])+(partData['engine'][4]*carData['carPartLevels']['engine'])+(partData['engine'][5]*carData['carPartLevels']['cooling'])
    setup_offset_brakes = (partData['brakes'][0]*weather['q1Temp'])+(partData['brakes'][1]*carData['carPartWear']['brakes'])+(partData['brakes'][2]*driverInfo['talent'])+(partData['brakes'][3]*carData['carPartLevels']['brakes'])+(partData['brakes'][4]*carData['carPartLevels']['electronics'])
    setup_offset_gear = (partData['gear'][0]*weather['q1Temp'])+(partData['gear'][1]*carData['carPartWear']['gear'])+(partData['gear'][2]*driverInfo['concentration'])+(partData['gear'][3]*carData['carPartLevels']['gear'])+(partData['gear'][4]*carData['carPartLevels']['electronics'])
    setup_offset_susp = (partData['susp'][0]*weather['q1Temp'])+(partData['susp'][1]*carData['carPartWear']['susp'])+(partData['susp'][2]*driverInfo['experience'])+(partData['susp'][3]*driverInfo['weight'])+(partData['susp'][4]*carData['carPartLevels']['susp'])+(partData['susp'][5]*carData['carPartLevels']['chassis'])+(partData['susp'][6]*carData['carPartLevels']['underbody'])

   
    if weather['q1Weather'] == 'Wet':
        setup_offset_wings = setup_offset_wings + (partData['wings'][6]*weather['q1Temp']) + partData['wings'][7]
        setup_offset_engine = setup_offset_engine + (partData['engine'][6]*weather['q1Temp']) + partData['engine'][7]
        setup_offset_brakes = setup_offset_brakes + (partData['brakes'][5]*weather['q1Temp']) + partData['brakes'][6]
        setup_offset_gear = setup_offset_gear + (partData['gear'][5]*weather['q1Temp']) + partData['gear'][6]
        setup_offset_susp = setup_offset_susp + (partData['susp'][7]*weather['q1Temp']) + partData['susp'][8]
        
    
    Q1_setup = {
        'wings': math.ceil(trackData['wings']+setup_offset_wings),
        'engine': math.ceil(trackData['engine']+setup_offset_engine),
        'brakes': math.ceil(trackData['brakes']+setup_offset_brakes),
        'gear': math.ceil(trackData['gear']+setup_offset_gear),
        'susp': math.ceil(trackData['susp']+setup_offset_susp)
    }
    
    setup_offset_wings = (partData['wings'][0]*weather['q2Temp'])+(partData['wings'][1]*carData['carPartWear']['FWing'])+(partData['wings'][2]*driverInfo['talent'])+(partData['wings'][3]*((carData['carPartLevels']['FWing']+carData['carPartLevels']['RWing'])/2))+(partData['wings'][4]*carData['carPartLevels']['chassis'])+(partData['wings'][5]*carData['carPartLevels']['underbody'])
    setup_offset_engine = (partData['engine'][0]*weather['q2Temp'])+(partData['engine'][1]*carData['carPartWear']['engine'])+(partData['engine'][2]*driverInfo['aggressiveness'])+(partData['engine'][3]*driverInfo['experience'])+(partData['engine'][4]*carData['carPartLevels']['engine'])+(partData['engine'][5]*carData['carPartLevels']['cooling'])
    setup_offset_brakes = (partData['brakes'][0]*weather['q2Temp'])+(partData['brakes'][1]*carData['carPartWear']['brakes'])+(partData['brakes'][2]*driverInfo['talent'])+(partData['brakes'][3]*carData['carPartLevels']['brakes'])+(partData['brakes'][4]*carData['carPartLevels']['electronics'])
    setup_offset_gear = (partData['gear'][0]*weather['q2Temp'])+(partData['gear'][1]*carData['carPartWear']['gear'])+(partData['gear'][2]*driverInfo['concentration'])+(partData['gear'][3]*carData['carPartLevels']['gear'])+(partData['gear'][4]*carData['carPartLevels']['electronics'])
    setup_offset_susp = (partData['susp'][0]*weather['q2Temp'])+(partData['susp'][1]*carData['carPartWear']['susp'])+(partData['susp'][2]*driverInfo['experience'])+(partData['susp'][3]*driverInfo['weight'])+(partData['susp'][4]*carData['carPartLevels']['susp'])+(partData['susp'][5]*carData['carPartLevels']['chassis'])+(partData['susp'][6]*carData['carPartLevels']['underbody'])

   
    if weather['q2Weather'] == 'Wet':
        setup_offset_wings = setup_offset_wings + (partData['wings'][6]*weather['q2Temp']) + partData['wings'][7]
        setup_offset_engine = setup_offset_engine + (partData['engine'][6]*weather['q2Temp']) + partData['engine'][7]
        setup_offset_brakes = setup_offset_brakes + (partData['brakes'][5]*weather['q2Temp']) + partData['brakes'][6]
        setup_offset_gear = setup_offset_gear + (partData['gear'][5]*weather['q2Temp']) + partData['gear'][6]
        setup_offset_susp = setup_offset_susp + (partData['susp'][7]*weather['q2Temp']) + partData['susp'][8]
        
    
    Q2_setup = {
        'wings': math.ceil(trackData['wings']+setup_offset_wings),
        'engine': math.ceil(trackData['engine']+setup_offset_engine),
        'brakes': math.ceil(trackData['brakes']+setup_offset_brakes),
        'gear': math.ceil(trackData['gear']+setup_offset_gear),
        'susp': math.ceil(trackData['susp']+setup_offset_susp)
    }
    
    setup = {
        'Q1': Q1_setup,
        'Q2': Q2_setup
    }
    
    return setup