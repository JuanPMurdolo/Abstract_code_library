from pydantic import create_model
from app.domain.entities import Entity
from typing import Any, Dict, Type

type_map = {
    "str": (str, ...),
    "int": (int, ...),
    "float": (float, ...),
    "bool": (bool, ...),
    "list": (list, ...),
    "dict": (dict, ...),
    "datetime": (str, ...),  # Assuming datetime is serialized as ISO string
    "date": (str, ...),      # Assuming date is serialized as ISO string
    "time": (str, ...),      # Assuming time is serialized as ISO string
    "uuid": (str, ...),      # Assuming UUID is serialized as string
    "bytes": (bytes, ...),   # Assuming bytes are serialized as base64 string
    "any": (Any, ...),       # Generic type for any data
    "object": (dict, ...),   # Generic object type
}

def create_pydantic_model(entity: Entity) -> Type:
    fields: Dict[str, Any] = {
        name: type_map[field_type]
        for name, field_type in entity.fields.items()
    }
    return create_model(entity.name + "Model", **fields)
