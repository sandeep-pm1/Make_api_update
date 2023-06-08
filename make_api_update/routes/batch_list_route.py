from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from data_parser.excel_loader_updated import get_model
from data_parser.excel_loader import get_main_list

router = APIRouter(
    tags=["batch-list"],
    responses={404: {"description": "Not found"}},
)


@router.get("/make/batch-list")
async def get_batch_list():
   
    main_list = get_main_list()
    return JSONResponse(content = get_model(main_list))