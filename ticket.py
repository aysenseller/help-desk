class Ticket:
    next_id = 1

    def __init__(self, title, description, priority):
        self.id = Ticket.next_id
        Ticket.next_id += 1

        self.title = title
        self.description = description
        self.priority = priority
        self.status = "Open"

    def __str__(self):
        return f"[{self.id}] {self.title} | {self.priority} | {self.status}"