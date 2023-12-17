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

# Latime Rola Efectiva Frame
frame1 = tk.LabelFrame(root, text="Latime Rola Efectiva (Ex: 198 x 1.5)", padx=10, pady=10)
frame1.grid(row=0, column=0, padx=10, pady=10)

labels1 = ['Latime x Grosime', 'Tip Material', 'Id Project']
for i, label_text in enumerate(labels1):
    label = tk.Label(frame1, text=label_text)
    label.grid(row=i, column=0)
    entry = tk.Entry(frame1)
    entry.grid(row=i, column=1)

# Rebuturi Frame
frame2 = tk.LabelFrame(root, text="Rebuturi", padx=10, pady=10)
frame2.grid(row=1, column=0)

labels2 = ['Lungime profil'] * 3
for i, label_text in enumerate(labels2, start=1):
    label = tk.Label(frame2, text=f'{label_text} {i}')
    label.pack()

# Profile Neconforme Frame
frame3 = tk.LabelFrame(root, text="Profile Neconforme", padx=10, pady=10)
frame3.grid(row=1, column=1)

labels3 = ['Lungime profil'] * 3
for i, label_text in enumerate(labels3, start=4):
    label = tk.Label(frame3, text=f'{label_text} {i}')
    label.pack()

# Function to open Excel file
btn_open_excel = tk.Button(root, text="Open Excel File", command=open_excel)
btn_open_excel.grid(row=2, columnspan=2, pady=10)

root.mainloop()
