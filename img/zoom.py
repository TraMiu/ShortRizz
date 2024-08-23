import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

class ImageCropper(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Batch Image Cropper')
        self.geometry('1040x1040')

        # Default rectangle size with 9:16 aspect ratio
        self.default_width = 648
        self.default_height = 1152


        # Variables to store the coordinates
        self.start_x = None
        self.start_y = None
        self.rect = None

        # Create a canvas to display the image
        self.canvas = tk.Canvas(self, cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Controls to navigate and save
        button_frame = tk.Frame(self)
        button_frame.pack(side=tk.TOP, fill=tk.X)

        tk.Button(button_frame, text="Load Folder", command=self.load_folder).pack(side=tk.LEFT)
        tk.Button(button_frame, text="Next Image", command=self.load_next_image).pack(side=tk.LEFT)

        # Move the button frame to the top left corner
        button_frame.place(x=0, y=0)

        # List of image files
        self.images = []
        self.current_image_index = 0

        # Bind mouse events to methods
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def load_folder(self):
        folder_path = "selected"
        if not folder_path:
            return
        self.images = [os.path.join(folder_path, file) for file in os.listdir(folder_path)
                       if file.lower().endswith(('png', 'jpg', 'jpeg', 'bmp'))]
        if not self.images:
            messagebox.showerror("Error", "No image files found in the folder.")
            return
        self.current_image_index = 0
        self.load_image()

    def load_image(self):
        if 0 <= self.current_image_index < len(self.images):
            file_path = self.images[self.current_image_index]
            self.image = Image.open(file_path)
            self.tk_image = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, image=self.tk_image, anchor='nw')
            self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))
        else:
            messagebox.showinfo("End", "No more images to crop.")

    def on_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        self.update_rectangle(self.start_x, self.start_y, self.default_width, self.default_height)

    def on_drag(self, event):
        current_x = self.canvas.canvasx(event.x)
        current_y = self.canvas.canvasy(event.y)
        width = self.default_width
        height = self.default_height
        new_x = min(self.start_x, current_x)
        new_y = min(self.start_y, current_y)
        self.update_rectangle(new_x, new_y, width, height)

    def update_rectangle(self, x, y, width, height):
        if self.rect:
            self.canvas.delete(self.rect)
        self.rect = self.canvas.create_rectangle(x, y, x + width, y + height, outline='red')

    def on_release(self, event):
        if self.rect:
            bbox = self.canvas.coords(self.rect)
            bbox = [int(coord) for coord in bbox]
            cropped_img = self.image.crop(bbox)
            # cropped_img.show()  # Optionally display the cropped image
            self.save_cropped_image(cropped_img)

    def save_cropped_image(self, cropped_img):
        base_path = os.path.dirname(self.images[self.current_image_index])
        save_folder = "cropped"
        os.makedirs(save_folder, exist_ok=True)
        file_name = "cropped_" + os.path.basename(self.images[self.current_image_index])
        save_path = os.path.join(save_folder, file_name)
        cropped_img.save(save_path)
        messagebox.showinfo("Saved", f"Image saved as {file_name} in {save_folder}")

    def load_next_image(self):
        if self.current_image_index + 1 < len(self.images):
            self.current_image_index += 1
            self.load_image()
        else:
            messagebox.showinfo("End", "You have reached the end of the folder.")

if __name__ == "__main__":
    app = ImageCropper()
    app.mainloop()

