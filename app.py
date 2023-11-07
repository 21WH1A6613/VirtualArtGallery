from flask import Flask, render_template, request, redirect, url_for, send_file
from PIL import Image
import os

app = Flask(__name__)

def process_images(image_dir):
    image_data = []
    for filename in os.listdir(image_dir):
        if filename.endswith(('.jpg', '.jpeg')):
            title = os.path.splitext(filename)[0]
            image_path = os.path.join(image_dir, filename)
            # Open the image and resize it
            image = Image.open(image_path)
            image.thumbnail((200, 200))  # Adjust the size as needed
            # Save the resized image with the same filename
            resized_image_path = os.path.join(image_dir, filename)
            image.save(resized_image_path)
            image_data.append({"filename": f'images/{filename}', "title": title})
    return image_data

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/art_gallery')
def art_gallery():
    image_dir = os.path.join(app.static_folder, 'images')
    image_data = process_images(image_dir)
    return render_template('art_galley.html', image_data=image_data)

@app.route('/view_image/<filename>')
def view_image(filename):
    image_dir = os.path.join(app.static_folder, 'images')
    image_path = os.path.join(image_dir, filename)
    return send_file(image_path)

if __name__ == '__main__':
    app.run(debug=True)
