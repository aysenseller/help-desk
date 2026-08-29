import json
from ticket import Ticket

def save_tickets(tickets, filename="ticket.json"):
    data = []

    for ticket in tickets:
        data.append({
            "id":ticket.id,
            "title":ticket.title,
            "description":ticket.description,
            "priority":ticket.priority,
            "status":ticket.status
        })


    with open(filename,"w")as file:
        json.dump(data,file,indent=4)

def load_tickets(filename="tickets.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)

        tickets = []

        for item in data:
            ticket = Ticket(
                item["title"],
                item["description"],
                item["priority"]
            )

            ticket.id = item["id"]
            ticket.status = item["status"]

            tickets.append(ticket)

        return tickets

    except FileNotFoundError:
        return []