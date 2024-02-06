from fastapi import APIRouter, HTTPException
from db import services, database
from models.service import ServiceIn, Service

router = APIRouter()


@router.get("/services/", description='get_all_services', operation_id='ServiceGetAll',
            response_model=list[Service])
async def get_services():
    query = services.select()
    return await database.fetch_all(query)


@router.get("/services/{service_id}", description='get_service', operation_id='ServiceGet',
            response_model=Service)
async def get_service(service_id: int):
    query = services.select().where(services.c.id == service_id)
    fetch = await database.fetch_one(query)
    if not fetch:
        raise HTTPException(status_code=404, detail='Услуга не найдена!')
    return fetch


@router.post("/services/", description='add_service', operation_id='ServiceAdd',
             response_model=Service)
async def add_service(service: ServiceIn):
    query = services.insert().values(service_date=service.service_date,
                                     client_id=service.client_id,
                                     car_id=service.car_id,
                                     description=service.description)
    last_record_id = await database.execute(query)
    return {**service.dict(), "id": last_record_id}


@router.put("/services/{service_id}", description='update_service', operation_id='ServiceUpdate',
            response_model=Service)
async def update_service(service_id: int, new_service: ServiceIn):
    query = services.update().where(services.c.id == service_id).values(**new_service.dict())
    fetch = await database.execute(query)
    if not fetch:
        raise HTTPException(status_code=404, detail='Услуга не найдена!')
    return {**new_service.dict(), "id": service_id}


@router.delete("/services/{service_id}", description='delete_service', operation_id='ServiceDelete')
async def delete_service(service_id: int):
    query = services.delete().where(services.c.id == service_id)
    fetch = await database.execute(query)
    if not fetch:
        raise HTTPException(status_code=404, detail='Услуга не найдена!')
    return {'message': 'Услуга была удалена'}