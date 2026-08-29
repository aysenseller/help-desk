from ticket import Ticket
from file_manager import save_tickets, load_tickets

def test_save_and_load_tickets(tmp_path):
    filename = tmp_path / "test_tickets.json"

    ticket = Ticket(
        "Wifi problemi",
        "Internete baglanamiyorum",
        "High"
    )

    save_tickets([ticket],filename)

    loaded_tickets = load_tickets(filename)

    assert len(loaded_tickets)== 1
    assert loaded_tickets[0].title == "Wifi problemi"
    assert loaded_tickets[0].description == "Internete baglanamiyorum"
    assert loaded_tickets[0].priority == "High"
    assert loaded_tickets[0].status == "Open"
    assert loaded_tickets[0].id == ticket.id