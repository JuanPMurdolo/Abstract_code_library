# registry.py
from app.schemas.entity_schemas import EntityDefinition


class Registry:
    def __init__(self):
        self.definitions = {}  # Dict[str, EntityDefinition]
        self.data = {}         # Dict[str, List[dict]] - cada entidad con su lista de datos

    def register(self, entity_definition: EntityDefinition):
        self.definitions[entity_definition.name] = entity_definition

    def update_definition(self, entity_definition: EntityDefinition):
        if entity_definition.name not in self.definitions:
            raise ValueError(f"Entidad '{entity_definition.name}' no está registrada.")
        self.definitions[entity_definition.name] = entity_definition
    
    def get_definition(self, entity_name: str) -> EntityDefinition:
        if entity_name not in self.definitions:
            raise KeyError(f"Entidad '{entity_name}' no está registrada.")
        return self.definitions[entity_name]

    def list_definitions(self):
        return list(self.definitions.values())
    
    def delete_definition(self, entity_name: str):
        if entity_name in self.definitions:
            del self.definitions[entity_name]
            if entity_name in self.data:
                del self.data[entity_name]
        else:
            raise KeyError(f"Entidad '{entity_name}' no está registrada.")
        
    def create(self, entity_name: str, data: dict):
        if entity_name not in self.definitions:
            raise KeyError(f"Entidad '{entity_name}' no está registrada.")
        
        if entity_name not in self.data:
            self.data[entity_name] = []
        
        self.data[entity_name].append(data)
        return data
    
    def list(self, entity_name: str):   
        if entity_name not in self.data:
            return []
        return self.data[entity_name]
    
    def update(self, entity_name: str, item_id: str, data: dict):
        if entity_name not in self.data:
            raise KeyError(f"Entidad '{entity_name}' no está registrada.")
        
        for item in self.data[entity_name]:
            if item.get("id") == item_id:
                item.update(data)
                return item
        
        raise KeyError(f"No se encontró el registro con id '{item_id}' en la entidad '{entity_name}'.")
    
    def delete_all(self, entity_name: str):
        if entity_name in self.data:
            del self.data[entity_name]
        else:
            raise KeyError(f"Entidad '{entity_name}' no está registrada.")
        
