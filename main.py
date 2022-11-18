from flask import Flask
from flask import request
import os

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload():
    image = request.files['image']
    image.save(os.path.join('static', image.filename))
    return image.filename


app.run()
