from flask import Flask, render_template, request, flash

app_flask = Flask(__name__)
app_flask.secret_key = 'xyz'

@app_flask.route('/')
def home():
    return render_template('index.html')

@app_flask.route('/<name>/', methods=['POST', 'GET'])
def name(name):
    global crop
    if(request.method == 'POST'):
        crop = request.form['crop']
        flash(f'Now growing {crop}')
    return render_template(f'person.html', data=[name])

app_flask.run()