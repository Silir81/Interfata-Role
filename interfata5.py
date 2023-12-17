import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pandas as pd

def display_selected_data(selected_tambur):
    selected_data = df[(df['Tambur'] == selected_tambur) & (df['KG / Rola'] > 0)][['Nr. Intern Rola', 'KG / Rola']]
    selected_data_table.delete(*selected_data_table.get_children())
    for index, row in selected_data.iterrows():
        selected_data_table.insert("", tk.END, values=tuple(row))

# Rest of your functions...

root = tk.Tk()
root.title("Excel Data Viewer")

tambur_var = tk.StringVar(root)
tambur_var.set('Select Tambur')
tambur_dropdown = tk.OptionMenu(root, tambur_var, 'Select Tambur')
tambur_dropdown.pack()

btn_open_excel = tk.Button(root, text="Open Excel File", command=open_excel)
btn_open_excel.pack()

selected_data_table = ttk.Treeview(root, columns=('Nr. Intern Rola', 'KG / Rola', 'New KG / Rola'), show='headings')
selected_data_table.heading('Nr. Intern Rola', text='Nr. Intern Rola')
selected_data_table.heading('KG / Rola', text='KG / Rola')
selected_data_table.heading('New KG / Rola', text='New KG / Rola')
selected_data_table.pack(padx=20, pady=20)

# Entry for new KG / Rola
new_kg_rola = tk.StringVar(root)
entry_value = tk.Entry(root, textvariable=new_kg_rola)
entry_value.pack()

update_btn = tk.Button(root, text="Update", command=update_value)
update_btn.pack()

add_btn = tk.Button(root, text="Add", command=add_value)
add_btn.pack()

# Apply grid lines to the table
style = ttk.Style(root)
style.configure("Treeview", rowheight=25, font=('Arial', 10))  # Adjust row height and font if needed
style.configure("Treeview.Heading", font=('Arial', 10, 'bold'))  # Style for column headings
style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])  # Adding grid lines

root.mainloop()
