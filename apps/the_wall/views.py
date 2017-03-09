from django.shortcuts import render, redirect
from .models import User, Post, Comment

def index(request):
	#renders the login and register page

 	#uncomment to nuke the databases
	# User.userManager.all().delete()
	# Post.postManager.all().delete()
	# Comment.commentManager.all().delete()

	return render(request, 'the_wall/index.html')

def register(request):
	#make request to user in model and do some validatation... returns a tuple!
	user = User.userManager.register(request.POST['uname'], request.POST['email'], request.POST['pw'], request.POST['cpw'])
	if user[0]:
		#Keep track of user in session
		request.session['user'] = (user[2], user[3])
		return redirect('/wall')
	else:
		context = {'errors': user[1]}
		return render(request, 'the_wall/index.html', context)

def login(request):
	#make request to user in model and do some validatation... returns a tuple!
	user = User.userManager.login(request.POST['email'], request.POST['pw'])
	#check user is in database
	if user[0]:
		#check user password matches password for email
		if user[1]:
			#Keep track of user in session
			request.session['user'] = (user[2], user[3])
			return redirect('/wall')
	else:
		context = {'errors': user[1]}
		return render(request, 'the_wall/index.html', context)

def logoff(request):
	#gets rid of session variables and sends them back to login page
	request.session.clear()
	return redirect('/')

def wall(request):
	#this is the place we will render all the posts and comments
	context = {'posts': Post.postManager.all().order_by('-created_at'), 'comments': Comment.commentManager.all()}
	return render(request, 'the_wall/wall.html', context)

def post(request):
	#handles making a post, renders a partial html
	Post.postManager.add(request.POST['content'], request.session['user'][0])
	context = {'posts': Post.postManager.all().order_by('-created_at'), 'comments': Comment.commentManager.all()}
	return render(request, 'the_wall/partials/wall_partial.html', context)

def comment(request, post_id):
	#handles making a comment, renders a partial html
	Comment.commentManager.add(request.POST['content'], request.session['user'][0], post_id)
	context = {'posts': Post.postManager.all().order_by('-created_at'), 'comments': Comment.commentManager.all()}
	return render(request, 'the_wall/partials/wall_partial.html', context)

def update(request):
	#this route will handle updating the page when new content is available
	context = {'posts': Post.postManager.all().order_by('-created_at'), 'comments': Comment.commentManager.all()}
	return render(request, 'the_wall/partials/wall_partial.html', context)