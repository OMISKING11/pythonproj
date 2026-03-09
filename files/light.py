import tkinter as tk
from tkinter import ttk, messagebox
from fractions import Fraction

def calculate():
    try:
        device_type = device_var.get()
        mirror_type = mirror_var.get()

        # Get input values
        f_in = f_entry.get().strip()
        u_in = u_entry.get().strip()
        v_in = v_entry.get().strip()
        h_o_in = ho_entry.get().strip()
        h_i_in = hi_entry.get().strip()

        f = None if f_in.lower() == 'x' or f_in == '' else float(f_in)
        u = None if u_in.lower() == 'x' or u_in == '' else float(u_in)
        v = None if v_in.lower() == 'x' or v_in == '' else float(v_in)
        h_o = None if h_o_in.lower() == 'x' or h_o_in == '' else float(h_o_in)
        h_i = None if h_i_in.lower() == 'x' or h_i_in == '' else float(h_i_in)

        is_mirror = device_type == 'Mirror'

        # Apply sign conventions
        if is_mirror:
            if mirror_type == 'Concave':
                if f is not None: f = -abs(f)
                if u is not None: u = -abs(u)
            else:  # Convex mirror
                if f is not None: f = abs(f)
                if u is not None: u = -abs(u)
        else:
            if mirror_type == 'Convex':  # Convex lens
                if f is not None: f = abs(f)
                if u is not None: u = -abs(u)
            else:  # Concave lens
                if f is not None: f = -abs(f)
                if u is not None: u = -abs(u)

        # Formula calculations
        def formula(f=None, u=None, v=None, is_mirror=True):
            if is_mirror:
                if f is None:
                    return 1 / v + 1 / u
                elif v is None:
                    return 1 / (1 / f - 1 / u)
                elif u is None:
                    return 1 / (1 / f - 1 / v)
            else:
                if f is None:
                    return 1 / v - 1 / u
                elif v is None:
                    return 1 / (1 / f + 1 / u)
                elif u is None:
                    return 1 / (1 / v - 1 / f)

        def magnification(v, u, is_mirror=True):
            return (-v / u) if is_mirror else (v / u)

        result_text_string = ""

        if f is None:
            f = formula(f=None, u=u, v=v, is_mirror=is_mirror)
            result_text_string += f"Calculated focal length (f): {abs(Fraction(f).limit_denominator())} cm\n"
        elif v is None:
            v = formula(f=f, u=u, v=None, is_mirror=is_mirror)
            result_text_string += f"Calculated image distance (v): {abs(Fraction(v).limit_denominator())} cm\n"
        elif u is None:
            u = formula(f=f, u=None, v=v, is_mirror=is_mirror)
            result_text_string += f"Calculated object distance (u): {abs(Fraction(u).limit_denominator())} cm\n"

        if h_i is not None and h_o is not None:
            m = h_i / h_o
            result_text_string += f"Magnification (m = h_i/h_o): {Fraction(m).limit_denominator()}\n"
        else:
            m = magnification(v, u, is_mirror)
            result_text_string += f"Magnification (m = {'-v/u' if is_mirror else 'v/u'}): {Fraction(m).limit_denominator()}\n"
            if h_o is None and h_i is not None:
                h_o = h_i / m
                result_text_string += f"Calculated object height (h_o): {abs(Fraction(h_o).limit_denominator())} cm\n"
            elif h_i is None and h_o is not None:
                h_i = m * h_o
                result_text_string += f"Calculated image height (h_i): {abs(Fraction(h_i).limit_denominator())} cm\n"

        # Image nature
        if m > 0:
            result_text_string += "Image is Upright and Virtual.\n"
        else:
            result_text_string += "Image is Inverted and Real.\n"

        # Clear Text widget and insert new result
        output_text.configure(state='normal')
        output_text.delete('1.0', tk.END)
        output_text.insert(tk.END, result_text_string)
        output_text.configure(state='disabled')

    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# GUI setup
root = tk.Tk()
root.title("Mirror and Lens Calculator")
root.geometry("550x550")

# Dropdowns
device_var = tk.StringVar(value='Mirror')
mirror_var = tk.StringVar(value='Concave')

tk.Label(root, text="Select Device Type:").pack(pady=(10,0))
tt = ttk.Combobox(root, textvariable=device_var, values=['Mirror', 'Lens'])
tt.pack()

tk.Label(root, text="Select Type:").pack(pady=(10,0))
tm = ttk.Combobox(root, textvariable=mirror_var, values=['Concave', 'Convex'])
tm.pack()

# Input fields
tk.Label(root, text="Focal length (f) [x if unknown]:").pack(pady=(10,0))
f_entry = tk.Entry(root)
f_entry.pack()

tk.Label(root, text="Object distance (u) [x if unknown]:").pack(pady=(10,0))
u_entry = tk.Entry(root)
u_entry.pack()

tk.Label(root, text="Image distance (v) [x if unknown]:").pack(pady=(10,0))
v_entry = tk.Entry(root)
v_entry.pack()

tk.Label(root, text="Object height (h_o) [x if unknown]:").pack(pady=(10,0))
ho_entry = tk.Entry(root)
ho_entry.pack()

tk.Label(root, text="Image height (h_i) [x if unknown or optional]:").pack(pady=(10,0))
hi_entry = tk.Entry(root)
hi_entry.pack()

# Calculate button
btn = tk.Button(root, text="Calculate", command=calculate)
btn.pack(pady=15)

# Canvas container for output
canvas = tk.Canvas(root, borderwidth=1, relief="sunken", width=520, height=150)
canvas.pack(pady=(5,15))

# Scrollbar for the Text widget inside canvas
scrollbar = tk.Scrollbar(root, orient="vertical", command=lambda *args: output_text.yview(*args))
scrollbar.place(x=520, y=420, height=150)

# Text widget inside canvas for selectable output
output_text = tk.Text(canvas, height=9, width=65, wrap='word', yscrollcommand=scrollbar.set)
output_text.pack()

# Disable editing by default
output_text.configure(state='disabled')

root.mainloop()
