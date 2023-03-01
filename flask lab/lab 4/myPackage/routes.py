from flask import render_template, url_for, redirect, flash, Blueprint
from myPackage import app,db
from myPackage.forms import RegistrationForm, LoginForm
from myPackage.models import User, Post

# login imports
from flask_login import login_user, current_user, logout_user, login_required

# hashing password
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

# blueprint
users = Blueprint(
	'users',
	__name__,
	url_prefix='/users'
)

# --------------------------- routes ---------------------------
# Decorator add functionality to functions without adding code
# (.route) Decorator handles all the complicated backend stuff
# to allow us to have a function for this specific route

# Homepage Endpoint
@app.route('/')
@app.route('/home')
def home():
	result = [
	{
		'student': 'yahia',
		'grade': 10,
		'year': 2021
	},
	{
		'student': 'ahmed',
		'grade': 20,
		'year': 2020
	},
	{
		'student': 'osama',
		'grade': 30,
		'year': 2019
	}
	]
	return render_template('home.html', result=result, title="home page")

# About Endpoint
@app.route('/about')
@login_required
def about():
	return render_template('about.html', title='about page')

# Redirect Endpoint
@app.route('/redirect')
def redirectFunc():
	return redirect(url_for('home'))

# Redirect Endpoint
@app.route('/test')
def test():
	result = [
	{
		'name': 'About page',
		'url': "about"
	},
	{
		'name': 'Home page',
		'url': "home"
	},
	]
	return render_template('test.html', result=result)

@users.route('/register', methods=['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		with app.app_context():
			# pip install flask-bcrypt
			hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf8')
			new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
			db.session.add(new_user)
			db.session.commit()
		flash(f"Registration Successfull {form.username.data}", "success")
		return redirect(url_for('users.login'))

	return render_template('register.html', title='Register', form=form)

@users.route('/login', methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))

	form = LoginForm()

	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()

		# if user exists , check his password
		if user and bcrypt.check_password_hash(user.password,form.password.data):
			login_user(user)
			flash(f"Login Successfull {user.username}", "success")
			return redirect(url_for('home'))
		else:
			flash(f"Login Unsuccessfull", "danger")
			return render_template('login.html', title='Login', form=form)

	return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))