import enum

from sqlalchemy import (
    TIMESTAMP,
    CheckConstraint,
    Column,
    Enum,
    ForeignKey,
    Index,
    Integer,
    MetaData,
    PrimaryKeyConstraint,
    String,
    Table,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class WorkersOrm(Base):
    __tablename__ = 'workers'


    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]

class Workload(enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"


class ResumesOrm(Base):
    __tablename__ = "resumes"

    id: Mapped[intpk]
    title: Mapped[str]
    compensation: Mapped[Optional[int]]
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete="CASCADE"))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]





























metadata_obj = MetaData()  # хранит данные о всех таблицах этого приложения


workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String),
)

