from typing import Dict
from app.schemas.entity_schemas import EntityField

class Entity:
    def __init__(self, name: str, fields: Dict[str, EntityField]):
        self.name = name
        self.fields = fields