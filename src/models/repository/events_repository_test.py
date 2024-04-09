import pytest
from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository

db_connection_handler.connect_to_db()

# configuração do teste de integração
# para executar o teste: pytest -s -v src/models/repository/events_repository_test.py

@pytest.mark.skip(reason="Novo registro em banco de dados")
def test_insert_event():
    event = {
        "uuid": "teste2-uuid",
        "title": "teste2-title",
        "slug": "teste2-slug",
        "maximum_attendees": 20
    }

    events_repository = EventsRepository()
    response = events_repository.insert_event(event)
    print(response)

@pytest.mark.skip(reason="Consulta evento por id")
def test_get_event_by_id():
    event_id = "teste2-uuid"
    events_repository = EventsRepository()
    response = events_repository.get_event_by_id(event_id)
    print(response)
    print(response.title)