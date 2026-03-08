import os
import numpy as np
from flask import Flask, render_template, request
from PIL import Image
from sklearn.cluster import KMeans

UPLOAD_FOLDER = "static/uploads"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def rgb_to_hex(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))


def extract_colors(image_path, num_colors=10):
    image = Image.open(image_path)

    # Resize for faster processing
    image = image.resize((200, 200))

    image_array = np.array(image)
    pixels = image_array.reshape(-1, 3)

    kmeans = KMeans(n_clusters=num_colors, n_init=10)
    kmeans.fit(pixels)

    colors = kmeans.cluster_centers_

    hex_colors = [rgb_to_hex(color) for color in colors]

    return hex_colors


@app.route("/", methods=["GET", "POST"])
def index():
    colors = None
    image_path = None

    if request.method == "POST":
        file = request.files["image"]

        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            colors = extract_colors(filepath)
            image_path = filepath

    return render_template("index.html", colors=colors, image_path=image_path)


if __name__ == "__main__":
    app.run(debug=True)