from domain.repositories import AbstractRepository

class EntityService:
    def __init__(self, repository: AbstractRepository):
        self.repository = repository

    def create_item(self, entity: str, data: dict):
        return self.repository.create(entity, data)

    def list_items(self, entity: str):
        return self.repository.list(entity)

    def update_item(self, entity: str, item_id: str, data: dict):
        return self.repository.update(entity, item_id, data)

    def delete_all(self, entity: str):
        self.repository.data.pop(entity, None)