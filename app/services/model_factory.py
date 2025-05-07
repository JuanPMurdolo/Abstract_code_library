from pydantic import create_model
from typing import Any, Dict, Type
from app.domain.entities import Entity

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
        if field_type in type_map
    }
    return create_model(entity.name + "Model", **fields)