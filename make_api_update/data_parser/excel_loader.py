from fastapi import HTTPException
import pandas as pd
import json, os

def add(main_list, temp_dict):
    name = temp_dict["name"]
    id = temp_dict["id"]

    if(not bool(main_list)):
        main_list.append(temp_dict)
    else:
        flag_added = False
        for ele in main_list:
            if(ele["name"]==name and ele["id"]==id):
                ele["cardList"].extend(temp_dict["cardList"])
                flag_added=True
                break
        if(not flag_added):
            main_list.append(temp_dict)


def get_main_list():

    main_list = []

    file_path = os.path.join("resource", "Table_Updated.xlsx")
    if(not os.path.isfile(file_path)):
        raise HTTPException(404, detail="Data not Available")
        
    data = pd.read_excel(file_path)

    if data.empty:
        return []

    for index, row in data.iterrows():

        cardList = []

        header = row['lane_header']
        id = row['id']

        batch_number = row['batch']
        brand_name = row['brand']
        manufacture_stage = row['manufacture_stage']
        image_link = 'assets/Images/feiba.png'
        status = row['status']
        event = ['Adhoc', 'Atrisk', 'SDN', 'Tender']

        if batch_number == 'nan':
            cardList.append([])
        else:
            cardList.append({"batchNumber": batch_number, "brandName": brand_name, "manufactureStage":manufacture_stage, "imageLink":image_link, "status": status, "event":event})

        temp_dict = {"name": header, "id":id, "cardList":cardList}
        
        add(main_list, temp_dict)

    return main_list   
