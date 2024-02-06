from pydantic import BaseModel, Field
from datetime import date

class ServiceIn(BaseModel):
    service_date: date = Field(..., title='Дата обслуживания')
    client_id: int = Field(title='ID клиента')
    car_id: int = Field(title='ID автомобиля')
    description: str = Field(default='', title="Описание", max_length=300)

class Service(ServiceIn):
    id: int