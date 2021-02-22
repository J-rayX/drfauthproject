# Django Rest Framework Authentication with Dj-Rest-Auth

This repository contains the code for my Medium article on [Authentication and authorization in Django RESTful APIs using Dj-Rest-Auth](https://jkaylight.medium.com/django-rest-framework-authentication-with-dj-rest-auth-4d5e606cde4d) with Gmail server for sending verification emails to users. A CRUD app example was used.

## To Run on Localhost:

- Have `Python` and `pip` installed on your local machine

## Running the Django project:

Create an isolated environment for the project with `virtualenv`. You can install `virtualenv` with the following command:

```
sudo pip install virtualenv
```

Create a new directory for the project:

```
mkdir myproject && cd myproject
```

Create a virtual environment for the project:

```bash
virtualenv env
```

Then, activate it:

```bash
source env/bin/activate
```

Clone the project from GitHub:

```bash
git clone https://github.com/J-rayX/drfauthproject
```

Install Django and Django REST Framework:

```bash
pip install django djangorestframework
```

Finally, `cd` into the _drfauthproject_ folder and run the project:

```bash
python manage.py runserver
```

Go to http://localhost:8000/ to see if the API is up and running.

Now, you can follow the article on Medium to learn how to implement authentication and authorization for your Django REST APIs. You will also learn how to use Gmail smtp server to send verification and password-reset emails to users.

**We move!** 💪
