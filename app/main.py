from fastapi import FastAPI
from fastapi_pagination import add_pagination
from app.routers import api_router

app = FastAPI(title="Academia API")
app.include_router(api_router)
add_pagination(app)


#if __name__ == "main":
#    import uvicorn

#    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_config='info', reload=True)