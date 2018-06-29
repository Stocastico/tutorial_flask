from flask import render_template, flash, redirect
from first_app import app
from first_app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Stefano'}
    posts = [
    {
        'author': {'username': 'John'},
        'body': 'Bla bla bla'
    },
    {
        'author': {'username': 'Susan'},
        'body': 'Foo bar baz'
    },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(('Login requested for user {}, remember_me={}'.format(
                form.username.data, form.remember_me.data)))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
