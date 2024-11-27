import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from graph import ld, plt_d


# Open file dialog and load data
def op_f():
    f = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if f:
        d = ld(f)
        if d is not None:
            sel_col(d)


# Column selection window
def sel_col(d):
    w = tk.Toplevel()
    w.title("Select Columns")
    w.geometry("500x500")

    # Instruction label
    tk.Label(w, text="Select columns for the graph:", font=("Arial", 12)).pack(pady=10)

    # Columns list
    cols = d.columns.tolist()

    # X-axis dropdown
    tk.Label(w, text="X-Axis:", font=("Arial", 10)).pack()
    x = tk.StringVar(value=cols[0])
    x_menu = ttk.Combobox(w, textvariable=x, values=cols, state="readonly")
    x_menu.pack(pady=5)

    # Y-axis checkboxes
    tk.Label(w, text="Y-Axis (Select one or more):", font=("Arial", 10)).pack()
    y = {c: tk.BooleanVar(value=False) for c in cols}
    for c in cols:
        ttk.Checkbutton(w, text=c, variable=y[c]).pack(anchor="w")

    # Confirm button
    def cf():
        x_col = x.get()
        y_cols = [c for c, v in y.items() if v.get()]
        if x_col and y_cols:
            w.destroy()
            plt_d(d, x_col, y_cols)
        else:
            messagebox.showwarning("No Selection", "Select X-axis and at least oneY-axis column.")

    ttk.Button(w, text="Plot Graph", command=cf).pack(pady=20)


# Main GUI
def gui():
    r = tk.Tk()
    r.title("Data Visualizer")
    r.geometry("600x400")

    tk.Label(
        r,
        text="Select CSV fil to visuaize data.\nChoose X and Y axes for plottin.",
        font=("Arial", 12),
        justify="center",
    ).pack(pady=20)

    ttk.Button(r, text="Open CSV", command=op_f).pack(pady=10)

    r.mainloop()


if __name__ == "__main__":
    gui()
