from pydantic import create_model
from app.domain.entities import Entity
from typing import Any, Dict, Type

type_map = {
    "str": (str, ...),
    "int": (int, ...),
    "float": (float, ...),
    "bool": (bool, ...),
}

def create_pydantic_model(entity: Entity) -> Type:
    fields: Dict[str, Any] = {
        name: type_map[field_type]
        for name, field_type in entity.fields.items()
    }
    return create_model(entity.name + "Model", **fields)
