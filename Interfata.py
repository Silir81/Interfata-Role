import tkinter as tk

def save_data():
    # Function to save the input data
    pass

root = tk.Tk()
root.title("User Interface")

# Labels
labels = [
    "Latime x Grosime",
    "Tip Material",
    "Id Proiect",
    "Rebuturi",
    "Lungime profil",
    "Nr. Intern Rola",
    "Tip Zincare",
    "Profile Neconforme"
]

for label_text in labels:
    label = tk.Label(root, text=label_text)
    label.pack()

# Entry fields
entry_fields = [tk.Entry(root) for _ in range(7)]
for entry in entry_fields:
    entry.pack()

# Dropdowns
dropdowns = [
    tk.OptionMenu(root, tk.StringVar(root, "Option 1"), "Option 1", "Option 2", "Option 3"),
    tk.OptionMenu(root, tk.StringVar(root, "Option A"), "Option A", "Option B", "Option C")
]

for dropdown in dropdowns:
    dropdown.pack()

# Save button
save_button = tk.Button(root, text="Save", command=save_data)
save_button.pack()

root.mainloop()
