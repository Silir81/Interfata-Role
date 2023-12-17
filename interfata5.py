import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pandas as pd
import os

# Placeholder DataFrame
df = pd.DataFrame({'Tambur': [], 'KG/Rola': []})
initial_headers = []


def display_selected_data(selected_tambur):
    global df
    selected_data = df[(df['Tambur'] == selected_tambur) & (df['KG/Rola'] > 0)]
    if 'Nr.InternRola' in df.columns:
        selected_data_table.delete(*selected_data_table.get_children())
        for index, row in selected_data[['Nr.InternRola', 'KG/Rola']].iterrows():
            selected_data_table.insert("", tk.END, values=tuple(row))
    else:
        print("'Nr.InternRola' column not found in DataFrame")


def update_value():
    global df
    selected_items = selected_data_table.selection()
    new_value = new_kg_rola.get()
    if selected_items and new_value.strip():
        new_value = int(new_value)
        for selected_item in selected_items:
            item_values = selected_data_table.item(selected_item, 'values')
            selected_nr_intern_rola = item_values[0]
            selected_kg_rola = item_values[1]
            initial_index = df[(df['Nr.InternRola'] == selected_nr_intern_rola) & (df['KG/Rola'] == float(selected_kg_rola))].index
            if len(initial_index) > 0:
                # Get the first index if available
                initial_index = initial_index[0]
                df.loc[initial_index, 'KG/Rola'] = new_value
                display_selected_data(tambur_var.get())

        df.to_excel(r"C:\Users\User\Desktop\Stoc Role 2022.xlsx", index=False, columns=initial_headers)


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

file_path = r"C:\Users\User\Desktop\Stoc Role 2022.xlsx"
if os.path.exists(file_path) and not df.empty:
    df.to_excel(file_path, index=False)

# GUI Setup
root = tk.Tk()
root.title("Excel Data Viewer")
tambur_var = tk.StringVar(root)
tambur_var.set('Select Tambur')
tambur_dropdown = tk.OptionMenu(root, tambur_var, 'Select Tambur')
tambur_dropdown.pack()
btn_open_excel = tk.Button(root, text="Open Excel File", command=open_excel)
btn_open_excel.pack()
selected_data_table = ttk.Treeview(root, columns=('Nr.InternRola', 'KG/Rola'), show='headings')
selected_data_table.heading('Nr.InternRola', text='Nr.InternRola')
selected_data_table.heading('KG/Rola', text='KG/Rola')
selected_data_table.pack(padx=60, pady=60)
new_kg_rola = tk.StringVar(root)
entry_value = tk.Entry(root, textvariable=new_kg_rola)
entry_value.pack()
update_btn = tk.Button(root, text="Update", command=update_value)
update_btn.pack()
style = ttk.Style(root)
style.configure("Treeview", rowheight=25, font=('Arial', 15))
style.configure("Treeview.Heading", font=('Arial', 20, 'bold'))
style.layout("Treeview", [('Treeview.tree area', {'sticky': 'answer'})])

root.mainloop()
