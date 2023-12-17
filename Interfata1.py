import tkinter as tk

root = tk.Tk()
root.title("Interface Example")

# Latime Rola Efectiva Frame
frame1 = tk.LabelFrame(root, text="Latime Rola Efectiva (Ex: 198 x 1.5)", padx=10, pady=10)
frame1.grid(row=0, column=0, padx=10, pady=10)

labels1 = ['Latime x Grosime', 'Tip Material', 'Id Project']
for i in range(3):
    label = tk.Label(frame1, text=labels1[i])
    label.grid(row=i, column=0)
    entry = tk.Entry(frame1)
    entry.grid(row=i, column=1)

# Rebuturi Frame
frame2 = tk.LabelFrame(root, text="Rebuturi", padx=10, pady=10)
frame2.grid(row=1, column=0)

labels2 = ['Lungime profil'] * 3
for i in range(3):
    label = tk.Label(frame2, text=f'{labels2[i]} {i+1}')
    label.pack()

# Profile Neconforme Frame
frame3 = tk.LabelFrame(root, text="Profile Neconforme", padx=10, pady=10)
frame3.grid(row=1,column=1)

labels3 = ['Lungime profil'] * 3
for i in range(3):
    label = tk.Label(frame3,text=f'{labels3[i]} {i+4}')
    label.pack()

root.mainloop()
