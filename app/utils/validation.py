from fastapi import HTTPException
from app.services.registry_check import Registry

def validate_relationships(entity_name: str, data: dict):
    entity_def = Registry.get_definition(entity_name)
    if not entity_def:
        raise HTTPException(status_code=404, detail=f"Entidad '{entity_name}' no está registrada.")
    print(entity_def)

    for field_name, field in entity_def.fields.items():
        if field_name not in data:
            if field.required:
                raise HTTPException(status_code=400, detail=f"El campo '{field_name}' es requerido pero no fue provisto.")
            continue
        if field.relation:
            related_entity = field.relation
            related_id = data.get(field_name)

            if related_id is None:
                raise HTTPException(status_code=400, detail=f"El campo relacional '{field_name}' no fue provisto.")

            related_items = Registry.data.get(related_entity, [])
            if not any(item.get("id") == related_id for item in related_items):
                raise HTTPException(
                    status_code=400,
                    detail=f"No existe un registro en '{related_entity}' con id = {related_id} para el campo '{field_name}'"
                )
