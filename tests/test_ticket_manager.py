from ticket_manager import TicketManager

def test_add_ticket():
    manager = TicketManager()
    manager.tickets = []

    manager.add_ticket(
        "Wifi problemi",
        "Internete baglanamiyorum",
        "High"
    )

    assert len(manager.tickets) == 1
    assert manager.tickets[0].title == "Wifi problemi"
    assert manager.tickets[0].priority == "High"

def test_find_by_id():
    manager = TicketManager()
    manager.tickets = []

    manager.add_ticket(
        "Bilgisayar problemi",
        "Bilgisayar acilmiyor",
        "Medium"
    )

    ticket = manager.find_by_id(manager.tickets[0].id)

    assert ticket is not None
    assert ticket.title == "Bilgisayar problemi"

def test_search():
    manager = TicketManager()
    manager.tickets = []

    manager.add_ticket(
        "Wifi problemi",
        "Internet yok",
        "High"
    )

    manager.add_ticket(
        "Mouse problemi",
        "Mouse calismiyor",
        "Low"
    )

    results = manager.search("Wifi")

    assert len(results) == 1
    assert results[0].title == "Wifi problemi"

def test_update_status():
    manager = TicketManager()
    manager.tickets = []

    manager.add_ticket(
        "Wifi problemi",
        "Internet yok",
        "High"
    )

    ticket_id = manager.tickets[0].id

    result = manager.update_status(
        ticket_id,
        "Resolved"
    )

    assert result is True
    assert manager.tickets[0].status == "Resolved"


def test_delete_ticket():
    manager = TicketManager()
    manager.tickets = []

    manager.add_ticket(
        "Wifi problemi",
        "Internet yok",
        "High"
    )

    ticket_id = manager.tickets[0].id

    result = manager.delete_ticket(ticket_id)

    assert result is True
    assert len(manager.tickets) == 0

def test_filter_by_status():
    manager = TicketManager()
    manager.tickets = []

    manager.add_ticket("Wifi", "Internet yok", "High")
    manager.add_ticket("Mouse", "Mouse bozuk", "Low")

    manager.update_status(manager.tickets[0].id, "Resolved")

    results = manager.filter_by_status("Resolved")

    assert len(results) == 1
    assert results[0].title == "Wifi"


def test_filter_by_priority():
    manager = TicketManager()
    manager.tickets = []

    manager.add_ticket("Wifi", "Internet yok", "High")
    manager.add_ticket("Mouse", "Mouse bozuk", "Low")

    results = manager.filter_by_priority("High")

    assert len(results) == 1
    assert results[0].title == "Wifi"


def test_sort_by_priority():
    manager = TicketManager()
    manager.tickets = []

    manager.add_ticket("Low Ticket", "Test", "Low")
    manager.add_ticket("High Ticket", "Test", "High")
    manager.add_ticket("Medium Ticket", "Test", "Medium")

    results = manager.sort_by_priority()

    assert results[0].priority == "High"
    assert results[1].priority == "Medium"
    assert results[2].priority == "Low"


def test_statistics():
    manager = TicketManager()
    manager.tickets = []

    manager.add_ticket("Ticket 1", "Test", "High")
    manager.add_ticket("Ticket 2", "Test", "Low")

    manager.update_status(manager.tickets[0].id, "Resolved")

    stats = manager.get_statistics()

    assert stats["total"] == 2
    assert stats["resolved"] == 1
    assert stats["open"] == 1
    assert stats["closed"] == 0
    