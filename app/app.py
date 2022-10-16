from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/landing')
@app.route('/home')
def index():
    return render_template('landing.html')  # index.html is our landing page


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
