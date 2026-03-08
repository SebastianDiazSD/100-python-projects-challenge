import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk

# ----------------------------
# Global Variables
# ----------------------------

image_path = None
image = None
preview_image = None

# ----------------------------
# Upload Image
# ----------------------------

def upload_image():
    global image_path, image

    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )

    if file_path:
        image_path = file_path
        image = Image.open(file_path)

        show_preview(image)


# ----------------------------
# Preview Image
# ----------------------------

def show_preview(img):
    global preview_image

    resized = img.copy()
    resized.thumbnail((400, 400))

    preview_image = ImageTk.PhotoImage(resized)

    canvas.create_image(200, 200, image=preview_image)


# ----------------------------
# Add Watermark
# ----------------------------

def add_watermark():
    global image

    if image is None:
        messagebox.showerror("Error", "Please upload an image first.")
        return

    watermark_text = watermark_entry.get()

    if watermark_text == "":
        messagebox.showerror("Error", "Enter watermark text.")
        return

    watermarked = image.copy()

    draw = ImageDraw.Draw(watermarked)

    width, height = watermarked.size

    try:
        font = ImageFont.truetype("arial.ttf", int(width / 20))
    except:
        font = ImageFont.load_default()

    text_width, text_height = draw.textbbox((0, 0), watermark_text, font=font)[2:]

    position = (width - text_width - 20, height - text_height - 20)

    draw.text(
        position,
        watermark_text,
        fill=(255, 255, 255, 180),
        font=font
    )

    show_preview(watermarked)

    image_with_watermark[0] = watermarked


# ----------------------------
# Save Image
# ----------------------------

def save_image():
    if image_with_watermark[0] is None:
        messagebox.showerror("Error", "Add a watermark first.")
        return

    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG file", "*.png"), ("JPEG file", "*.jpg")]
    )

    if save_path:
        image_with_watermark[0].save(save_path)
        messagebox.showinfo("Success", "Image saved successfully! 🇨🇴")


# ----------------------------
# GUI
# ----------------------------

window = tk.Tk()
window.title("Watermark App – Hecho en Colombia 🇨🇴")
window.geometry("500x650")
window.config(padx=20, pady=20)

image_with_watermark = [None]

# Title
title_label = tk.Label(
    window,
    text="Watermark App",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=10)

subtitle = tk.Label(
    window,
    text="Add your watermark automatically\nInspired by Colombian builders 🇨🇴",
    font=("Arial", 10)
)
subtitle.pack(pady=5)

# Canvas preview
canvas = tk.Canvas(window, width=400, height=400, bg="lightgray")
canvas.pack(pady=10)

# Upload button
upload_button = tk.Button(
    window,
    text="Upload Image",
    command=upload_image,
    width=20
)
upload_button.pack(pady=5)

# Watermark text
watermark_entry = tk.Entry(window, width=35)
watermark_entry.insert(0, "sebastiandiaz.dev | Hecho en Colombia 🇨🇴")
watermark_entry.pack(pady=10)

# Add watermark
watermark_button = tk.Button(
    window,
    text="Add Watermark",
    command=add_watermark,
    width=20
)
watermark_button.pack(pady=5)

# Save button
save_button = tk.Button(
    window,
    text="Save Image",
    command=save_image,
    width=20
)
save_button.pack(pady=20)

window.mainloop()