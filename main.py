import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from starlette import status
from starlette.responses import RedirectResponse
from db import database
from controllers import client, car, service

app = FastAPI(openapi_url="/api/v1/openapi.json")


def auto_shop_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="AutoShopAPI",
        version="1.0.0",
        description="Учебный проект по созданию API для веб-сервиса Ателье для автомобилей с использованием "
                    "фреймворка FastAPI (Python) и SQLAlchemy (ORM)",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = auto_shop_openapi


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(client.router, tags=["Клиенты"])
app.include_router(car.router, tags=["Автомобили"])
app.include_router(service.router, tags=["Услуги"])


@app.get("/")
async def root():
    return RedirectResponse(url="/docs", status_code=status.HTTP_302_FOUND)


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)