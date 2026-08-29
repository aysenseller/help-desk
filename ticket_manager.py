from ticket import Ticket
from file_manager import save_tickets, load_tickets

class TicketManager:
    def __init__(self):
        self.tickets =load_tickets()
        if self.tickets:
            Ticket.next_id = max(ticket.id for ticket in self.tickets) + 1

    def add_ticket(self, title, description, priority):
        ticket = Ticket(title,description,priority)
        self.tickets.append(ticket)
        save_tickets(self.tickets)


    def show_tickets(self):
        for ticket in self.tickets:
            print(ticket)

    def find_by_id(self,ticket_id):
        for ticket in self.tickets:
            if ticket_id == ticket.id :
                return ticket

        return None


    def search(self, keyword):
        results = []

        for ticket in self.tickets:
            if keyword.lower() in ticket.title.lower():
                results.append(ticket)

        return results

    def update_status(self, ticket_id, new_status):
        ticket = self.find_by_id(ticket_id)

        if ticket :
            ticket.status = new_status
            save_tickets(self.tickets)
            return True
        
        return False

    def delete_ticket(self,ticket_id):
        ticket = self.find_by_id(ticket_id)

        if ticket:
            self.tickets.remove(ticket)
            save_tickets(self.tickets)
            return True

        return False

    def get_statistics(self):
        stats = {
            "total":len(self.tickets),
            "open":0,
            "in_progress":0,
            "resolved":0,
            "closed":0
        }

        for ticket in self.tickets:
            if ticket.status == "Open":
                stats["open"]+=1
            elif ticket.status == "In Progress":
                stats["in_progress"] +=1
            elif ticket.status == "Resolved":
                stats["resolved"]+= 1
            elif ticket.closed == "Closed":
                stats["closed"]+= 1

        return stats

    def filter_by_status(self,status):
        results = []

        for ticket in self.tickets:
            if ticket.status == status:
                results.append(ticket)

        return results

    def filter_by_priority(self,priority):
        results=[]

        for ticket in self.tickets:
            if ticket.priority == priority:
                results.append(ticket)

        return results

    def sort_by_id(self):
        return sorted(
            self.tickets,
            key=lambda ticket:ticket.id
        )

    def sort_by_priority(self):
        priority_order = {
            "high": 1,
            "medium": 2,
            "low": 3
        }

        return sorted(
            self.tickets,
            key=lambda ticket:priority_order[ticket.priority.lower()]
        
        )