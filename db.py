from sqlalchemy import Table, Column, Integer, String, Date, ForeignKey, MetaData
import databases
import sqlalchemy
from settings import settings
from os import environ

metadata = MetaData()

clients = Table(
    "clients",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("document", String(50), nullable=False),
    Column("surname", String(30), nullable=False),
    Column("firstname", String(30), nullable=False),
    Column("patronymic", String(30), nullable=True),
    Column("birthday", Date, nullable=False),
    Column("phone", String(12), nullable=False),
    Column("email", String(50), unique=True, nullable=False),
)

cars = Table(
    "cars",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("make", String(50), nullable=False),
    Column("model", String(50), nullable=False),
    Column("year", Integer, nullable=False),
    Column("owner_id", ForeignKey("clients.id"), nullable=False),
)

services = Table(
    "services",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("service_date", Date, nullable=False),
    Column("client_id", ForeignKey("clients.id"), nullable=False),
    Column("car_id", ForeignKey("cars.id"), nullable=False),
    Column("description", String(300), nullable=False),
)

TESTING = environ.get("TESTING")

if TESTING:
    TEST_DATABASE_URL = settings.TEST_DATABASE_URL
    database = databases.Database(TEST_DATABASE_URL)
    engine = sqlalchemy.create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
else:
    DATABASE_URL = settings.DATABASE_URL
    database = databases.Database(DATABASE_URL)
    engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

metadata.create_all(engine)