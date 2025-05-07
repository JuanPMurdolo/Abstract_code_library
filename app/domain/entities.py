from typing import Dict

class Entity:
    def __init__(self, name: str, fields: Dict[str, str]):
        self.name = name
        self.fields = fields  # Ej: {"nombre": "str", "edad": "int"}