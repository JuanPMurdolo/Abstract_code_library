from pydantic import create_model, Field, ConfigDict
from typing import Any, Dict, Type

from app.domain.entities import Entity

type_map = {
    "str": str,
    "int": int,
    "float": float,
    "bool": bool
}

def create_pydantic_model(entity: Entity) -> Type:
    fields: Dict[str, tuple] = {}

    for name, field_def in entity.fields.items():
        py_type = type_map.get(field_def.type, str)
        fields[name] = (py_type, Field(...))

    # Agregamos configuración explícita para evitar error de generación de schema
    model_config = ConfigDict(arbitrary_types_allowed=True)

    return create_model(
        entity.name + "Model",
        __config__=model_config,
        **fields
    )

