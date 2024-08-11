Image Encryption Tool
This project is a simple image encryption tool that performs basic pixel manipulation operations on images. The tool includes functionalities for swapping pixel values and applying basic mathematical operations to each pixel. It also features a web interface built with Flask for easy interaction.

Features
Pixel Swapping: Swap red and green color channels in an image.
Mathematical Operations: Apply addition, subtraction, multiplication, or division operations to pixel values.
Web Interface: User-friendly interface to upload images and choose encryption methods.
Installation
Prerequisites
Python 3.x
pip (Python package installer)
Libraries
Install the required libraries using pip:

bash
Copy code
pip install Flask Pillow numpy
Usage
Clone the Repository

bash
Copy code
git clone https://github.com/Karthikdude/SCT_CS_2.git
cd SCT_CS_2
Run the Flask Application

bash
Copy code
python app.py
This will start a development server at http://127.0.0.1:5000.

Access the Web Interface

Open your browser and navigate to http://127.0.0.1:5000 to use the image encryption tool. You can upload an image, select an operation (pixel swap or mathematical operation), and download the encrypted image.

File Structure
/static/styles.css: Contains the CSS styles for the web interface.
/templates/index.html: HTML template for the web interface.
app.py: Flask application script with image manipulation logic.
Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any questions or suggestions, please contact Karthik S Sathyan.

