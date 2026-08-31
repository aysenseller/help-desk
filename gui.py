import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

from ticket_manager import TicketManager
from file_manager import save_tickets


manager = TicketManager()


# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()
root.title("Help Desk System")
root.geometry("1000x800")
root.minsize(700, 500)


# =========================================================
# SCROLLABLE AREA
# =========================================================

canvas = tk.Canvas(root)

scrollbar = ttk.Scrollbar(
    root,
    orient="vertical",
    command=canvas.yview
)

canvas.configure(
    yscrollcommand=scrollbar.set
)

scrollbar.pack(
    side="right",
    fill="y"
)

canvas.pack(
    side="left",
    fill="both",
    expand=True
)


main_frame = tk.Frame(canvas)

canvas_window = canvas.create_window(
    (0, 0),
    window=main_frame,
    anchor="nw"
)


def update_scroll_region(event=None):
    canvas.configure(
        scrollregion=canvas.bbox("all")
    )


main_frame.bind(
    "<Configure>",
    update_scroll_region
)


def resize_main_frame(event):
    canvas.itemconfig(
        canvas_window,
        width=event.width
    )


canvas.bind(
    "<Configure>",
    resize_main_frame
)


# =========================================================
# MOUSE WHEEL
# =========================================================

def mouse_wheel(event):
    canvas.yview_scroll(
        int(-1 * (event.delta / 120)),
        "units"
    )


canvas.bind_all(
    "<MouseWheel>",
    mouse_wheel
)


# =========================================================
# TITLE
# =========================================================

title_label = tk.Label(
    main_frame,
    text="HELP DESK SYSTEM",
    font=("Arial", 26, "bold"),
    pady=5
)

title_label.pack(
    pady=15
)


# =========================================================
# TICKET MANAGEMENT
# =========================================================

add_frame = tk.LabelFrame(
    main_frame,
    text="Add New Ticket",
    padx=10,
    pady=10,
    font=("Arial", 11, "bold")
)

add_frame.pack(
    fill="x",
    padx=20,
    pady=5
)


# ---------- TITLE ----------

tk.Label(
    add_frame,
    text="Title:"
).grid(
    row=0,
    column=0,
    padx=5,
    pady=5
)


title_entry = tk.Entry(
    add_frame,
    width=30
)

title_entry.grid(
    row=0,
    column=1,
    padx=5,
    pady=5
)


# ---------- DESCRIPTION ----------

tk.Label(
    add_frame,
    text="Description:"
).grid(
    row=1,
    column=0,
    padx=5,
    pady=5
)


description_entry = tk.Entry(
    add_frame,
    width=30
)

description_entry.grid(
    row=1,
    column=1,
    padx=5,
    pady=5
)


# ---------- PRIORITY ----------

tk.Label(
    add_frame,
    text="Priority:"
).grid(
    row=0,
    column=2,
    padx=5,
    pady=5
)


priority_combo = ttk.Combobox(
    add_frame,
    values=[
        "Low",
        "Medium",
        "High"
    ],
    state="readonly",
    width=15
)

priority_combo.set("Medium")

priority_combo.grid(
    row=0,
    column=3,
    padx=5,
    pady=5
)


# ---------- DUE DATE ----------

tk.Label(
    add_frame,
    text="Due Date:"
).grid(
    row=1,
    column=2,
    padx=5,
    pady=5
)


due_date_entry = tk.Entry(
    add_frame,
    width=18
)

due_date_entry.grid(
    row=1,
    column=3,
    padx=5,
    pady=5
)


# ---------- STATUS ----------

tk.Label(
    add_frame,
    text="New Status:"
).grid(
    row=2,
    column=0,
    padx=5,
    pady=5
)


status_combo = ttk.Combobox(
    add_frame,
    values=[
        "Open",
        "In progress",
        "Resolved",
        "Closed"
    ],
    state="readonly",
    width=15
)

status_combo.set("Open")

status_combo.grid(
    row=2,
    column=1,
    padx=5,
    pady=5
)


# =========================================================
# TICKET TABLE
# =========================================================

list_frame = tk.LabelFrame(
    main_frame,
    text="Tickets",
    padx=10,
    pady=10,
    font=("Arial", 11, "bold")
)

list_frame.pack(
    fill="x",
    padx=20,
    pady=5
)


columns = (
    "ID",
    "Title",
    "Priority",
    "Status",
    "Due Date"
)


ticket_table = ttk.Treeview(
    list_frame,
    columns=columns,
    show="headings",
    height=12
)


for column in columns:
    ticket_table.heading(
        column,
        text=column
    )


ticket_table.column(
    "ID",
    width=60,
    anchor="center"
)

ticket_table.column(
    "Title",
    width=300
)

ticket_table.column(
    "Priority",
    width=120,
    anchor="center"
)

ticket_table.column(
    "Status",
    width=150,
    anchor="center"
)

ticket_table.column(
    "Due Date",
    width=120,
    anchor="center"
)


ticket_table.pack(
    fill="both",
    expand=True
)


# =========================================================
# PRIORITY COLORS
# =========================================================

ticket_table.tag_configure(
    "High",
    background="#ffcccc"
)

ticket_table.tag_configure(
    "Medium",
    background="#ffe5cc"
)

ticket_table.tag_configure(
    "Low",
    background="#ccffcc"
)

ticket_table.tag_configure(
    "Overdue",
    background="#ff9999"
)


# =========================================================
# TICKET DETAILS
# =========================================================

details_frame = tk.LabelFrame(
    main_frame,
    text="Ticket Details",
    padx=10,
    pady=10,
    font=("Arial", 11, "bold")
)

details_frame.pack(
    fill="x",
    padx=20,
    pady=5
)


details_label = tk.Label(
    details_frame,
    text="Select a ticket to see details.",
    justify="left",
    anchor="w"
)

details_label.pack(
    fill="x"
)


# =========================================================
# FUNCTIONS
# =========================================================

def refresh_tickets():

    for item in ticket_table.get_children():
        ticket_table.delete(item)

    for ticket in manager.tickets:

        tag = ticket.priority

        if (
            ticket.due_date
            and ticket.status not in ["Resolved", "Closed"]
        ):

            try:

                due_date = datetime.strptime(
                    ticket.due_date,
                    "%d/%m/%Y"
                ).date()

                if due_date < datetime.today().date():
                    tag = "Overdue"

            except ValueError:
                pass

        ticket_table.insert(
            "",
            tk.END,
            values=(
                ticket.id,
                ticket.title,
                ticket.priority,
                ticket.status,
                ticket.due_date or "-"
            ),
            tags=(tag,)
        )


def refresh_statistics():

    stats = manager.get_statistics()

    total_label.config(
        text=f"Total: {stats['total']}"
    )

    open_label.config(
        text=f"Open: {stats['open']}"
    )

    progress_label.config(
        text=f"In Progress: {stats['in_progress']}"
    )

    resolved_label.config(
        text=f"Resolved: {stats['resolved']}"
    )

    closed_label.config(
        text=f"Closed: {stats['closed']}"
    )

    overdue_count = 0

    for ticket in manager.tickets:

        if (
            ticket.due_date
            and ticket.status not in ["Resolved", "Closed"]
        ):

            try:

                due_date = datetime.strptime(
                    ticket.due_date,
                    "%d/%m/%Y"
                ).date()

                if due_date < datetime.today().date():
                    overdue_count += 1

            except ValueError:
                pass

    overdue_label.config(
        text=f"Overdue: {overdue_count}"
    )


# =========================================================
# ADD TICKET
# =========================================================

def add_ticket():

    title = title_entry.get().strip()
    description = description_entry.get().strip()
    priority = priority_combo.get()
    due_date = due_date_entry.get().strip()

    if due_date:

        try:

            datetime.strptime(
                due_date,
                "%d/%m/%Y"
            )

        except ValueError:

            messagebox.showerror(
                "Invalid Date",
                "Please enter the date in DD/MM/YYYY format."
            )

            return

    if not title:

        messagebox.showerror(
            "Error",
            "Title cannot be empty."
        )

        return

    if not description:

        messagebox.showerror(
            "Error",
            "Description cannot be empty."
        )

        return

    manager.add_ticket(
        title,
        description,
        priority
    )

    ticket = manager.tickets[-1]

    ticket.due_date = (
        due_date
        if due_date
        else None
    )

    save_tickets(
        manager.tickets
    )

    messagebox.showinfo(
        "Success",
        "Ticket added successfully!"
    )

    title_entry.delete(
        0,
        tk.END
    )

    description_entry.delete(
        0,
        tk.END
    )

    due_date_entry.delete(
        0,
        tk.END
    )

    priority_combo.set(
        "Medium"
    )

    status_combo.set(
        "Open"
    )

    refresh_tickets()
    refresh_statistics()


# =========================================================
# DELETE TICKET
# =========================================================

def delete_ticket():

    selected = ticket_table.selection()

    if not selected:

        messagebox.showwarning(
            "Warning",
            "Please select a ticket."
        )

        return

    item = ticket_table.item(
        selected[0]
    )

    ticket_id = item["values"][0]

    confirm = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this ticket?"
    )

    if not confirm:
        return

    success = manager.delete_ticket(
        ticket_id
    )

    if success:

        messagebox.showinfo(
            "Success",
            "Ticket deleted successfully!"
        )

        details_label.config(
            text="Select a ticket to see details."
        )

        title_entry.delete(
            0,
            tk.END
        )

        description_entry.delete(
            0,
            tk.END
        )

        due_date_entry.delete(
            0,
            tk.END
        )

        refresh_tickets()
        refresh_statistics()

    else:

        messagebox.showerror(
            "Error",
            "Ticket not found."
        )


# =========================================================
# UPDATE STATUS
# =========================================================

def update_status():

    selected = ticket_table.selection()

    if not selected:

        messagebox.showwarning(
            "Warning",
            "Please select a ticket."
        )

        return

    item = ticket_table.item(
        selected[0]
    )

    ticket_id = item["values"][0]

    new_status = status_combo.get()

    if not new_status:

        messagebox.showwarning(
            "Warning",
            "Please select a status."
        )

        return

    success = manager.update_status(
        ticket_id,
        new_status
    )

    if success:

        messagebox.showinfo(
            "Success",
            "Status updated successfully!"
        )

        refresh_tickets()
        refresh_statistics()

        for item_id in ticket_table.get_children():

            values = ticket_table.item(
                item_id
            )["values"]

            if values[0] == ticket_id:

                ticket_table.selection_set(
                    item_id
                )

                ticket_table.focus(
                    item_id
                )

                break

    else:

        messagebox.showerror(
            "Error",
            "Ticket not found."
        )


# =========================================================
# SHOW TICKET DETAILS
# =========================================================

def show_ticket_details(event=None):

    selected = ticket_table.selection()

    if not selected:
        return

    item = ticket_table.item(
        selected[0]
    )

    values = item.get(
        "values",
        []
    )

    if not values:
        return

    ticket_id = int(
        values[0]
    )

    ticket = manager.find_by_id(
        ticket_id
    )

    if not ticket:

        messagebox.showerror(
            "Error",
            "Ticket not found."
        )

        return

    # Fill edit fields

    title_entry.delete(
        0,
        tk.END
    )

    title_entry.insert(
        0,
        ticket.title
    )

    description_entry.delete(
        0,
        tk.END
    )

    description_entry.insert(
        0,
        ticket.description
    )

    priority_combo.set(
        ticket.priority
    )

    status_combo.set(
        ticket.status
    )

    due_date_entry.delete(
        0,
        tk.END
    )

    due_date_entry.insert(
        0,
        ticket.due_date or ""
    )

    # Show details

    details_label.config(
        text=(
            f"ID: {ticket.id}\n"
            f"Title: {ticket.title}\n"
            f"Description: {ticket.description}\n"
            f"Priority: {ticket.priority}\n"
            f"Status: {ticket.status}\n"
            f"Due Date: {ticket.due_date or '-'}"
        )
    )


ticket_table.bind(
    "<<TreeviewSelect>>",
    show_ticket_details
)


# =========================================================
# EDIT TICKET
# =========================================================

def edit_ticket():

    selected = ticket_table.selection()

    if not selected:

        messagebox.showwarning(
            "Warning",
            "Please select a ticket."
        )

        return

    item = ticket_table.item(
        selected[0]
    )

    ticket_id = item["values"][0]

    ticket = manager.find_by_id(
        ticket_id
    )

    if not ticket:

        messagebox.showerror(
            "Error",
            "Ticket not found."
        )

        return

    title = title_entry.get().strip()
    description = description_entry.get().strip()
    priority = priority_combo.get()
    due_date = due_date_entry.get().strip()

    if due_date:

        try:

            datetime.strptime(
                due_date,
                "%d/%m/%Y"
            )

        except ValueError:

            messagebox.showerror(
                "Invalid Date",
                "Please enter the date in DD/MM/YYYY format."
            )

            return

    if not title:

        messagebox.showerror(
            "Error",
            "Title cannot be empty."
        )

        return

    if not description:

        messagebox.showerror(
            "Error",
            "Description cannot be empty."
        )

        return

    ticket.title = title
    ticket.description = description
    ticket.priority = priority

    ticket.due_date = (
        due_date
        if due_date
        else None
    )

    save_tickets(
        manager.tickets
    )

    messagebox.showinfo(
        "Success",
        "Ticket updated successfully!"
    )

    refresh_tickets()
    refresh_statistics()


# =========================================================
# SEARCH
# =========================================================

def search_tickets():

    keyword = search_entry.get().strip()

    if not keyword:

        refresh_tickets()
        return

    results = manager.search(
        keyword
    )

    for item in ticket_table.get_children():
        ticket_table.delete(item)

    for ticket in results:

        tag = ticket.priority

        if (
            ticket.due_date
            and ticket.status not in ["Resolved", "Closed"]
        ):

            try:

                due_date = datetime.strptime(
                    ticket.due_date,
                    "%d/%m/%Y"
                ).date()

                if due_date < datetime.today().date():
                    tag = "Overdue"

            except ValueError:
                pass

        ticket_table.insert(
            "",
            tk.END,
            values=(
                ticket.id,
                ticket.title,
                ticket.priority,
                ticket.status,
                ticket.due_date or "-"
            ),
            tags=(tag,)
        )


# =========================================================
# FILTER
# =========================================================

def filter_tickets():

    selected_status = status_filter.get()
    selected_priority = priority_filter.get()
    selected_due = due_filter.get()

    results = manager.tickets

    if selected_status != "All":

        results = [
            ticket
            for ticket in results
            if ticket.status == selected_status
        ]

    if selected_priority != "All":

        results = [
            ticket
            for ticket in results
            if ticket.priority == selected_priority
        ]

    if selected_due == "Overdue":

        filtered_results = []

        for ticket in results:

            if (
                ticket.due_date
                and ticket.status not in ["Resolved", "Closed"]
            ):

                try:

                    due_date = datetime.strptime(
                        ticket.due_date,
                        "%d/%m/%Y"
                    ).date()

                    if due_date < datetime.today().date():
                        filtered_results.append(ticket)

                except ValueError:
                    pass

        results = filtered_results

    for item in ticket_table.get_children():
        ticket_table.delete(item)

    for ticket in results:

        tag = ticket.priority

        if (
            ticket.due_date
            and ticket.status not in ["Resolved", "Closed"]
        ):

            try:

                due_date = datetime.strptime(
                    ticket.due_date,
                    "%d/%m/%Y"
                ).date()

                if due_date < datetime.today().date():
                    tag = "Overdue"

            except ValueError:
                pass

        ticket_table.insert(
            "",
            tk.END,
            values=(
                ticket.id,
                ticket.title,
                ticket.priority,
                ticket.status,
                ticket.due_date or "-"
            ),
            tags=(tag,)
        )


def clear_filter():

    status_filter.set(
        "All"
    )

    priority_filter.set(
        "All"
    )

    due_filter.set(
        "All"
    )

    refresh_tickets()


# =========================================================
# SORT
# =========================================================

def sort_tickets():

    selected_sort = sort_combo.get()

    if selected_sort == "ID":

        results = sorted(
            manager.tickets,
            key=lambda ticket: ticket.id
        )

    elif selected_sort == "Priority":

        priority_order = {
            "High": 1,
            "Medium": 2,
            "Low": 3
        }

        results = sorted(
            manager.tickets,
            key=lambda ticket:
            priority_order.get(
                ticket.priority,
                4
            )
        )

    elif selected_sort == "Title":

        results = sorted(
            manager.tickets,
            key=lambda ticket:
            ticket.title.lower()
        )

    elif selected_sort == "Due Date":

        results = sorted(
            manager.tickets,
            key=lambda ticket: (
                datetime.strptime(
                    ticket.due_date,
                    "%d/%m/%Y"
                )
                if ticket.due_date
                else datetime.max
            )
        )

    else:

        results = manager.tickets

    for item in ticket_table.get_children():
        ticket_table.delete(item)

    for ticket in results:

        tag = ticket.priority

        if (
            ticket.due_date
            and ticket.status not in ["Resolved", "Closed"]
        ):

            try:

                due_date = datetime.strptime(
                    ticket.due_date,
                    "%d/%m/%Y"
                ).date()

                if due_date < datetime.today().date():
                    tag = "Overdue"

            except ValueError:
                pass

        ticket_table.insert(
            "",
            tk.END,
            values=(
                ticket.id,
                ticket.title,
                ticket.priority,
                ticket.status,
                ticket.due_date or "-"
            ),
            tags=(tag,)
        )


# =========================================================
# BUTTONS
# =========================================================

add_button = tk.Button(
    add_frame,
    text="Add Ticket",
    width=15,
    command=add_ticket,
    font=("Arial", 10, "bold"),
    padx=5,
    pady=3
)

add_button.grid(
    row=0,
    column=4,
    padx=5,
    pady=5
)


edit_button = tk.Button(
    add_frame,
    text="Edit Ticket",
    width=15,
    command=edit_ticket,
    font=("Arial", 10, "bold"),
    padx=5,
    pady=3
)

edit_button.grid(
    row=1,
    column=4,
    padx=5,
    pady=5
)


delete_button = tk.Button(
    add_frame,
    text="Delete Ticket",
    width=15,
    command=delete_ticket,
    font=("Arial", 10, "bold"),
    padx=5,
    pady=3
)

delete_button.grid(
    row=2,
    column=4,
    padx=5,
    pady=5
)


update_button = tk.Button(
    add_frame,
    text="Update Status",
    width=15,
    command=update_status,
    font=("Arial", 10, "bold"),
    padx=5,
    pady=3
)

update_button.grid(
    row=3,
    column=4,
    padx=5,
    pady=5
)


# =========================================================
# SEARCH FRAME
# =========================================================

search_frame = tk.LabelFrame(
    main_frame,
    text="Search",
    padx=10,
    pady=5,
    font=("Arial", 11, "bold")
)

search_frame.pack(
    fill="x",
    padx=20,
    pady=5
)


search_entry = tk.Entry(
    search_frame,
    width=40
)

search_entry.pack(
    side="left",
    padx=5
)


search_button = tk.Button(
    search_frame,
    text="Search",
    width=12,
    command=search_tickets,
    font=("Arial", 10, "bold"),
    padx=5,
    pady=3
)

search_button.pack(
    side="left",
    padx=5
)


clear_search_button = tk.Button(
    search_frame,
    text="Clear",
    width=10,
    command=lambda: (
        search_entry.delete(0, tk.END),
        refresh_tickets()
    ),
    font=("Arial", 10, "bold"),
    padx=5,
    pady=3
)

clear_search_button.pack(
    side="left",
    padx=5
)


# =========================================================
# FILTER FRAME
# =========================================================

filter_frame = tk.LabelFrame(
    main_frame,
    text="Filter",
    padx=10,
    pady=10,
    font=("Arial", 11, "bold")
)

filter_frame.pack(
    fill="x",
    padx=20,
    pady=5
)


tk.Label(
    filter_frame,
    text="Status:"
).pack(
    side="left",
    padx=5
)


status_filter = ttk.Combobox(
    filter_frame,
    values=[
        "All",
        "Open",
        "In progress",
        "Resolved",
        "Closed"
    ],
    state="readonly",
    width=15
)

status_filter.set(
    "All"
)

status_filter.pack(
    side="left",
    padx=5
)


tk.Label(
    filter_frame,
    text="Priority:"
).pack(
    side="left",
    padx=5
)


priority_filter = ttk.Combobox(
    filter_frame,
    values=[
        "All",
        "Low",
        "Medium",
        "High"
    ],
    state="readonly",
    width=15
)

priority_filter.set(
    "All"
)

priority_filter.pack(
    side="left",
    padx=5
)


tk.Label(
    filter_frame,
    text="Due:"
).pack(
    side="left",
    padx=5
)


due_filter = ttk.Combobox(
    filter_frame,
    values=[
        "All",
        "Overdue"
    ],
    state="readonly",
    width=12
)

due_filter.set(
    "All"
)

due_filter.pack(
    side="left",
    padx=5
)


filter_button = tk.Button(
    filter_frame,
    text="Apply Filter",
    width=15,
    command=filter_tickets,
    font=("Arial", 10, "bold"),
    padx=5,
    pady=3
)

filter_button.pack(
    side="left",
    padx=10
)


clear_filter_button = tk.Button(
    filter_frame,
    text="Clear",
    width=10,
    command=clear_filter,
    font=("Arial", 10, "bold"),
    padx=5,
    pady=3
)

clear_filter_button.pack(
    side="left",
    padx=5
)


# =========================================================
# SORT FRAME
# =========================================================

sort_frame = tk.LabelFrame(
    main_frame,
    text="Sort",
    padx=10,
    pady=5,
    font=("Arial", 11, "bold")
)

sort_frame.pack(
    fill="x",
    padx=20,
    pady=5
)


sort_combo = ttk.Combobox(
    sort_frame,
    values=[
        "ID",
        "Priority",
        "Title",
        "Due Date"
    ],
    state="readonly",
    width=15
)

sort_combo.set(
    "ID"
)

sort_combo.pack(
    side="left",
    padx=5
)


sort_button = tk.Button(
    sort_frame,
    text="Sort",
    width=12,
    command=sort_tickets,
    font=("Arial", 10, "bold"),
    padx=5,
    pady=3
)

sort_button.pack(
    side="left",
    padx=5
)


# =========================================================
# STATISTICS
# =========================================================

stats_frame = tk.LabelFrame(
    main_frame,
    text="Statistics",
    padx=10,
    pady=10,
    font=("Arial", 12, "bold")
)

stats_frame.pack(
    fill="x",
    padx=20,
    pady=5
)


total_label = tk.Label(
    stats_frame,
    text="Total: 0",
    font=("Arial", 11, "bold")
)

total_label.pack(
    side="left",
    padx=15
)


open_label = tk.Label(
    stats_frame,
    text="Open: 0",
    font=("Arial", 11, "bold")
)

open_label.pack(
    side="left",
    padx=15
)


progress_label = tk.Label(
    stats_frame,
    text="In Progress: 0",
    font=("Arial", 11, "bold")
)

progress_label.pack(
    side="left",
    padx=15
)


resolved_label = tk.Label(
    stats_frame,
    text="Resolved: 0",
    font=("Arial", 11, "bold")
)

resolved_label.pack(
    side="left",
    padx=15
)


closed_label = tk.Label(
    stats_frame,
    text="Closed: 0",
    font=("Arial", 11, "bold")
)

closed_label.pack(
    side="left",
    padx=15
)


overdue_label = tk.Label(
    stats_frame,
    text="Overdue: 0",
    font=("Arial", 11, "bold")
)

overdue_label.pack(
    side="left",
    padx=20
)


# =========================================================
# INITIAL LOAD
# =========================================================

refresh_tickets()
refresh_statistics()

root.mainloop()