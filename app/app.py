from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('landing.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/officers')
def officers():
    return render_template('officers.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/sponsors')
def sponsors():
    return render_template('sponsors.html')

if __name__ == '__main__':
    app.run(debug=True)