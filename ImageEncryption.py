from flask import Flask, request, render_template, send_file
import os
from PIL import Image
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    file = request.files['image']
    operation = request.form.get('operation', 'swap')
    
    input_path = 'input_image.jpg'
    output_path = 'output_image.jpg'
    
    file.save(input_path)
    
    if operation == 'swap':
        swap_pixels(input_path, output_path)
    elif operation:
        value = int(request.form.get('value', 50))
        apply_math_operation(input_path, output_path, operation, value)
    
    return send_file(output_path, as_attachment=True)

def swap_pixels(image_path, output_path):
    img = Image.open(image_path)
    pixels = np.array(img)
    pixels[..., 0], pixels[..., 1] = pixels[..., 1], pixels[..., 0]
    encrypted_img = Image.fromarray(pixels)
    encrypted_img.save(output_path)

def apply_math_operation(image_path, output_path, operation='add', value=50):
    img = Image.open(image_path)
    pixels = np.array(img)
    
    if operation == 'add':
        pixels = np.clip(pixels + value, 0, 255)
    elif operation == 'subtract':
        pixels = np.clip(pixels - value, 0, 255)
    elif operation == 'multiply':
        pixels = np.clip(pixels * value, 0, 255)
    elif operation == 'divide':
        pixels = np.clip(pixels / value, 0, 255)

    encrypted_img = Image.fromarray(pixels.astype(np.uint8))
    encrypted_img.save(output_path)

if __name__ == '__main__':
    app.run(debug=True)
