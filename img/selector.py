import tkinter as tk
from tkinter import Label, Checkbutton, IntVar, Button
from PIL import Image, ImageTk
import json
import os
import shutil

# Load phrases data from json file
with open('..\scenes.txt') as f:
    data = json.load(f)
transcripts = list(data.keys())

# Generate image paths
image_paths = []
for i in range(len(transcripts)*4):
    image_paths.append(f"output/{i}.jpeg")

selected_images = []
checkboxes = []
phrase_index = 0

# code to clear all jpeg files in the selected folder
for i in range(100):
    try:
        os.remove("selected/"+str(i)+".jpeg")
    except:
        pass

def show_transcript(index):
    # Clear previous content
    for widget in frame.winfo_children():
        widget.destroy()

    # Display transcript
    transcript_label = Label(frame, text=f"{transcript_index+1}/{len(transcripts)} "+transcripts[index], wraplength=300)
    transcript_label.pack()

    # Display images corresponding to the transcript
    start = index * 4
    end = start + 4
    for i in range(start, end):
        try:
            img = Image.open(image_paths[i])
            img = img.resize((150, 150))
            photo = ImageTk.PhotoImage(img)
            chk_val = IntVar()
            chk = Checkbutton(frame, image=photo, variable=chk_val, onvalue=i, offvalue=-2)
            chk.photo = photo  # Keep a reference to prevent garbage-collection
            chk.pack(side="left", padx=10, pady=10)
            checkboxes.append((chk, chk_val))
        except Exception as e:
            print("Error loading image:", e)

def save_selection():
    selected_images.clear()  # Clear previous selections

    for chk, chk_val in checkboxes:
        value = chk_val.get()
        if value != 0:
            selected_images.append(image_paths[value])

    print("Selected images:", selected_images)



def write_to_folder():
    output_folder = 'selected'
    os.makedirs(output_folder, exist_ok=True)
    global selected_images
    # If user not choose 0.jpeg for the first time
    if(len(selected_images) > len(transcripts)):
        selected_images = selected_images[1:]
    elif(len(selected_images) < len(transcripts)):
        selected_images = selected_images + [image_paths[0]]

    for img_path in selected_images:
        try:
            shutil.copy(img_path, output_folder)
            print(f"Copied {img_path} to {output_folder}")
        except Exception as e:
            print(f"Error copying {img_path}:", e)

# Create main window
root = tk.Tk()
root.title("Image Selector")

# Frame for content
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

# Buttons for navigation
btn_frame = tk.Frame(root)
btn_frame.pack(fill='x')
transcript_index = 0

def next_transcript():
    global transcript_index
    transcript_index = (transcript_index + 1) % len(transcripts)
    show_transcript(transcript_index)

show_transcript(transcript_index)

next_btn = Button(btn_frame, text="Next", command=next_transcript)
next_btn.pack(side="right")

save_btn = Button(btn_frame, text="Save Selection", command=save_selection)
save_btn.pack(side="right")

write_btn = Button(btn_frame, text="Write to Folder", command=write_to_folder)
write_btn.pack(side="left")

root.mainloop()
