# import tkinter as tk
# from tkinter import ttk, scrolledtext, messagebox
# import json

# def load_text():
#     try:
#         with open('character.txt', 'r') as file:
#             print("reach load text:", file.read())
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
#     global prompts, current_key_index, prompt_fixes
#     try:
#         with open('scenes.txt', 'r') as file:
#             data = json.load(file)
#             with open('character.txt') as f:
#                 character = f.read()

#             scenes = list(data.values())
#             scripts = list(data.keys())
#             name = input("Enter the character's name: ")

#             prompts = {}
#             prompt_fixes = {}
#             for i in range(len(scenes)):
#                 scene = scenes[i]
#                 scene = scene.replace(name, character)
#                 prompts[scripts[i]] = scene
#                 if "'s" in scene:
#                     prompt_fixes[scripts[i]] = scene

#             current_key_index = 0
#             show_current_prompt()
#     except FileNotFoundError:
#         messagebox.showerror("Error", "The file scenes.txt does not exist. You may want to run parse.py first.")
#     except json.JSONDecodeError:
#         messagebox.showerror("Error", "The file scenes.txt is not a valid JSON file.")
#     except Exception as e:
#         messagebox.showerror("Error", str(e))

# def show_current_prompt():
#     global current_key_index
#     if prompt_fixes:
#         current_key = list(prompt_fixes.keys())[current_key_index]
#         current_value = prompt_fixes[current_key]
#         key_label.config(text=f"Script: {current_key}")
#         text_editor.config(state=tk.NORMAL)
#         text_editor.delete('1.0', tk.END)
#         text_editor.insert(tk.END, current_value)
#         text_editor.config(state=tk.DISABLED)

# def save_current_prompt():
#     global current_key_index
#     if prompts and prompt_fixes:
#         current_key = list(prompt_fixes.keys())[current_key_index]
#         current_value = text_editor.get('1.0', tk.END).strip()
#         prompts[current_key] = current_value

# def next_prompt():
#     global current_key_index
#     if prompts:
#         save_current_prompt()
#         current_key_index += 1
#         if current_key_index < len(prompt_fixes):
#             show_current_prompt()
#         else:
#             messagebox.showinfo("Info", "All prompts have been processed.")
#             # Optionally, save the updated prompts to a file
#             save_dict()

# def save_dict():
#     try:
#         with open('scenes_edited.txt', 'w') as file:
#             json.dump(prompts, file, indent=4)
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
# key_label = ttk.Label(dict_tab, text="Script:")
# key_label.pack(padx=10, pady=5)
# text_editor = scrolledtext.ScrolledText(dict_tab, wrap=tk.WORD, width=50, height=10)
# text_editor.pack(padx=10, pady=10)
# load_dict_button = ttk.Button(dict_tab, text='Load Dictionary', command=load_dict)
# load_dict_button.pack(side=tk.LEFT)
# next_button = ttk.Button(dict_tab, text='Next', command=next_prompt)
# next_button.pack(side=tk.LEFT)
# save_dict_button = ttk.Button(dict_tab, text='Save Dictionary', command=save_dict)
# save_dict_button.pack(side=tk.RIGHT)

# tab_control.pack(expand=1, fill='both')

# app.mainloop()


import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, simpledialog
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
    global prompts, current_key_index, prompt_fixes
    character = text_editor.get('1.0', tk.END).strip()
    
    try:
        with open('scenes.txt', 'r') as file:
           
            data = json.load(file)
            scenes = list(data.values())
            scripts = list(data.keys())

            name_entry.delete(0, tk.END)
            name_entry.insert(0, simpledialog.askstring("Input", "Enter the character's name:"))
            name = name_entry.get()
            prompts = {}
            prompt_fixes = {}
            for i in range(len(scenes)):
                scene = scenes[i]
                scene = scene.replace(name, character)
                scene = scene.replace("'s", "and his/her")
                prompts[scripts[i]] = scene
                prompt_fixes[scripts[i]] = scene

            current_key_index = 0
            show_current_prompt()
    except FileNotFoundError:
        messagebox.showerror("Error", "The file scenes.txt does not exist. You may want to run parse.py first.")
    except json.JSONDecodeError:
        messagebox.showerror("Error", "The file scenes.txt is not a valid JSON file.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def show_current_prompt():
    global current_key_index
    if prompt_fixes:
        current_key = list(prompt_fixes.keys())[current_key_index]
        current_value = prompt_fixes[current_key]
        key_label.config(text=f"{SCENE_EDITOR_GUIDANCE} \nScript: {current_key}")
        dict_editor.delete('1.0', tk.END)
        dict_editor.insert(tk.END, current_value)
def save_current_prompt():
    global current_key_index
    if prompts and prompt_fixes:
        current_key = list(prompt_fixes.keys())[current_key_index]
        current_value = dict_editor.get('1.0', tk.END).strip()
        prompts[current_key] = current_value

def next_prompt():
    global current_key_index
    if prompts:
        save_current_prompt()
        current_key_index += 1
        if current_key_index < len(prompt_fixes):
            show_current_prompt()
        else:
            messagebox.showinfo("Info", "All prompts have been processed.")
            # Optionally, save the updated prompts to a file
            # save_dict()

def save_dict():
    try:
        # data = {}
        # for key, entry in entries.items():
        #     data[key] = entry.get()
        with open('scenes.txt', 'w') as file:
            #file.write(prompts)
            json.dump(prompts, file, indent=4)
        messagebox.showinfo("Info", "Saved to file.")
           #json.dump(data, file, indent=4)
    except Exception as e:
        messagebox.showerror("Error", str(e))

app = tk.Tk()
app.title("Quality Control GUI")
entries = {}

tab_control = ttk.Notebook(app)

CHARACTER_EDITOR_GUIDANCE = """
Make sure the description is short (with "," to describe the character's features) and no mouth expression (smile).
"""

# Text editor tab
text_tab = ttk.Frame(tab_control)
tab_control.add(text_tab, text='Character Editor')
character_label = ttk.Label(text_tab, text=CHARACTER_EDITOR_GUIDANCE)
character_label.pack(padx=10, pady=5)
text_editor = scrolledtext.ScrolledText(text_tab, wrap=tk.WORD)
text_editor.pack(expand=True, fill='both')
load_text_button = ttk.Button(text_tab, text='Load Text', command=load_text)
load_text_button.pack(side=tk.LEFT)
save_text_button = ttk.Button(text_tab, text='Save Text', command=save_text)
save_text_button.pack(side=tk.RIGHT)


SCENE_EDITOR_GUIDANCE = """Guidance:
1. Load the dictionary from scenes.txt.
2. Enter the character's name in the input box.
3. Review and edit the script in the text box.
4. Click 'Next' to move to the next script.
5. Click 'Save Dictionary' to save the updated dictionary to scenes.txt.

Make sure the description is illustrative and detailed for the script.
"""
# Dictionary editor tab
dict_tab = ttk.Frame(tab_control)
tab_control.add(dict_tab, text='Scene Editor')
name_label = ttk.Label(dict_tab, text="Input name:")
name_label.pack(padx=10, pady=5)
name_entry = tk.Entry(dict_tab)
name_entry.pack(padx=10, pady=5)

key_label = ttk.Label(dict_tab, text=SCENE_EDITOR_GUIDANCE+"\nScript:")
key_label.pack(padx=10, pady=5)
dict_editor = scrolledtext.ScrolledText(dict_tab, wrap=tk.WORD)
dict_editor.pack(expand=True, fill='both')
load_dict_button = ttk.Button(dict_tab, text='Load Dictionary', command=load_dict)
load_dict_button.pack(side=tk.LEFT)
next_button = ttk.Button(dict_tab, text='Next', command=next_prompt)
next_button.pack(side=tk.LEFT)
save_dict_button = ttk.Button(dict_tab, text='Save Dictionary', command=save_dict)
save_dict_button.pack(side=tk.RIGHT)

tab_control.pack(expand=1, fill='both')

app.mainloop()

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
#     # Clear existing entries in the GUI
#     for widget in frame.winfo_children():
#         widget.destroy()
#     # Attempt to load and display data from scenes.txt
#     try:

#         with open('scenes.txt', 'r') as file:
#             data = json.load(file)
#             with open('character.txt') as f:
#                 character = f.read()
#             print(character)

#             scenes = list(data.values())
#             scripts = list(data.keys())
#             name = input("Enter the character's name: ")
#             # for each scene, replace the character name with given description in string
#             prompts = dict()
#             for i in range(len(scenes)):
#                 scene = scenes[i]
#                 scene = scene.replace(name, character)
#                 prompts[scripts[i]] = scene
                
                

#             print (prompts)
            
#             # Create GUI elements for each key-value pair
#             for i, (key, value) in enumerate(prompts.items()):
#                 if "'s" in value: 
#                     tk.Label(frame, text=key, anchor="w", width=100).grid(row=2*i, column=0, sticky="w")
#                     for key, value in data.items():
# #                 dict_listbox.insert(tk.END, f"{key}: {value}")
#                     entry = tk.Entry(frame, width=100)
#                     entry.grid(row=2*i+1, column=0, sticky="w")
#                     entry.insert(tk.END, value)
#                     entries[key] = entry
#                     # Configure the column to expand with the content
#                     frame.columnconfigure(0, weight=1)
#                     # Configure the row to expand with the content
#                     frame.rowconfigure(2*i+1, weight=1)
#     except FileNotFoundError:
#         messagebox.showerror("Error", "The file scenes.txt does not exist. You may want to run parse.py first.")
#     except json.JSONDecodeError:
#         messagebox.showerror("Error", "The file scenes.txt is not a valid JSON file.")
#     except Exception as e:
#         messagebox.showerror("Error", str(e))

# def save_dict():
#     try:
#         data = {}
#         # Collect data from entries and update the dictionary
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
# canvas = tk.Canvas(dict_tab)
# scrollbar = ttk.Scrollbar(dict_tab, orient="vertical", command=canvas.yview)
# scrollable_frame = ttk.Frame(canvas)

# scrollable_frame.bind(
#     "<Configure>",
#     lambda e: canvas.configure(
#         scrollregion=canvas.bbox("all")
#     )
# )

# canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
# canvas.configure(yscrollcommand=scrollbar.set)

# frame = tk.Frame(scrollable_frame)
# frame.pack(padx=10, pady=10)

# load_dict_button = ttk.Button(dict_tab, text='Load Dictionary', command=load_dict)
# load_dict_button.pack(side=tk.LEFT)
# save_dict_button = ttk.Button(dict_tab, text='Save Dictionary', command=save_dict)
# save_dict_button.pack(side=tk.RIGHT)

# canvas.pack(side="left", fill="both", expand=True)
# scrollbar.pack(side="right", fill="y")

# tab_control.pack(expand=1, fill='both')

# app.mainloop()
