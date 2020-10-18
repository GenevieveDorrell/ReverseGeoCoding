import os
from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
from gpx_parser import get_latlon
from directions import get_directions

UPLOAD_FOLDER = 'uploads\\'
ALLOWED_EXTENSIONS = {'gpx'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        print(request.files)
        if 'file' in request.files:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                flash('we are working on your route please give us a second :)')
                latlon = get_latlon((UPLOAD_FOLDER + file.filename))
                directionsList = get_directions(latlon)
                for direction in directionsList:
                    flash(direction)
            else:
                flash('Please Upload a .gpx type file')
    return render_template('home.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/getDirections', methods=['POST', 'GET'])
def getDirections():
    return render_template('directions.html')
