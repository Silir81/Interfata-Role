import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pandas as pd
import os

# Placeholder DataFrame
df = pd.DataFrame({'Tambur': [], 'KG/Rola': [], 'Grosime': []})
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

def update_tambur_options(selected_grosime):
    global df
    tambur_options = df[df['Grosime'] == selected_grosime]['Tambur'].unique().tolist()
    tambur_var.set('Select Tambur')
    menu_tambur.delete(0, 'end')  # Correct deletion of menu items
    for option in tambur_options:
        menu_tambur.add_command(label=option, command=tk._setit(tambur_var, option))

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
                initial_index = initial_index[0]
                df.loc[initial_index, 'KG/Rola'] = new_value
                display_selected_data(tambur_var.get())
        df.to_excel(r"C:\Users\User\Desktop\Stoc Role 2022.xlsx", index=False, columns=initial_headers)

def open_excel():
    global df, initial_headers
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    if file_path:
        df = pd.read_excel(file_path)
        initial_headers = df.columns.tolist()
        grosime_options = df['Grosime'].unique().tolist()
        grosime_var.set('Select Grosime')
        menu_grosime.delete(0, 'end')  # Correct deletion of menu items
        for option in grosime_options:
            menu_grosime.add_command(label=str(option), command=tk._setit(grosime_var, str(option)))
        grosime_dropdown.config(state="normal")
        grosime_var.trace('w', lambda *args: filter_data(grosime_var.get()))

def filter_data(selected_grosime):
    global df
    if selected_grosime != 'Select Grosime':
        filtered_df = df[df['Grosime'] == selected_grosime]
        tambur_options = filtered_df['Tambur'].unique().tolist()
        tambur_var.set('Select Tambur')
        menu_tambur.delete(0, 'end')  # Correct deletion of menu items
        for option in tambur_options:
            menu_tambur.add_command(label=str(option), command=tk._setit(tambur_var, str(option)))
        tambur_dropdown.config(state="normal")
        tambur_var.trace('w', lambda *args: display_selected_data(tambur_var.get()))


file_path = r"C:\Users\User\Desktop\Stoc Role 2022.xlsx"
if os.path.exists(file_path) and not df.empty:
    df.to_excel(file_path, index=False)

# GUI Setup (update here to include filtering by Grosime)
root = tk.Tk()
root.title("Registru role")

frame = tk.Frame(root)
frame.pack()

grosime_var = tk.StringVar(root)
grosime_var.set('Select Grosime')
grosime_dropdown = tk.Menubutton(frame, textvariable=grosime_var, width=20)
grosime_dropdown.grid(row=0, column=0)

tambur_var = tk.StringVar(root)
tambur_var.set('Select Tambur')
tambur_dropdown = tk.Menubutton(frame, textvariable=tambur_var, width=20)
tambur_dropdown.grid(row=0, column=1)

menu_grosime = tk.Menu(grosime_dropdown, tearoff=False)
grosime_dropdown.configure(menu=menu_grosime)

menu_tambur = tk.Menu(tambur_dropdown, tearoff=False)
tambur_dropdown.configure(menu=menu_tambur)

btn_open_excel = tk.Button(frame, text="Deschide fisierul Excel", command=open_excel, height=3, width=20)
btn_open_excel.grid(row=1, column=0)

update_btn = tk.Button(frame, text="Update", command=update_value, height=3, width=20)
update_btn.grid(row=1, column=1)

new_kg_rola = tk.StringVar(root)
entry_value = tk.Entry(root, textvariable=new_kg_rola)
entry_value.pack()

style = ttk.Style(root)
style.configure("Treeview", rowheight=25, font=('Arial', 15))
style.configure("Treeview.Heading", font=('Arial', 20, 'bold'))
style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

selected_data_table = ttk.Treeview(root, columns=('Nr.InternRola', 'KG/Rola'), show='headings')
selected_data_table.heading('Nr.InternRola', text='Nr.InternRola')
selected_data_table.heading('KG/Rola', text='KG/Rola')
selected_data_table.pack(padx=60, pady=60)

selected_data_table.tag_configure('oddrow', background='green')
selected_data_table.tag_configure('evenrow', background='lightgray')

root.mainloop()