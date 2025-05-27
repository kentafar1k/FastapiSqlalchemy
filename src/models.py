from sqlalchemy import Table, Column, Integer, String, MetaData

metadata_obj = MetaData()  # хранит данные о всех таблицах этого приложения


workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String),
)



