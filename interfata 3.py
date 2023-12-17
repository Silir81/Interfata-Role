import tkinter as tk
from tkinter import filedialog
import pandas as pd

def open_excel():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    if file_path:
        df = pd.read_excel(file_path)  # Read the Excel file into a DataFrame
        for i, column in enumerate(excel_columns):
            entry = entries[i]
            entry.delete(0, tk.END)  # Clear the entry field
            entry.insert(tk.END, df[column].iloc[0])  # Insert data from DataFrame into entry field

root = tk.Tk()
root.title("Excel Data Viewer")

# Get the column names from the Excel file
excel_columns = ['Tambur', 'KG / Rola', 'Nr. Intern Rola', 'Latime x Grosime Efectiva', 'Locatie Depozit']

# Create labels, entries, and store entries in a list
entries = []
for i, column in enumerate(excel_columns):
    label = tk.Label(root, text=column)
    label.grid(row=i, column=0)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1)
    entries.append(entry)

# Button to open Excel file
btn_open_excel = tk.Button(root, text="Open Excel File", command=open_excel)
btn_open_excel.grid(row=len(excel_columns), columnspan=2, pady=10)

root.mainloop()
