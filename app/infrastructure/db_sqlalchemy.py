from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.domain.repositories import AbstractRepository
from typing import Dict, List
import uuid
import json

DATABASE_URL = "postgresql+asyncpg://user:password@localhost/dbname"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class SQLAlchemyRepository(AbstractRepository):
    def __init__(self):
        self.session_factory = async_session

    async def create(self, entity_name: str, data: dict) -> dict:
        async with self.session_factory() as session:
            item_id = str(uuid.uuid4())
            data["id"] = item_id
            await session.execute(
                f"INSERT INTO {entity_name} (id, data) VALUES (:id, :data)",
                {"id": item_id, "data": json.dumps(data)}
            )
            await session.commit()
            return data

    async def list(self, entity_name: str) -> List[dict]:
        async with self.session_factory() as session:
            result = await session.execute(f"SELECT data FROM {entity_name}")
            rows = result.fetchall()
            return [json.loads(r[0]) for r in rows]

    # implementá `get`, `update`, `delete` igual
    async def get(self, entity_name: str, item_id: str) -> dict:
        async with self.session_factory() as session:
            result = await session.execute(
                f"SELECT data FROM {entity_name} WHERE id = :id",
                {"id": item_id}
            )
            row = result.fetchone()
            return json.loads(row[0]) if row else None
        
    async def update(self, entity_name: str, item_id: str, data: dict) -> dict:
        async with self.session_factory() as session:
            await session.execute(
                f"UPDATE {entity_name} SET data = :data WHERE id = :id",
                {"data": json.dumps(data), "id": item_id}
            )
            await session.commit()
            return data
    
    async def delete(self, entity_name: str, item_id: str) -> None:
        async with self.session_factory() as session:
            await session.execute(
                f"DELETE FROM {entity_name} WHERE id = :id",
                {"id": item_id}
            )
            await session.commit()
    
    async def delete_all(self, entity_name: str) -> None:
        async with self.session_factory() as session:
            await session.execute(f"DELETE FROM {entity_name}")
            await session.commit()
    
    