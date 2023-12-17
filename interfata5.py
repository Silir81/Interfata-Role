import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pandas as pd
import os

# Placeholder DataFrame
df = pd.DataFrame({'Tambur': [], 'KG / Rola': [], 'New KG / Rola': []})

# Placeholder for initial headers
initial_headers = []

# Function to display selected data
def display_selected_data(selected_tambur):
    global df
    selected_data = df[(df['Tambur'] == selected_tambur) & (df['KG / Rola'] > 0)]
    if 'Nr. Intern Rola' in df.columns:
        selected_data_table.delete(*selected_data_table.get_children())
        for index, row in selected_data[['Nr. Intern Rola', 'KG / Rola']].iterrows():
            selected_data_table.insert("", tk.END, values=tuple(row))
    else:
        print("'Nr. Intern Rola' column not found in DataFrame")

# Function to update values
def update_value():
    global df
    selected_items = selected_data_table.selection()
    new_value = new_kg_rola.get()
    if selected_items and new_value.strip():
        new_value = int(new_value)
        for selected_item in selected_items:
            item_values = selected_data_table.item(selected_item, 'values')
            df.at[selected_item, 'KG / Rola'] = new_value
            df.at[selected_item, 'New KG / Rola'] = new_value
            display_selected_data(item_values[0])

        # Save the updated DataFrame with initial headers
        df.to_excel(r"C:\Users\User\Desktop\Stoc Role 2022.xlsx", index=False, columns=initial_headers)

# Function to add values
def add_value():
    global df
    new_value = new_kg_rola.get()
    tambur = tambur_var.get()
    if new_value.strip():
        new_value = int(new_value)
        new_row = pd.Series({'Tambur': tambur, 'KG / Rola': 0, 'New KG / Rola': new_value})
        df = df.append(new_row, ignore_index=True)
        display_selected_data(tambur)

# Function to open Excel
def open_excel():
    global df
    global initial_headers
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    if file_path:
        df = pd.read_excel(file_path)
        initial_headers = df.columns.tolist()  # Get the initial column headers
        tambur_options = df['Tambur'].unique().tolist()
        tambur_var.set('Select Tambur')
        tambur_dropdown['menu'].delete(0, 'end')
        for option in tambur_options:
            tambur_dropdown['menu'].add_command(label=option, command=tk._setit(tambur_var, option))
        tambur_dropdown.config(state="normal")
        tambur_var.trace('w', lambda *args: display_selected_data(tambur_var.get()))

# Initial file path
file_path = r"C:\Users\User\Desktop\Stoc Role 2022.xlsx"

# Check if the file exists and write the initial DataFrame
if os.path.exists(file_path):
    df.to_excel(file_path, index=False)

# GUI Setup
root = tk.Tk()
root.title("Excel Data Viewer")

# Rest of the GUI setup...

root.mainloop()