from flask import Flask, render_template, url_for, flash, redirect, request
from form import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy
import git
from flask_sqlalchemy import SQLAlchemy

#handle redirects
app = Flask(__name__)
proxied = FlaskBehindProxy(app)  ## add this line
app.config['SECRET_KEY'] = 'your_secret_key_here'  # replace with your actual secret key




# form page
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        # get user fields and add to database
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home')) # if so - send to home page
    return render_template('register.html', title='Register', form=form)
