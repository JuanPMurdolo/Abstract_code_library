from app.domain.entities import Entity
from typing import Dict

class EntityRegistry:
    def __init__(self):
        self.definitions: Dict[str, Entity] = {}

    def register(self, entity: Entity):
        self.definitions[entity.name] = entity

    def get_definition(self, name: str) -> Entity:
        return self.definitions[name]

    def list_definitions(self) -> list[str]:
        return list(self.definitions.keys())
    
    def update_definition(self, entity: Entity):
        if entity.name not in self.definitions:
            raise ValueError("Entidad no existe")
        self.definitions[entity.name] = entity