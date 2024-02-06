from pydantic import BaseModel, Field
from datetime import date

class CarIn(BaseModel):
    make: str = Field(..., title='Марка автомобиля', max_length=50)
    model: str = Field(..., title='Модель автомобиля', max_length=50)
    year: int = Field(..., title='Год выпуска')
    owner_id: int = Field(title='ID владельца')

class Car(CarIn):
    id: int