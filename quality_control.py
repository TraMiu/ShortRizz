# import tkinter as tk
# from tkinter import ttk, scrolledtext, messagebox
# import json

# def load_text():
#     try:
#         with open('character.txt', 'r') as file:
#             text_editor.delete('1.0', tk.END)
#             text_editor.insert(tk.END, file.read())
#     except FileNotFoundError:
#         messagebox.showerror("Error", "The file character.txt does not exist. You may want to run design_character.py first.")
#     except Exception as e:
#         messagebox.showerror("Error", str(e))

# def save_text():
#     try:
#         with open('character.txt', 'w') as file:
#             file.write(text_editor.get('1.0', tk.END))
#     except Exception as e:
#         messagebox.showerror("Error", str(e))

# def load_dict():
#     try:
#         with open('scenes.txt', 'r') as file:
#             data = json.load(file)
#             for key, value in data.items():
#                 dict_listbox.insert(tk.END, f"{key}: {value}")
#     except FileNotFoundError:
#         messagebox.showerror("Error", "The file scenes.txt does not exist. You may want to run parse.py first.")
#     except json.JSONDecodeError:
#         messagebox.showerror("Error", "The file scenes.txt is not a valid JSON file.")
#     except Exception as e:
#         messagebox.showerror("Error", str(e))

# def save_dict():
#     try:
#         data = {}
#         items = dict_listbox.get(0, tk.END)
#         for item in items:
#             key, value = item.split(": ")
#             data[key] = value
#         with open('dict.txt', 'w') as file:
#             json.dump(data, file, indent=4)
#     except Exception as e:
#         messagebox.showerror("Error", str(e))

# app = tk.Tk()
# app.title("Quality Control GUI")

# tab_control = ttk.Notebook(app)

# # Text editor tab
# text_tab = ttk.Frame(tab_control)
# tab_control.add(text_tab, text='Character Editor')
# text_editor = scrolledtext.ScrolledText(text_tab, wrap=tk.WORD)
# text_editor.pack(expand=True, fill='both')
# load_text_button = ttk.Button(text_tab, text='Load Text', command=load_text)
# load_text_button.pack(side=tk.LEFT)
# save_text_button = ttk.Button(text_tab, text='Save Text', command=save_text)
# save_text_button.pack(side=tk.RIGHT)

# # Dictionary editor tab
# dict_tab = ttk.Frame(tab_control)
# tab_control.add(dict_tab, text='Scene Editor')
# dict_listbox = tk.Listbox(dict_tab, width=50, height=10)
# dict_listbox.pack(padx=10, pady=10)
# load_dict_button = ttk.Button(dict_tab, text='Load Dictionary', command=load_dict)
# load_dict_button.pack(side=tk.LEFT)
# save_dict_button = ttk.Button(dict_tab, text='Save Dictionary', command=save_dict)
# save_dict_button.pack(side=tk.RIGHT)

# tab_control.pack(expand=1, fill='both')

# app.mainloop()

# import tkinter as tk
# from tkinter import ttk, scrolledtext, messagebox, simpledialog
# import json

# def load_text():
#     try:
#         with open('character.txt', 'r') as file:
#             text_editor.delete('1.0', tk.END)
#             text_editor.insert(tk.END, file.read())
#     except FileNotFoundError:
#         messagebox.showerror("Error", "The file character.txt does not exist. You may want to run design_character.py first.")
#     except Exception as e:
#         messagebox.showerror("Error", str(e))

# def save_text():
#     try:
#         with open('character.txt', 'w') as file:
#             file.write(text_editor.get('1.0', tk.END))
#     except Exception as e:
#         messagebox.showerror("Error", str(e))

# def load_dict():
#     for widget in frame.winfo_children():
#         widget.destroy()
#     try:
#         with open('scenes.txt', 'r') as file:
#             data = json.load(file)
#             for i, (key, value) in enumerate(data.items()):
#                 tk.Label(frame, text=key, anchor="w", width=20).grid(row=i, column=0)
#                 entry = tk.Entry(frame, width=30)
#                 entry.grid(row=i, column=1)
#                 entry.insert(tk.END, value)
#                 entries[key] = entry
#     except FileNotFoundError:
#         messagebox.showerror("Error", "The file scenes.txt does not exist. You may want to run parse.py first.")
#     except json.JSONDecodeError:
#         messagebox.showerror("Error", "The file scenes.txt is not a valid JSON file.")
#     except Exception as e:
#         messagebox.showerror("Error", str(e))

# def save_dict():
#     try:
#         data = {}
#         for key, entry in entries.items():
#             data[key] = entry.get()
#         with open('scenes.txt', 'w') as file:
#             json.dump(data, file, indent=4)
#     except Exception as e:
#         messagebox.showerror("Error", str(e))

# app = tk.Tk()
# app.title("Quality Control GUI")
# entries = {}

# tab_control = ttk.Notebook(app)

# # Text editor tab
# text_tab = ttk.Frame(tab_control)
# tab_control.add(text_tab, text='Character Editor')
# text_editor = scrolledtext.ScrolledText(text_tab, wrap=tk.WORD)
# text_editor.pack(expand=True, fill='both')
# load_text_button = ttk.Button(text_tab, text='Load Text', command=load_text)
# load_text_button.pack(side=tk.LEFT)
# save_text_button = ttk.Button(text_tab, text='Save Text', command=save_text)
# save_text_button.pack(side=tk.RIGHT)

# # Dictionary editor tab
# dict_tab = ttk.Frame(tab_control)
# tab_control.add(dict_tab, text='Scene Editor')
# frame = tk.Frame(dict_tab)
# frame.pack(expand=True, fill='both', padx=10, pady=10)
# load_dict_button = ttk.Button(dict_tab, text='Load Dictionary', command=load_dict)
# load_dict_button.pack(side=tk.LEFT)
# save_dict_button = ttk.Button(dict_tab, text='Save Dictionary', command=save_dict)
# save_dict_button.pack(side=tk.RIGHT)

# tab_control.pack(expand=1, fill='both')

# app.mainloop()

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import json

def load_text():
    try:
        with open('character.txt', 'r') as file:
            text_editor.delete('1.0', tk.END)
            text_editor.insert(tk.END, file.read())
    except FileNotFoundError:
        messagebox.showerror("Error", "The file character.txt does not exist. You may want to run design_character.py first.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def save_text():
    try:
        with open('character.txt', 'w') as file:
            file.write(text_editor.get('1.0', tk.END))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def load_dict():
    # Clear existing entries in the GUI
    for widget in frame.winfo_children():
        widget.destroy()
    # Attempt to load and display data from scenes.txt
    try:
        with open('scenes.txt', 'r') as file:
            data = json.load(file)
            # Create GUI elements for each key-value pair
            for i, (key, value) in enumerate(data.items()):
                tk.Label(frame, text=key, anchor="w", width=100).grid(row=2*i, column=0, sticky="w")
                entry = tk.Entry(frame, width=100)
                entry.grid(row=2*i+1, column=0, sticky="w")
                entry.insert(tk.END, value)
                entries[key] = entry
                # Configure the column to expand with the content
                frame.columnconfigure(0, weight=1)
                # Configure the row to expand with the content
                frame.rowconfigure(2*i+1, weight=1)
    except FileNotFoundError:
        messagebox.showerror("Error", "The file scenes.txt does not exist. You may want to run parse.py first.")
    except json.JSONDecodeError:
        messagebox.showerror("Error", "The file scenes.txt is not a valid JSON file.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def save_dict():
    try:
        data = {}
        # Collect data from entries and update the dictionary
        for key, entry in entries.items():
            data[key] = entry.get()
        with open('scenes.txt', 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        messagebox.showerror("Error", str(e))

app = tk.Tk()
app.title("Quality Control GUI")
entries = {}

tab_control = ttk.Notebook(app)

# Text editor tab
text_tab = ttk.Frame(tab_control)
tab_control.add(text_tab, text='Character Editor')
text_editor = scrolledtext.ScrolledText(text_tab, wrap=tk.WORD)
text_editor.pack(expand=True, fill='both')
load_text_button = ttk.Button(text_tab, text='Load Text', command=load_text)
load_text_button.pack(side=tk.LEFT)
save_text_button = ttk.Button(text_tab, text='Save Text', command=save_text)
save_text_button.pack(side=tk.RIGHT)

# Dictionary editor tab
dict_tab = ttk.Frame(tab_control)
tab_control.add(dict_tab, text='Scene Editor')
canvas = tk.Canvas(dict_tab)
scrollbar = ttk.Scrollbar(dict_tab, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

frame = tk.Frame(scrollable_frame)
frame.pack(padx=10, pady=10)

load_dict_button = ttk.Button(dict_tab, text='Load Dictionary', command=load_dict)
load_dict_button.pack(side=tk.LEFT)
save_dict_button = ttk.Button(dict_tab, text='Save Dictionary', command=save_dict)
save_dict_button.pack(side=tk.RIGHT)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

tab_control.pack(expand=1, fill='both')

app.mainloop()
