from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [{
    'author': 'Person1',
    'title': 'Blog1',
    'content': 'Person1 content',
    'date_posted': 'April 1st 2019'
}, {
    'author': 'Person2',
    'title': 'Blog2',
    'content': 'Person2 content',
    'date_posted': 'April 2st 2019'

}, {
    'author': 'Person3',
    'title': 'Blog3',
    'content': 'Person3 content',
    'date_posted': 'April 3st 2019'

}, {
    'author': 'Person4',
    'title': 'Blog4',
    'content': 'Person4 content',
    'date_posted': 'April 4st 2019'

}
]


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts)


@app.route('/reg')
@app.route('/registration')
@app.route('/register')
def registration():
    return 'this is page to registration'


@app.route('/login')
def login():
    return 'this is the page to display login'


@app.route('/about')
@app.route('/me')
@app.route('/aboutme')
def aboutme():
    return render_template("aboutme.html", title="About the Author of this Blog")


if __name__ == '__main__':
    app.run()
    app.debug(True)
