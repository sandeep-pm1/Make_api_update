from fastapi.encoders import jsonable_encoder
from model.batch_list_model import Card, BatchDetail

def get_model(main_list):
    result = []
    for ele in main_list:
        for key, value in ele.items():
            batch_name = ele['name']
            batch_id = ele['id']
            cardList = ele['cardList']

            batch_card_list = []

            for elements in cardList:
                
                batch_number = elements['batchNumber']
                brand_name = elements['brandName']
                manufacture_Stage = elements['manufactureStage']
                image_link = elements['imageLink']
                status_data = elements['status']
                event = elements['event']

                card = Card(
                    batchNumber = batch_number,
                    brandName = brand_name,
                    manufactureStage = manufacture_Stage,
                    imageLink = image_link,
                    status = status_data,
                    events = event
                )
                
                if(str(batch_number)!='nan'):
                    json_compatible_card_data = jsonable_encoder(card)
                    batch_card_list.append(json_compatible_card_data)
            
            batch_details = BatchDetail(
                name = batch_name,
                id = batch_id,
                cardList = batch_card_list
            )

        json_compatible_batch_data = jsonable_encoder(batch_details)
        result.append(json_compatible_batch_data)
        
    return result   
            


