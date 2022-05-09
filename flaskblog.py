from turtle import title
from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'cb6a728ae892028ef000a95c7923c8b9'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
        {
        'author': 'Jane Doe',
        'title': 'Blog Post',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }

]

#two route being handled by the same function
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
