from typing import List
from pydantic import ValidationError
from app.services.model_factory import create_pydantic_model
from app.domain.entities import Entity

def validate_existing_data(entity: Entity, existing_data: List[dict]):
    model_cls = create_pydantic_model(entity)
    errors = []

    for item in existing_data:
        try:
            model_cls(**item)
        except ValidationError as ve:
            errors.append({
                "id": item.get("id", "unknown"),
                "errors": ve.errors()
            })

    return errors