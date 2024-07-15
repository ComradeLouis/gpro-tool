import os, json

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
    setup_path = f'output/S{officeData['season']}_setups'
    write_json(setup_path,setup_file,setupAndFuel)
    wear_file = f"{trackInfo['trackName']}_R{officeData['race']}_wear.json"
    wear_path = f'output/S{officeData['season']}_wear'
    write_json(wear_path,wear_file,carPartWear)
    loss_file = f"{trackInfo['trackName']}_R{officeData['race']}_loss.json"
    loss_path = f'output/S{officeData['season']}_loss'
    write_json(loss_path,loss_file,totalLoss)
    beststrat_file = f"{trackInfo['trackName']}_R{officeData['race']}_idealstrat.json"
    beststrat_path = f'output/S{officeData['season']}_strat'
    write_json(beststrat_path,beststrat_file,bestStrat)
    strat_file = f"{trackInfo['trackName']}_R{officeData['race']}_allstrat.json"
    strat_path = f'output/S{officeData['season']}_strat/S{officeData['season']}_allstrat'
    write_json(strat_path,strat_file,stratLoss)