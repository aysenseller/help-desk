from ticket_manager import TicketManager

manager = TicketManager()

def show_menu():
    print("\n========== HELP DESK ==========")
    print("1. Add ticket")
    print("2. Show all tickets")
    print("3. Find ticket by ID")
    print("4. Search tickets")
    print("5. Update status")
    print("6. Delete ticket")
    print("7. Statistics")
    print("8. Filter by Status")
    print("9. Filter by Priority")
    print("10. Sort by ID")
    print("11. Sort by Priority")
    print("12. Exit")
    print("===============================")

while True:
    show_menu()

    choice = input("Choose an option: ")

    if choice == "1":
        while True:
            title = input("Title: ").strip()
            if title:
                break
            print("Title cannot be empty.")

        while True:
            description = input("Description: ").strip()

            if description:
                break
            print("Description cannot be empty.")

        while True:
            priority = input("Priority (Low/Medium/High): ")

            if priority in ["Low","Medium","High"]:
                break
            print("Invalid priority. Use Low, Medium or High.")

        manager.add_ticket(title, description, priority)

        print("Ticket added successfully!")

    elif choice == "2":
        manager.show_tickets()

    elif choice == "3":
        try:
            ticket_id = int(input("Ticket ID: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        ticket = manager.find_by_id(ticket_id)

        if ticket:
            print(ticket)
            print("Description:", ticket.description)
        else:
            print("Ticket not found.")

    elif choice == "4":
        keyword = input("Search:")
        results = manager.search(keyword)

        if results:
            for ticket in results:
                print(ticket)
        else:
            print("No tickets found.")

    elif choice == "5":
        try:
            ticket_id = int(input("Ticket ID: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        valid_status = [
            "Open",
            "In Progress",
            "Resolved",
            "Closed"
        ]
        while True:
            new_status = input("New status (Open/In Progress/Resolved/Closed): ")
            if new_status in valid_status:
                break
            print("Invalid status.")

        success = manager.update_status(ticket_id, new_status)

        if success:
            print("Status updated successfully!")
        else:
            print("Ticket not found.")

    elif choice == "6":
        try:
            ticket_id = int(input("Ticket ID: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        success = manager.delete_ticket(ticket_id)

        if success:
            print("Ticket deleted successfully!")
        else:
            print("Ticket not found.")


    elif choice == "7":
        stats = manager.get_statistics()

        print("\n===== Statistics =====")
        print("Total:", stats["total"])
        print("Open:", stats["open"])
        print("In Progress:", stats["in_progress"])
        print("Resolved:", stats["resolved"])
        print("Closed:", stats["closed"])

    elif choice == "8":
        status = input(
            "Status (Open/In Progress/Resolved/Closed): "
        )

        results = manager.filter_by_status(status)

        for ticket in results:
            print(ticket)

    elif choice == "9":
        priority = input(
            "Priority (High/Medium/Low): "
        )

        results = manager.filter_by_priority(priority)

        for ticket in results:
            print(ticket)

    elif choice == "10":
        tickets = manager.sort_by_id()

        for ticket in tickets:
            print(ticket)

    elif choice == "11":
        tickets = manager.sort_by_priority()

        for ticket in tickets:
            print(ticket)

    elif choice == "12":
            print("Goodbye!")
            break
    
    else:
        print("Invalid choice.")

