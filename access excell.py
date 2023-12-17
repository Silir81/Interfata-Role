import tkinter as tk
from tkinter import filedialog
import pandas as pd

def open_excel():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    if file_path:
        df = pd.read_excel(file_path)  # Read the Excel file into a DataFrame
        # Perform operations with the DataFrame as needed
        print(df)  # For demonstration purposes, printing the DataFrame contents

root = tk.Tk()
root.title("Interface Example")

# Function to open Excel file
btn_open_excel = tk.Button(root, text="Open Excel File", command=open_excel)
btn_open_excel.pack()

root.mainloop()
