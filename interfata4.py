import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pandas as pd
import os

# Placeholder DataFrame
df = pd.DataFrame({'Tambur': [], 'KG / Rola': [], 'New KG / Rola': []})

def display_selected_data(selected_tambur):
    global df
    selected_data = df[(df['Tambur'] == selected_tambur) & (df['KG / Rola'] > 0)]
    if 'Nr. Intern Rola' in df.columns:
        selected_data_table.delete(*selected_data_table.get_children())
        for index, row in selected_data[['Nr. Intern Rola


def update_value():
    global df
    selected_items = selected_data_table.selection()
    new_value = new_kg_rola.get()
    if selected_items and new_value.strip():
        new_value = int(new_value)
        for selected_item in selected_items:
            item_values = selected_data_table.item(selected_item, 'values')
            df.at[selected_item, 'KG / Rola'] = new_value  # Replace 'KG / Rola' with the new value
            df.at[selected_item, 'New KG / Rola'] = new_value
            display_selected_data(item_values[0])

        # Save the modified DataFrame back to the Excel file
        if os.path.exists(file_path):
            with pd.ExcelWriter(file_path, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                df.to_excel(writer, index=False, header=False)
        else:
            print("The file does not exist.")

# Rest of the code remains unchanged


# Rest of the code remains unchanged


def add_value():
    global df
    new_value = new_kg_rola.get()
    tambur = tambur_var.get()
    if new_value.strip():
        new_value = int(new_value)
        new_row = pd.Series({'Tambur': tambur, 'KG / Rola': 0, 'New KG / Rola': new_value})
        df = df.append(new_row, ignore_index=True)
        display_selected_data(tambur)

def open_excel():
    global df
    global tambur_dropdown

    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    if file_path:
        df = pd.read_excel(file_path)
        tambur_options = df['Tambur'].unique().tolist()
        print(tambur_options)  # Check the contents of tambur_options

        tambur_var.set('Select Tambur')
        tambur_dropdown['menu'].delete(0, 'end')
        for option in tambur_options:
            tambur_dropdown['menu'].add_command(label=option, command=tk._setit(tambur_var, option))
        tambur_dropdown.config(state="normal")
        tambur_var.trace('w', lambda *args: display_selected_data(tambur_var.get()))

# Check if the Excel file exists
file_path = r"C:\Users\User\Desktop\Stoc Role 2022.xlsx"
if os.path.exists(file_path):
    df = pd.read_excel(file_path)

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

new_kg_rola = tk.StringVar(root)
entry_value = tk.Entry(root, textvariable=new_kg_rola)
entry_value.pack()

update_btn = tk.Button(root, text="Update", command=update_value)
update_btn.pack()

add_btn = tk.Button(root, text="Add", command=add_value)
add_btn.pack()

style = ttk.Style(root)
style.configure("Treeview", rowheight=25, font=('Arial', 10))
style.configure("Treeview.Heading", font=('Arial', 10, 'bold'))
style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

root.mainloop()
