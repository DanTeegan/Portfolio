from flask import *
from functools import wraps

app = Flask(__name__)

app.secret_key = "secret key"

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/index")
def home():
    return render_template('index.html')

@app.route("/aboutme")
def aboutme():
    return render_template('aboutme.html')

@app.route("/projects")
def projects():
    return render_template('projects.html')

@app.route("/cv")
def cv():
    return render_template('cv.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True) # Good practice to add debug = true