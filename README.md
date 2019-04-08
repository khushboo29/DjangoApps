# DjangoApps
Full-Featured Web App with Django

django-admin
django-admin startproject django_project
python manage.py runserver
http://127.0.0.1:8000/
http://127.0.0.1:8000/admin/
python manage.py startapp blog
http://127.0.0.1:8000/blog
http://127.0.0.1:8000/blog/about/
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
	cred: username: khushboo29
		pwd: testing@123
	username: TestUser
		pwd: testing@123
python manage.py makemigrations blog
python manage.py sqlmigrate blog 0001
python manage.py migrate
python manage.py shell
>>> from django.contrib.auth.models import User
>>> from blog.models import Post
>>> User.objects.all()
>>> User.objects.first()
>>> User.objects.last()
>>> User.objects.filter(username='TestUser')
>>> User.objects.filter(username='TestUser').first()
>>> user = User.objects.filter(username='TestUser').first()
>>> user.id
>>> User.objects.get(id=1)
Post.objects.all()
post_1 = Post(title='Blog 1',author=user,content='First Post content')
post_1.save()
Post.objects.all()
post_2 = Post(title='Blog 2',author=user,content='Second Post content')
post_1.save()
Post.objects.all()
#filter the post written by particular user
.modelsname_set
user.post_set
user.post_set.all()
user.post_set.create(title='Blog 3',content='Third Post content')
#no need to save it by cmd, it automatically saves it
python manage.py startapp users

