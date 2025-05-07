from pydantic import BaseModel, Field
from typing import Optional, Dict

class EntityData(BaseModel):
    data: Dict[str, str | int | float | bool]

class UpdateEntityData(BaseModel):
    data: Dict[str, str | int | float | bool]

class EntityDefinition(BaseModel):
    name: str
    fields: Dict[str, str]  # Ej: {"nombre": "str", "edad": "int"}
