from fastapi import APIRouter, Depends, HTTPException
import os
from fastapi.responses import FileResponse
from constants import filename_constants

router = APIRouter(
    tags=["legend"],
    responses={404: {"description": "Not found"}},
)


@router.get("/make/legend")
async def get_legend():
    dir_name = filename_constants.legend_filename
    if(not is_file_exist(dir_name)):
        raise HTTPException(404, detail="Data not Available")
        #return "Data not Available"
    elif is_file_empty(dir_name):
        #raise HTTPException(404, detail="Data not Available")
        return []

    return FileResponse(dir_name)


def is_file_exist(filename):
    return os.path.isfile(filename)

def is_file_empty(filename):
    return os.stat(filename).st_size == 0