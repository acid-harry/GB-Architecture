from fastapi import APIRouter, HTTPException
from db import cars, database
from models.car import CarIn, Car

router = APIRouter()


@router.get("/cars/", description='get_all_cars', operation_id='CarGetAll', response_model=list[Car])
async def get_cars():
    query = cars.select()
    return await database.fetch_all(query)


@router.get("/cars/{car_id}", description='get_car', operation_id='CarGet', response_model=Car)
async def get_car(car_id: int):
    query = cars.select().where(cars.c.id == car_id)
    fetch = await database.fetch_one(query)
    if not fetch:
        raise HTTPException(status_code=404, detail='Автомобиль не найден!')
    return fetch


@router.post("/cars/", description='add_car', operation_id='CarAdd', response_model=Car)
async def add_car(car: CarIn):
    query = cars.insert().values(make=car.make,
                                 model=car.model,
                                 year=car.year,
                                 owner_id=car.owner_id)
    last_record_id = await database.execute(query)
    return {**car.model_dump(), "id": last_record_id}


@router.put("/cars/{car_id}", description='update_car', operation_id='CarUpdate', response_model=Car)
async def update_car(car_id: int, new_car: CarIn):
    query = cars.update().where(cars.c.id == car_id).values(**new_car.model_dump())
    fetch = await database.execute(query)
    if not fetch:
        raise HTTPException(status_code=404, detail='Автомобиль не найден')
    return {**new_car.model_dump(), "id": car_id}


@router.delete("/cars/{car_id}", description='delete_car', operation_id='CarDelete')
async def delete_car(car_id: int):
    query = cars.delete().where(cars.c.id == car_id)
    fetch = await database.execute(query)
    if not fetch:
        raise HTTPException(status_code=404, detail='Автомобиль не найден')
    return {'message': 'Автомобиль удален'}