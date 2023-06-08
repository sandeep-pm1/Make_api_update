from fastapi import FastAPI, APIRouter
from routes import legend_route, batch_list_route
from config_api import sub_process

app = FastAPI(
    docs_url="/api/v2/docs",
    redoc_url="/api/v2/redocs",
    title="demo application",
    description="this is a demo application",
    version="2.0",
    openapi_url="/api/v2/openapi.json",
)


app.include_router(legend_route.router)
app.include_router(batch_list_route.router)
app.include_router(sub_process.router)