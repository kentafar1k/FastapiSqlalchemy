from sqlalchemy import text, insert
from src.database import sync_engine, async_engine
from src.models import metadata_obj, workers_table


def create_tables():
    sync_engine.echo = False
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)
    sync_engine.echo = True


def insert_data():
    with sync_engine.connect() as conn:
        # stmt = '''INSERT INTO workers (username) VALUES
        # ('Bobr'),
        # ('Volk')'''
        stmt = insert(workers_table).values(
            [
                {"username": "Bober"},
                {"username": "Volk"},
            ]
        )
        conn.execute(stmt)
        conn.commit()