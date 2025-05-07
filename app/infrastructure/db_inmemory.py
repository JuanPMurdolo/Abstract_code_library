import uuid
from typing import Dict, List
from domain.repositories import AbstractRepository

class InMemoryRepository(AbstractRepository):
    def __init__(self):
        self.data: Dict[str, Dict[str, dict]] = {}

    def create(self, entity_name: str, data: dict) -> dict:
        item_id = str(uuid.uuid4())
        data["id"] = item_id
        self.data.setdefault(entity_name, {})[item_id] = data
        return data

    def get(self, entity_name: str, item_id: str) -> dict:
        return self.data[entity_name][item_id]

    def list(self, entity_name: str) -> List[dict]:
        return list(self.data.get(entity_name, {}).values())

    def update(self, entity_name: str, item_id: str, data: dict) -> dict:
        self.data[entity_name][item_id].update(data)
        return self.data[entity_name][item_id]

    def delete(self, entity_name: str, item_id: str) -> None:
        del self.data[entity_name][item_id]
