
rmvirtualenv djangoenv			;***MMM only if already exists
mkvirtualenv djangoenv
pip install django==2.1.5		;***MMM DO NOT USE 2.1.1 THROWS EXCEPTIONS

django-admin help
django-admin startproject mysite
cd mysite
python manage.py runserver		; start django
open a browser url = localhost:8000	; test
python manage.py migrate		; create the database (see section in mysite\settings.py)
dir					; note the db.sqlite3 db is created
winpty python manage.py createsuperuser		; create a superuser to admin the db
	user = mike
	password = Password1!
python manage.py startapp polling	; create a polling app
dir					; note the polling created app folder
edit mysite\settings
	section: INSTALL_APPS
			add your polling app to the bottom of the list
			'polling',	; ***MMM be sure to include the single quotes
git init
			
create the overall site web templates
mkdir mysite\templates
edit mysite\templates\base.html		; ref the video for the code
edit mysite\settings.py			; add 'DIRS': [os.path.join(BASE_DIR, 'mysite/templates')],        

edit mysite\polling\models.py		; ref the video
python manage.py makemigrations		; migrate the changes to the db
python manage.py migrate
edit mysite\polling\admin.py		; register the poll model
start python manage.py runserver	;  # Then visit http://localhost:8000/admin/
mkdir mysite\polling\templates\polling	; we create polling view templates under our polling app
edit mysite\polling\templates\polling\list.html		; create template, ref the video
edit mysite\polling\templates\polling\detail.html	; create template, ref the video
edit mysite\polling\views.py		; add the view for the template, ref the video
edit mysite\urls.py			; define the route to your top level site in urlpatterns, see the video
edit mysite\polling\urls.py		; routes for the polling app
start python manage.py runserver	;  # Then visit http://localhost:8000/polling/

python manage.py startapp blogging	; create the blogging app
edit mysite\settings
	section: INSTALL_APPS
			add your polling app to the bottom of the list
			'blogging',	; ***MMM be sure to include the single quotes
python manage.py makemigrations blogging	; migrate the table changes to the db for blogging
python manage.py migrate			; update the db

- using the django shell to test interactively
python manage.py shell
from blogging.models import Post
from django.contrib.auth.models import User
all_users = User.objects.all()
p2 = Post(title="Another post",
            text="The second one created",
            author=all_users[0]).save()
p3 = Post(title="The third one",
            text="With the word 'heffalump'",
            author=all_users[0]).save()
p4 = Post(title="Posters are a great decoration",
            text="When you are a poor college student",
            author=all_users[0]).save()
Post.objects.count()

- the blogging app via admin
edit mysite\blogging\admin.py		; ref the video
python manage.py runserver		; start django

------------------
lesson 7 activity

edit blogging/models.py			; per lesson, ie add Category class
python manage.py makemigrations		; comit to the model using migrations
python manage.py migrate		; comit to the db
edit blogging/admin.py			; add Category
python manage.py runserver
http://localhost:8000/admin		; test categories appears in admin
edit tests.py				; test give a name to the displayed category
python manage.py test blogging		; one test will fail
edit blogging/models.py			; per lesson
retest					; verify categories, and name appears
edit blogging/views.py			; per lesson
edit blogging/url.conf			; per lesson
add this to misite/misite/urls.py	; path('', include('blogging.urls')),
edit blogging/tests.py			; per lesson add test_list_only_published
edit blogging/templates/blogging/list.html	; per lesson, list html
edit blogging/view.html			; per lesson, add list view
edit blogging/templates/blogging/detail.html	; per lesson, detail html
edit blogging/detail.html			; per lesson, add detail view
edit blogging/templates/blogging/list.html	; per lesson, 4 tests run successfully
edit mysite/templates/base.html			; per lesson, static files, css
edit mysite/templates/login.html		; per lesson, for login
edit mysite/mysite/urls.py			; per lesson, for login, logout
http://localhost:8000/admin		; test login page

----------------------------------

lesson 8 assignment notes, continue blogging app from lesson 7
django addons (all-auth, ModelForm)
pip install django-allauth
update settings.py			; per lesson all-auth instrs
update urls.py				; per lesson all-auth instrs
python manage.py migrate		; comit

;setup facebook app
login facebook.com
	change url to developers.facebook.com
	follow video to create an app https://www.youtube.com/watch?v=-XME8Q25omQ
	set site url = localhost:8000		
		scroll to bottom click add platform
		select website
		set site url = localhost:8000
	USE DEV MODE, no need to swith to live mode, this way no domain is needed

	Note:
		Not needed since we are in dev mode, but just for ref
		https://stackoverflow.com/questions/13376710/facebook-app-domain-name-when-using-localhost

http://localhost:8000/admin		; follow configuration per lesson
edit home->sites from example.com to localhost:8000 FB Login
add home->social application->add
	click add social application
	select provider == Facebook
	client id = 662030651180909	; app id
	secret key = 68288648fb895a09a06cd720334f1032	; app secret
	specify localhost:8000 for the chosen site
	click save

test
http://localhost:8000/admin/socialaccount/socialapp/
http://localhost:8000/accounts/admin
http://localhost:8000/accounts/facebook/login
	user: mikea

;django addon ModelForm
;create a django form from an existing model
;follow instructions per
;represent db model as a form (ref doc http://blog.appliedinformaticsinc.com/using-django-modelform-a-quick-guide/)
python manage.py makemigrations		; migrate the changes to the db
python manage.py migrate
edit views.py, urls.py, forms.py	; edit per ModelForm requirements
start python manage.py runserver	;  # Then visit http://localhost:8000/admin/
browser http://localhost:8000/create	; submit ModelForm, test create short post
browser http://localhost:8000/admin/posts	; test the create short post form submission











