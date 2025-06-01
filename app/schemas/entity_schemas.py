from pydantic import BaseModel, Field
from typing import Optional, Dict

class EntityData(BaseModel):
    data: Dict[str, str | int | float | bool]

class UpdateEntityData(BaseModel):
    data: Dict[str, str | int | float | bool]

class EntityField(BaseModel):
    type: str
    relation: Optional[str] = None

class EntityDefinition(BaseModel):
    name: str
    fields: Dict[str, EntityField]
