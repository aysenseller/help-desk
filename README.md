# Help Desk System

A Python-based Help Desk Ticket Management System that allows users to create, manage, search, filter, sort, and track support tickets through both a terminal-based system and a graphical user interface (GUI).

## Features

### Ticket Management

* Add new tickets
* Show all tickets
* Find tickets by ID
* Edit tickets
* Delete tickets
* Update ticket status
* View detailed ticket information

### Priority Management

Tickets can have three priority levels:

* High
* Medium
* Low

Tickets are displayed with different colors according to their priority.

### Status Management

Supported ticket statuses:

* Open
* In progress
* Resolved
* Closed

### Search

* Search tickets by keyword
* Search results are displayed directly in the ticket table

### Filtering

Tickets can be filtered by:

* Status
* Priority
* Overdue status

### Sorting

Tickets can be sorted by:

* ID
* Priority
* Title
* Due Date

### Due Date

* Add a due date to a ticket
* Display due dates in the ticket table
* Detect overdue tickets automatically
* Highlight overdue tickets
* Display the number of overdue tickets in Statistics

Date format:

```text
DD/MM/YYYY
```

### Statistics

The system displays:

* Total tickets
* Open tickets
* In Progress tickets
* Resolved tickets
* Closed tickets
* Overdue tickets

### Data Persistence

Ticket information is stored using JSON files.

The system supports:

* Saving tickets
* Loading tickets
* Preserving ticket IDs
* Preserving ticket status
* Preserving priority
* Preserving due dates

### GUI

The project includes a Tkinter-based graphical user interface.

The GUI provides:

* Scrollable interface
* Ticket table
* Ticket details
* Add Ticket
* Edit Ticket
* Delete Ticket
* Update Status
* Search
* Filter
* Sort
* Statistics
* Validation messages
* Confirmation dialogs
* Priority and overdue highlighting

## Technologies

* Python
* Tkinter
* JSON
* Pytest
* Git
* GitHub

## Project Structure

```text
help-desk/
│
├── gui.py
├── main.py
├── ticket.py
├── ticket_manager.py
├── file_manager.py
├── ticket.json
├── tickets.json
│
└── tests/
    └── test_ticket.py
```

## Installation

Clone the repository:

```bash
git clone https://github.com/aysenseller/help-desk.git
```

Go to the project directory:

```bash
cd help-desk
```

## Running the Application

### GUI

Run:

```bash
python gui.py
```

### Terminal Version

Run:

```bash
python main.py
```

## Running Tests

Run:

```bash
pytest
```

Current test result:

```text
12 passed
```

## Validation

The application includes validation for:

* Empty ticket titles
* Empty descriptions
* Invalid due date formats
* Missing ticket selection
* Invalid ticket IDs
* Status updates
* Ticket deletion confirmation

## Data Storage

Ticket data is stored in JSON format, allowing the application to preserve ticket information between runs.

## Git

The project uses Git for version control and GitHub for repository hosting.

Main development work is organized using Git branches and commits.

## Future Improvements

Possible future improvements include:

* User authentication
* Multiple support agents
* Ticket assignment
* Comments and ticket history
* Attachments
* Email notifications
* Advanced reporting
* Database integration
* REST API
* Web-based interface

## Author

**Ayşen Seller**

Computer Engineering Student
