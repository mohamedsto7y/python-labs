# RUN THIS FILE WITH python test.py read_users
from myPackage import db,app
import sys
from myPackage.models import User, Post

# create database
def create_db():
	with app.app_context():
		# you will have instance folder with site.db inside
		db.create_all()

# -------------------------- CRUD OPERATIONS --------------------------
# Create operation
def create_users():
	with app.app_context():
		user = User(username='Yahia2', email='yahia2@gmail.com', password='123')
		db.session.add(user)
		db.session.commit()

# Create operation
def create_posts():
	with app.app_context():
		user = User.query.filter_by(username="yahia123").first()
		post1 = Post(title='testtitle', content='testcontent', user_id=user.id)
		post2 = Post(title='testtitle2', content='testcontent2', user_id=user.id)
		db.session.add(post1)
		db.session.add(post2)
		db.session.commit()

# Read operation
def read_users():
	with app.app_context():
		user = User.query.first()
		print(f"user is {user.username}")
		for post in user.posts:
			print(f"Post : {post.title}")

# Join queries
def read_join():
	with app.app_context():
		query = db.session.query(
			Post,
			User
			)\
			.join(User, Post.user_id == User.id)\
			.filter(User.email == "yahia@gmail.com")\
			.order_by(Post.id.asc())\
			.all()

		for record in query:
			print(f"id : {record.Post.id}")
			print(f"title : {record.Post.title}")
			print(f"content : {record.Post.content}")
			print(f"user email : {record.User.email}\n")

# Update operation
def update_users():
	with app.app_context():
		print("Get Specific user")
		user = User.query.filter_by(username="Yahia2").first()
		print(user)
		user.email = 'asd@gmail.com'
		db.session.commit()
		user = User.query.filter_by(username="Yahia2").first()
		print("\nAfter Change")
		print(user)

# Delete operation
def delete_users():
	with app.app_context():
		users = User.query.all()
		print(users)

		user = User.query.filter_by(username="Yahia2").first()
		db.session.delete(user)
		db.session.commit()

		users = User.query.all()
		print(users)

# snippet to allow us to run funcs from terminal with "python test.py print_func"
if __name__ == '__main__':
	globals()[sys.argv[1]]()