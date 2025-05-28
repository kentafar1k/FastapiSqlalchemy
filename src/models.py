from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class WorkersOrm(Base):
    __tablename__ = 'workers'


    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]




























metadata_obj = MetaData()  # хранит данные о всех таблицах этого приложения


workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String),
)

