from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
import os
from data_parser.swimlanes_forprocess_parser import *

#creating routing for the sub_process
router = APIRouter(
    tags=["legend"],
    responses={404: {"description": "Not found"}},
)

#validating the recived input parameters
def validate_params(brands, opus, sites, process):
    #ignoring case by converting to lower case
    dict_sub_keys = [key.lower() for key in dict_sub.keys()]
    if brands.lower() == 'alofisel' and opus.lower() == 'biologics' and sites.lower() == 'madrid' and process.lower() in dict_sub_keys:
        return process
    else:
        return False

#feeding file path to get dict with stage and respective swimlanes
file_path = os.path.join("resource", "SwimlanesForProcess.xlsx")  
dict_sub = create_dict_from_excel(file_path)


@router.get("/boards/subprocesses/{brands}/{opus}/{sites}/{process}?boardName=")#"/boards/subprocesses/{brands}/{opus}/{sites}/{process}?boardName="
async def subprocess(brands: str, opus: str, sites: str, process: str, boardName: str = None):
    validate_param_result =  validate_params(brands, opus, sites, process)
    if validate_param_result != False:
        response_data = {"subprocesses": dict_sub[validate_param_result.upper()]}
        #jsonifying response
        return JSONResponse(content=response_data)
    else:
        return {"status": "error", "message": "Invalid parameters"}
