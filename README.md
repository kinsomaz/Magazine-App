# team9-project1


## Hosting

Visit https://magazine-ecx.herokuapp.com/ 

## NOTE

It uses some environment parameters. Checked the .env.example file for details. Contact the backend devs for more info.

## Functionality 

The magazine app brings you the latest entertainment news and music news,
you can search for any intrest and it will bring you the latest.

It also comes with a blog app where users can register, login, and create blog post for users to see and
can see posts created by other users.


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

blog create page, url = '/create'

blog detail page, url = '/blog/detail/slug'

blog edit page, url = '/blog/edit/slug'

blog delete page, url = '/blog/delete/slug'


### users

Has the whole user registration and login forms and authentication with the user profile and edit user profile


registration page, url = 'users/register'....redirect to magazine home page if already logged in

login page, url = 'users/login'....redirect to magazine home page if already logged in

profile page, url = 'users/profile'....need to be logged in

edit profile page, url = 'users/edit_profile'....need to be logged in


### search

This is the app that adds search feature to the blog app.

search page, url = '/search'

packages instaleed: django, Pillow, django-crispy-forms

