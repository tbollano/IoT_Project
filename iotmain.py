from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': '',
        'title': '',
        'content': '',
        'date_posted': ''
    },
    {
        'author': '',
        'title': '',
        'content': '',
        'date_posted': ''
    }
]

@app.route('/') #root page '/'
def hello_world():
    return '<h1>Hello World!<h1>'

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)