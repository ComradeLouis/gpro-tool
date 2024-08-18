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
        
def create_outputs(trackInfo,officeData,setupAndFuel,carPartWear,totalLoss,bestStrat,testWear,testData):
    
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
    testWear_file = f"{trackInfo['trackName']}_R{officeData['race']}_testWear.json"
    testWear_path = f'output/rawData/S{officeData['season']}_testWear'
    write_json(testWear_path,testWear_file,testWear)
    testData_file = f"{trackInfo['trackName']}_R{officeData['race']}_testData.json"
    testData_path = f'output/rawData/S{officeData['season']}_testData'
    write_json(testData_path,testData_file,testData)
    
    allData = {'1':setupAndFuel,'2':bestStrat,'3':carPartWear,'4':testWear,'5':testData}
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
    strategy = pd.DataFrame(data['2'])
    strategy.index = strategy.index + 1
    raceWear = pd.DataFrame(data['3']['Track Wear'])
    endOfRaceWear = pd.DataFrame(data['3']['End of Race Wear'])
    testingWear = pd.DataFrame(data['4'])
    testingData = pd.DataFrame(data['5'])
    
    with pd.ExcelWriter(f'{target_path}\{target_file}') as writer:
        Qsetup.to_excel(writer,sheet_name="Qualy Setup",index=True)
        Rsetup.to_excel(writer,sheet_name="Race Setup",index=True)
        strategy.to_excel(writer,sheet_name="Strategy",index=True)
        for column in strategy:
            column_length = 20
            col_idx = strategy.columns.get_loc(column)
            writer.sheets['Strategy'].set_column(col_idx, col_idx, column_length)
        writer.sheets['Strategy'].set_column(11, 11, column_length)
        raceWear.to_excel(writer,sheet_name="Race Wear",index=True)
        endOfRaceWear.to_excel(writer,sheet_name="End of Race Wear",index=True)
        testingWear.to_excel(writer,sheet_name="Testing Wear",index=True)
        for column in testingWear:
            column_length = 16
            col_idx = testingWear.columns.get_loc(column)
            writer.sheets['Testing Wear'].set_column(col_idx, col_idx, column_length)
        writer.sheets['Testing Wear'].set_column(2, 2, column_length)
        testingData.to_excel(writer,sheet_name="Testing Data",index=True)
        for column in testingData:
            column_length = 13
            col_idx = testingData.columns.get_loc(column)
            writer.sheets['Testing Data'].set_column(col_idx, col_idx, column_length)
        writer.sheets['Testing Data'].set_column(3, 3, column_length)