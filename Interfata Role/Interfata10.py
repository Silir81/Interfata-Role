import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd
import os

# Placeholder DataFrame
df = pd.DataFrame({'Tambur': [], 'KG/Rola': [], 'Nr.InternRola': []})
df_rebut = pd.DataFrame(columns=['Operator', 'ID Proiect', 'Cod Rola', 'Tip Profil', 'Lungime Profil'])
initial_headers = []
file_path_rebut = r"C:\Users\User\Desktop\Rebut.xlsx"  # Update this path as necessary

# Function to read profile types from Excel file
def get_profile_types():
    try:
        df_lista_profile = pd.read_excel(file_path_rebut, sheet_name='Lista Profile')
        return df_lista_profile.iloc[:, 0].dropna().tolist()  # Assuming profile types are in the first column
    except Exception as e:
        print(f"Error reading profile types: {e}")
        return []

# Read profile types
profile_types = get_profile_types()

# Function to display selected data
def display_selected_data(selected_tambur):
    global df
    selected_data = df[(df['Tambur'] == selected_tambur) & (df['KG/Rola'] > 0)]
    if not selected_data.empty:
        selected_data_table.delete(*selected_data_table.get_children())
        for index, row in selected_data[['Nr.InternRola', 'KG/Rola', 'Grosime']].iterrows():
            selected_data_table.insert("", tk.END, values=tuple(row))
    else:
        print(f"No data found for '{selected_tambur}'")

# Function to update value
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
            initial_index = df[
                (df['Nr.InternRola'] == selected_nr_intern_rola) & (df['KG/Rola'] == float(selected_kg_rola))].index
            if len(initial_index) > 0:
                initial_index = initial_index[0]
                df.loc[initial_index, 'KG/Rola'] = new_value
                display_selected_data(tambur_var.get())

        df.to_excel(r"C:\Users\User\Mexi Web Project\Documente Vanzari - Documents\Stoc Role 2022.xlsx", index=False,
                    columns=initial_headers)

        # Clear the entry field after updating
        new_kg_rola.set("")


# Function to open Excel
def open_excel():
    global df
    global initial_headers
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    if file_path:
        df = pd.read_excel(file_path)
        initial_headers = df.columns.tolist()

        # Get unique 'Tambur' values and sort them
        tambur_options = sorted(df['Tambur'].unique().tolist())

        tambur_var.set('Select Tambur')
        tambur_dropdown['menu'].delete(0, 'end')
        for option in tambur_options:
            tambur_dropdown['menu'].add_command(label=option, command=tk._setit(tambur_var, option))
        tambur_dropdown.config(state="normal")
        tambur_var.trace('w', lambda *args: display_selected_data(tambur_var.get()))


def save_to_excel():
    global df_rebut

    # Retrieve data from entry fields
    operator = entries["Operator"].get()
    id_proiect = entries["Project ID"].get()
    cod_rola = entries["Cod Rola"].get()
    tip_profil = entries["Tip Profil"].get()
    lungime_profil = entries["Lungime Profil"].get()

    # Create a new DataFrame for the row to be added
    new_row_df = pd.DataFrame([{
        'Operator': operator,
        'ID Proiect': id_proiect,
        'Cod Rola': cod_rola,
        'Tip Profil': tip_profil,
        'Lungime Profil': lungime_profil
    }])

    # Read all sheets from the Excel file into a dict of DataFrames
    with pd.ExcelFile(file_path_rebut) as xls:
        dfs = {sheet_name: pd.read_excel(xls, sheet_name) for sheet_name in xls.sheet_names}

    # Update the specific DataFrame (e.g., 'Sheet1')
    target_sheet_name = 'Sheet1'  # Replace with your target sheet name
    if target_sheet_name in dfs:
        updated_df = pd.concat([dfs[target_sheet_name], new_row_df], ignore_index=True)
    else:
        updated_df = new_row_df
    dfs[target_sheet_name] = updated_df

    # Write back to Excel file
    with pd.ExcelWriter(file_path_rebut, engine='openpyxl') as writer:
        for sheet_name, df_sheet in dfs.items():
            df_sheet.to_excel(writer, sheet_name=sheet_name, index=False)

    # Clear the entry fields after saving
    for field in field_names:
        entries[field].set("")

def new_button_action():
    print("New Button clicked!")

# GUI Setup
root = tk.Tk()
root.title("Registru Role")

# Create the Notebook widget
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Create a frame for the existing content
existing_content_frame = ttk.Frame(notebook)
notebook.add(existing_content_frame, text='Registru Role')

# Add existing widgets to existing_content_frame
# Move your existing widgets to this frame
btn_open_excel = tk.Button(existing_content_frame, text="Deschide Registrul Role", command=open_excel, height=2, width=20, bg='green', font=('Calibri', 12))
btn_open_excel.pack()
new_button = tk.Button(existing_content_frame, text="New Button", command=new_button_action, height=2, width=20, bg='blue', font=('Calibri', 12))
new_button.pack(pady=10)  # Adjust pady as needed for spacing


tambur_var = tk.StringVar(existing_content_frame)
tambur_var.set('Select Tambur')
tambur_dropdown = tk.OptionMenu(existing_content_frame, tambur_var, 'Select Tambur')
tambur_dropdown.pack()
tambur_dropdown.config(height=2, width=16, bg='green', font=('Calibri', 12))

new_kg_rola = tk.StringVar(existing_content_frame)
entry_value = tk.Entry(existing_content_frame, textvariable=new_kg_rola, width=16, bg='orange', font=('Calibri', 15))
entry_value.pack()

update_btn = tk.Button(existing_content_frame, text="Update", command=update_value, height=2, width=20, bg='green', font=('Calibri', 12))
update_btn.pack()

selected_data_table = ttk.Treeview(existing_content_frame, columns=('Nr.InternRola', 'KG/Rola', 'Grosime'), show='headings')
selected_data_table.heading('Nr.InternRola', text='Nr.InternRola')
selected_data_table.heading('KG/Rola', text='KG/Rola')
selected_data_table.heading('Grosime', text='Grosime')
selected_data_table.pack(padx=60, pady=60)

style = ttk.Style(existing_content_frame)
style.configure("Treeview", rowheight=25, font=('Arial', 15))
style.configure("Treeview.Heading", font=('Arial', 20, 'bold'))
style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

# Create a new frame for the new tab
new_tab_frame = ttk.Frame(notebook)
notebook.add(new_tab_frame, text='New Tab')

# Data fields for New Tab
field_names = ["Operator", "Project ID", "Cod Rola", "Tip Profil", "Lungime Profil"]
entries = {}

for field in field_names:
    frame = ttk.Frame(new_tab_frame)
    frame.pack(padx=10, pady=5, fill='x')

    label = ttk.Label(frame, text=field, font=('Calibri', 12))
    label.pack(side=tk.LEFT, padx=5, pady=5)

    if field == "Tip Profil":
        tip_profil_var = tk.StringVar()
        tip_profil_dropdown = ttk.OptionMenu(frame, tip_profil_var, profile_types[0], *profile_types)
        tip_profil_dropdown.pack(side=tk.LEFT, fill='x', expand=True)
        entries[field] = tip_profil_var
    else:
        entry_var = tk.StringVar()
        entry = ttk.Entry(frame, textvariable=entry_var, font=('Calibri', 12))
        entry.pack(side=tk.LEFT, fill='x', expand=True)
        entries[field] = entry_var

# Add a button in the new_tab_frame to trigger saving to Excel
save_btn = ttk.Button(new_tab_frame, text="Save to Excel", command=save_to_excel)
save_btn.pack(pady=10)

root.mainloop()
