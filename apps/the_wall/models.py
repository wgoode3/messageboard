from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
from datetime import datetime

PASSWORD_REGEX = re.compile(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{8,}$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
	def register(self, uname, email, pw, cpw):
		message = []
		if len(uname) < 1:
			message.append('username cannot be blank')
		if len(email) < 1:
			message.append('email cannot be blank')
		if not EMAIL_REGEX.match(email):
			message.append('invalid email address')
		check = User.userManager.filter(uname=uname)
		if len(check) > 0:
			message.append('username already exists')
		check = User.userManager.filter(email=email)
		if len(check) > 0:
			message.append('email already exists')
		if len(pw) < 1:
			message.append('password cannot be blank')
		if not PASSWORD_REGEX.match(pw):
			message.append('password must be 8 characters or more with at least one capital letter, lowercase letter, and number')
		if pw != cpw:
			message.append('password does not match confirm password')

		if len(message) > 0:
			return (False, message)
		else:
			pw_hash = bcrypt.hashpw(str(pw), bcrypt.gensalt())
			user = User.userManager.create(uname=uname, email=email, pw_hash=pw_hash) 
			return (True, user, user.id, user.uname)
	
	def login(self, email, pw):
		message = []
		if len(email) < 1:
			message.append('email cannot be blank')
		if len(pw) < 1:
			message.append('password cannot be blank')
		if not PASSWORD_REGEX.match(pw):
			message.append('password must be 8 characters or more with at least one capital letter, lowercase letter, and number')
		
		if len(message) < 1:
			login = User.userManager.filter(email=email)
			if len(login) < 1:
				message.append('email not in database')
			else:
				if bcrypt.checkpw(str(pw), str(login[0].pw_hash)):
					return (True, login, login[0].id, login[0].uname)
				else:
					message.append('wrong password dude')

		return (False, message)

class PostManager(models.Manager):
	def add(self, content, user):
		if len(content) < 1:
			message = 'post cannot be blank'
			return (False, message)
		else:
			post = Post.postManager.create(user_id=user, content=content)
			return (True, post)

class CommentManager(models.Manager):
	def add(self, content, user, post):
		if len(content) < 1:
			message = 'comment cannot be blank'
			return (False, message)
		else:
			comment = Comment.commentManager.create(user_id=user, post_id=post, content=content)
			return (True, comment)

class User(models.Model):
	uname = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	pw_hash = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	userManager = UserManager()

class Post(models.Model):
	user = models.ForeignKey(User)
	content = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	postManager = PostManager()

class Comment(models.Model):
	user = models.ForeignKey(User)
	post = models.ForeignKey(Post)
	content = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	commentManager = CommentManager()