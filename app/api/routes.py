from fastapi import APIRouter, HTTPException, Depends, Header
from app.auth.jwt_utils import create_token, verify_token
from app.services.model_factory import create_pydantic_model
from app.services.entity_service import EntityService
from app.infrastructure.db_inmemory import InMemoryRepository
from app.domain.entities import Entity
from app.services.entity_registry import EntityRegistry
from app.schemas.entity_schemas import EntityData, EntityDefinition
from app.services.validation_helper import validate_existing_data

router = APIRouter()
registry = EntityRegistry()
service = EntityService(InMemoryRepository())

def get_current_user(authorization: str = Header(...)):
    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer":
        raise HTTPException(status_code=401, detail="Formato inválido")
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido")
    return payload["sub"]

@router.post("/define")
def define_entity(definition: EntityDefinition, user: str = Depends(get_current_user)):
    if user != "admin":
        raise HTTPException(status_code=403, detail="Acceso denegado. Solo el administrador puede definir entidades.")
    if definition.name in registry.definitions:
        raise HTTPException(status_code=400, detail="Entidad ya registrada")
    if not definition.fields:
        raise HTTPException(status_code=400, detail="Debe definir al menos un campo")
    entity = EntityDefinition(**definition.model_dump())
    registry.register(entity)
    return {"message": f"Entidad '{definition.name}' registrada correctamente."}

@router.post("/{entity}")
def create_dynamic(entity: str, payload: dict, user: str = Depends(get_current_user)):
    try:
        definition = registry.get_definition(entity)
    except KeyError:
        raise HTTPException(status_code=404, detail="Entidad no registrada")
    model_cls = create_pydantic_model(definition)
    if not model_cls:
        raise HTTPException(status_code=500, detail="Error al crear el modelo dinámico")
    if not isinstance(payload, dict):
        raise HTTPException(status_code=400, detail="El payload debe ser un objeto JSON válido")
    validated = model_cls(**payload)  # lanza ValidationError si falla
    return service.create_item(entity, validated.dict())

@router.put("/define/{entity_name}")
def update_entity_definition(entity_name: str, definition: EntityDefinition, user: str = Depends(get_current_user)):
    if entity_name != definition.name:
        raise HTTPException(status_code=400, detail="El nombre no coincide con la URL")

    try:
        entity = EntityData(definition.name, definition.fields)
        registry.update_definition(entity)
        return {"message": f"Entidad '{entity_name}' actualizada correctamente."}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/define")
def list_definitions(user: str = Depends(get_current_user)):
    return registry.list_definitions()

@router.get("/define/{entity_name}")
def get_definition(entity_name: str, user: str = Depends(get_current_user)):
    try:
        definition = registry.get_definition(entity_name)
        return {
            "name": definition.name,
            "fields": definition.fields
        }
    except KeyError:
        raise HTTPException(status_code=404, detail="Entidad no encontrada")

@router.delete("/define/{entity_name}")
def delete_definition(entity_name: str, user: str = Depends(get_current_user)):
    try:
        del registry.definitions[entity_name]
        service.delete_all(entity_name)
        return {"message": f"Entidad '{entity_name}' y sus datos fueron eliminados."}
    except KeyError:
        raise HTTPException(status_code=404, detail="Entidad no encontrada")
    
@router.put("/define/{entity_name}")
def update_entity_definition(entity_name: str, definition: EntityDefinition, user: str = Depends(get_current_user)):
    if entity_name != definition.name:
        raise HTTPException(status_code=400, detail="El nombre no coincide con la URL")

    try:
        entity = EntityData(definition.name, definition.fields)
        
        # Validar datos existentes antes de actualizar
        existing_data = service.list_items(entity_name)
        errors = validate_existing_data(entity, existing_data)

        # Actualizamos la definición igual, pero avisamos si hay errores
        registry.update_definition(entity)

        return {
            "message": f"Entidad '{entity_name}' actualizada correctamente.",
            "validation_errors": errors if errors else None
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))