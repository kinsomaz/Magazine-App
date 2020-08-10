# team9-project1


## Hosting

Visit https://magazine-ecx.herokuapp.com/ 

## Database

currentlty have two models

1. Default django user model

2. profile model(one to one relationship with user model..i.e one user is entitled to one profile), currently in the user app models

admin details


username = 'admin'

password = 'admin1234'

we have four apps

1. magazine
2. blog
3. users
4. search



### Magazine


This app has the basic templates and views

home page,  url = ''

about page,  url = '/about'

contact page,  url = '/contact'


### Blog


This is the app that users can use to write, edit, delete and view their posts.

NOTE: Slug is what the writer entered in the slug field during the creation of each post. 

blog home page, url = '/blog'

blog create page, url = '/blog-new'

blog detail page, url = '/blog/slug'

blog edit page, url = '/blog/slug/edit'

blog delete page, url = '/blog/slug/delete'


### users

has the whole user registration and login forms and authentication with the user profile and edit user profile


registration page, url = 'users/register'....redirect to magazine home page if already logged in

login page, url = 'users/login'....redirect to magazine home page if already logged in

profile page, url = 'users/profile'....need to be logged in

edit profile page, url = 'users/edit_profile'....need to be logged in


### search

This is the app that adds search feature to the blog app.

search page, url = '/search'

packages instaleed: django, Pillow, django-crispy-forms

NB: the templates and styling for the pages are still going to be edited...these are just dummy templates

Any questions can be asked on the group chat
