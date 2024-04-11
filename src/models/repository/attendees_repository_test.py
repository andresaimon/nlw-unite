import pytest
from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo registro em banco de dados")
def test_insert_attendee():
    event_id = "teste1-uuid"
    attendees_info = {
        "uuid": "uuid_attendee_teste1",
        "name": "atendee name teste1",
        "email": "teste1@email.com",
        "event_id": event_id
    }
    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendee(attendees_info)
    print(response)

@pytest.mark.skip(reason="Consulta")
def test_get_attendee_badge_by_id():
    attendde_id = "uuid_attendee_teste1"
    attendees_repository = AttendeesRepository()
    attendee = attendees_repository.get_attendee_badge_by_id(attendde_id)

    print(attendee)
    print(attendee.title)