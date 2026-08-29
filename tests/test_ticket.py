from ticket import Ticket

def test_ticket_creation():
    ticket = Ticket(
        "Wifi problemi",
        "Internete baglanamiyorum",
        "High"
    )

    assert ticket.title == "Wifi problemi"
    assert ticket.description == "Internete baglanamiyorum"
    assert ticket.priority == "High"
    assert ticket.status == "Open"

def test_ticket_id():
    ticket1 = Ticket("Problem 1", "Aciklama 1", "Low")
    ticket2 = Ticket("Problem 2", "Aciklama 2", "Medium")

    assert ticket2.id == ticket1.id + 1