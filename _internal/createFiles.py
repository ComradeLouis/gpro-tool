import os, json, pandas as pd

def write_json(target_path, target_file, data):
    if not os.path.exists(target_path):
        try:
            os.makedirs(target_path)
        except Exception as e:
            print(e)
            raise
    with open(os.path.join(target_path, target_file), 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
def create_outputs(trackInfo,officeData,setupAndFuel,carPartWear,totalLoss,bestStrat,stratLoss):
    
    setup_file = f"{trackInfo['trackName']}_R{officeData['race']}_setup.json"
    setup_path = f'output/rawData/S{officeData['season']}_setups'
    write_json(setup_path,setup_file,setupAndFuel)
    wear_file = f"{trackInfo['trackName']}_R{officeData['race']}_wear.json"
    wear_path = f'output/rawData/S{officeData['season']}_wear'
    write_json(wear_path,wear_file,carPartWear)
    loss_file = f"{trackInfo['trackName']}_R{officeData['race']}_loss.json"
    loss_path = f'output/rawData/S{officeData['season']}_loss'
    write_json(loss_path,loss_file,totalLoss)
    beststrat_file = f"{trackInfo['trackName']}_R{officeData['race']}_idealstrat.json"
    beststrat_path = f'output/rawData/S{officeData['season']}_strat'
    write_json(beststrat_path,beststrat_file,bestStrat)
    strat_file = f"{trackInfo['trackName']}_R{officeData['race']}_allstrat.json"
    strat_path = f'output/rawData/S{officeData['season']}_strat/S{officeData['season']}_allstrat'
    write_json(strat_path,strat_file,stratLoss)
    
    allData = {'1':setupAndFuel,'2':bestStrat,'3':carPartWear,'4':stratLoss}
    allData_file = f'{trackInfo['trackName']}_R{officeData['race']}.xlsx'
    allData_path = f'output/S{officeData['season']}'
    write_excel(allData_path,allData_file,allData)

def write_excel(target_path,target_file, data):
    if not os.path.exists(target_path):
        try:
            os.makedirs(target_path)
        except Exception as e:
            print(e)
            raise
    
    Qsetup = pd.DataFrame(data['1']['setup']['Qualy'])
    Rsetup = pd.DataFrame(data['1']['setup']['Race'])
    strategy = pd.DataFrame(data['2'], index=[0])
    raceWear = pd.DataFrame(data['3']['Track Wear'])
    endOfRaceWear = pd.DataFrame(data['3']['End of Race Wear'])
    oneStop = pd.DataFrame(data['4']['1'])
    twoStop = pd.DataFrame(data['4']['2'])
    threeStop = pd.DataFrame(data['4']['3'])
    fourStop = pd.DataFrame(data['4']['4'])
    
    with pd.ExcelWriter(f'{target_path}\{target_file}') as writer:
        Qsetup.to_excel(writer,sheet_name="Qualy Setup",index=True)
        Rsetup.to_excel(writer,sheet_name="Race Setup",index=True)
        strategy.to_excel(writer,sheet_name="Strategy",index=False)
        raceWear.to_excel(writer,sheet_name="Race Wear",index=True)
        endOfRaceWear.to_excel(writer,sheet_name="End of Race Wear",index=True)
        oneStop.to_excel(writer,sheet_name="1 stop strategy",index=True)
        twoStop.to_excel(writer,sheet_name="2 stop strategy",index=True)
        threeStop.to_excel(writer,sheet_name="3 stop strategy",index=True)
        fourStop.to_excel(writer,sheet_name="4 stop strategy",index=True)