import os
from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
from gpx_parser import get_latlon
from directions import get_directions

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'gpx'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/', methods=['POST', 'GET'])#home page
def home():
    flash('Upload a .gpx file')
    flash('It may take us a second to calucalte your route so please be patient')
    if request.method == 'POST': # is activated when a file is uploaded
        if 'file' in request.files:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename) # security protocol
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) # save uploaded file
                flash('we are working on your route please give us a second :)')
                latlon = get_latlon((UPLOAD_FOLDER + "/" + file.filename)) # parse file
                flash('okay here are your directions happy travels')
                directionsList = get_directions(latlon) # calcualte directions
                for direction in directionsList:
                    flash(direction) #display directions
                os.remove((UPLOAD_FOLDER + "/" + file.filename)) # remove uploaded file
            else:
                flash('Please Upload a .gpx type file')
    return render_template('home.html')

def allowed_file(filename): #checks if it is the correct file type
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
