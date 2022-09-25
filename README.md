<img src="./readme-files/imgs/candy_care_logo.jpg">

# Candy Care Dublin

The live link can be found <a href="https://candycaredublin.herokuapp.com/" target="_blank" rel="noopener">here</a>.

This project was created as part of the Full Stack Software Development course offered by Code Institute.

# Table of Contents

- [Candy Care Dublin](#candy-care-dublin)
- [Table of Contents](#table-of-contents)
- [Project Architecture](#project-architecture)
  - [Django Framework](#django-framework)
    - [What is Django?](#what-is-django)
    - [Why did I choose Django to work with?](#why-did-i-choose-django-to-work-with)
  - [Django Architecture](#django-architecture)
    - [Django Project MVT Structure](#django-project-mvt-structure)
    - [MVT (Model-View-Template)](#mvt-model-view-template)
  - [Design Architecture](#design-architecture)
    - [MVT Django Project Structure](#mvt-django-project-structure)
  - [Project settings structure](#project-settings-structure)
    - [Development environment](#development-environment)
    - [Testing environment](#testing-environment)
    - [Production environment](#production-environment)
- [Acknowledgements](#acknowledgements)
- [Disclaimer](#disclaimer)
- [Author](#author)

# Project Architecture

## Django Framework

![django_logo](https://static.djangoproject.com/img/logos/django-logo-negative.png)

**The web framework for perfectionists with deadlines.**

### What is Django?

Django is a free and open-source web application framework written in Python. It is used for rapid web development and clean, pragmatic design. It is built by experienced developers to make repetitive tasks easier, so we can focus on writing apps instead of reinventing the wheel. Django was created in 2003 when web developers at the Lawrence Journal-World newspaper started using Python for their web development. After creating a number of websites, they started to factor out and reuse lots of common code and design patterns. That common code led to a generic web development framework that was open-sourced as the “Django” project in 2005. Since the original developers were surrounded by newspaper writers, well-written documentation is a key part of Django. This means that there are excellent references to check out on the official Django documentation pages. The Django framework is extremely large, but the Django community is absolutely massive. The community has contributed a lot of third-party code for Django. No matter what we are trying to do, there’s a good chance that we will find the solution for it on djangopackages.org. The website includes everything, from authentication and authorization to full-on Django-powered content management systems, from e-commerce add-ons to integrations with Stripe.

### Why did I choose Django to work with?

While Django is most often used for web development, it can be used for many other purposes as well. It is a highly-regarded piece of software and is highly recommended for anyone who is serious about their web development. It can be used to build large e-commerce websites, blogging sites, or anything else that requires a scalable, high-performing website. In this article, we are going to cover all the basics you need to know to get started with Django. We will cover topics such as setting up your development environment and installing and using Django. We will also cover how to choose the right Django installation for your needs and how to get the most out of the framework by using best practices. Here are some reasons why I chose to work with Django:

 - Django is a great option for beginner and advanced developers alike. It’s very easy to learn and install, and it doesn’t require any external tools or libraries. It can be used to build any type of web or mobile app, from the simplest to the most complex. Django is often cited as a “best practices” application development framework, because it follows a consistent structure, provides everything developers might need and is very easy to use.
 
 - This flexibility is what makes Django such a popular choice for building websites. It’s easy to learn, easy to implement, and can be extended with a huge range of tools and libraries. It’s also very quick to create a website with and can be up and running in a matter of days.
 
 - Ridiculously fast.
     - Django was designed to help developers take applications from concept to completion as quickly as possible. 

 - Reassuringly secure.
     - Django takes security seriously and helps developers avoid many common security mistakes.

 - Exceedingly scalable.
     - Some of the busiest sites on the web leverage Django’s ability to quickly and flexibly scale.

## Django Architecture

Before we really get into the Django universe, let's talk about the software architecture model.

The most popular software architecture, by far, is the Model-View-Controller, or MVC.

Model–view–controller (MVC) is a software architectural pattern commonly used for developing user interfaces that divide the related program logic into three interconnected elements. This is done to separate internal representations of information from the ways information is presented to and accepted from the user.

MVC divides any large application into three parts:

  1. The Model
  2. The View
  3. The Controller

<img src="./readme-files/imgs/mvc.jpg"/>

Read more in [Wikipedia](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller).

### Django Project MVT Structure

Every web application is basically divided into three main sections: **input data**, **business logic**, and **user interface**.

The code has certain functions to perform, the input data is the dataset and how it is stored in the database. It is just a matter of delivering the input to the database in the desired format. The Business Logic is what controls the output of the server in HTML or another format. The HTML and CSS are the pages that it is written for. These days, the approach taken is different. The content is gathered from multiple sources and stored in separate files. This is known as page streaming, and it is a widely used approach for website content. The code for the webpage is stored in one file and the HTML, CSS and JS are stored in separate files. The content is streamed from the server and rendered in the browser.

### MVT (Model-View-Template)

Django is based on Model-View-Template architecture. MVT is a design pattern or design architecture that Django follows to develop web applications.

MVT determines the total structure and workflow of a Django application. In an MVT architecture

 - The **Model** manages the data and is represented by a database. A model is basically a database table.
 - The **View** receives HTTP requests and sends HTTP responses. A view interacts with a model and template to complete a response. It is in **View** where the application logic is present.
 - The **Template** is basically the front-end layer and the dynamic HTML component of a Django application. The **Template** layer handles the staticfiles such as CSS, JavaScript and Images.

Below I show how the application architecture was designed, based on Django's MVT pattern structure.

## Design Architecture

### MVT Django Project Structure

<img src="./readme-files/imgs/architecture_design.jpg"/>

[Back to top ⇧](#table-of-contents)

## Project settings structure

The configuration file is one of the most important elements in any Django project. Knowing this, I decided to divide the configuration files structure into four files, one of them being the base file, which will contain everything that is needed in any project environment, be it **production**, **development** or **testing**. The other three files are for development, testing and finally production environments.

For that, create a folder called `settings` inside the main project folder. Inside it, add the `development.py`, `testing.py`, `production.py` and `__init__.py` files. After that, take the base `settings.py` file (which is in the root of the main project folder) and move it into the settings folder.

We will do this so that within the `settings.py` file there are only elements that will be used in any of the environments, be it production, testing or development. However, whatever we need to create differently for each environment, we will put it in the files we just created.

For this project, both the development and test environments use the `sqlite` database locally, while the production environment uses the `Postgresql` database. That way, development and testing data doesn't mix with the data that will be in production. To do this kind of separation, we must place the database settings in their respective files.

See below how the project structure should look 👇

<img src="./readme-files/imgs/project_structure.jpg"/>

Now, we will need to open each file and add some settings.

### Development environment

```
from .settings import *

DEBUG = True

SECRET_KEY = os.environ.get("SECRET_KEY_DEVELOPMENT")
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

```

### Testing environment

```
from .settings import *

DEBUG = True
SECRET_KEY = os.environ.get("SECRET_KEY_TESTING")
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### Production environment

```
import os
import dj_database_url
from .settings import *

if os.path.exists("env.py"):
    import env

DEBUG = False
SECRET_KEY = os.environ.get("SECRET_KEY_PRODUCTION")
ALLOWED_HOSTS = [os.environ.get("HEROKU_HOST")]

DATABASES = {'default': dj_database_url.parse(os.environ.get("HEROKU_DB"))}

```

Remembering that it is good programming practices not to leave SECRET_KEYS visible as this will result in the vulnerability of the application. Therefore, generate your own secret keys and configure them through environment variables.

You can use Python `os` library to set your environment variables and then import them into the files, as I exemplify below:

```
import os

# SECRET KEYS
os.environ.setdefault("SECRET_KEY_DEVELOPMENT", "YOUR SECRET KEY")
os.environ.setdefault("SECRET_KEY_PRODUCTION", "YOUR SECRET KEY")
os.environ.setdefault("SECRET_KEY_TESTING", "YOUR SECRET KEY")

```
Once that's done, don't forget to remove the database settings and secret key from the `settings.py` file.

It is worth mentioning that with this change in the project structure, you will need to change some more settings, so that the application works correctly. By default, in the `settings.py` file, the `BASE_DIR` variable looks like this: `BASE_DIR = Path(__file__).resolve().parent.parent`. You will need to add a new `.parent` as there has been a subdivision of the main project folder. So the `BASE_DIR` variable should look like this: `BASE_DIR = Path(__file__).resolve().parent.parent.parent`.

Also, in the `wsgi.py` file you will need to notice that by default, the environment variable setting will look like this:

```
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "candycaredublin.settings")

application = get_wsgi_application()
```

Since three independent environments were created, we need to tell Django which environment we are going to work with. In this way, it is necessary to add, right after `settings`, the environment name.

If working in the development environment, add `.development`. If working in the testing environment, add `.testing` and so on.

The same thing should apply to the `manage.py` file which by default appears as

```
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'candycaredublin.settings')

    # The rest of the code was hidden to optimize the page. Do not remove anything after this line.
    ...
```

If working in the development environment, add `.development` after `settings`. If working in the testing environment, add `.testing` and so on.

Be sure to change it each time you are working in a different environment.

With the project configured correctly, when running the application, you will see something similar to this.

<img src="./readme-files/imgs/django_launch.png"/>

[Back to top ⇧](#table-of-contents)

# Acknowledgements

I would like to take the opportunity to thank:

 - To God first, to my family, friends and colleagues for their advice, support and help with testing.
 - To my mentors Felipe Alarcon & Richard Wells for their feedback, advices, support and, above all, for their patience.
 - All Code Institute Tutors and Community on Slack for the peer reviews and advice.


# Disclaimer

> ****Disclaimer***: The following Context is completely fictional, the company, the context, the CEO, the business questions exist only in my imagination.

> **For educational purposes only.

# Author

Made with ❤️ by <b>Emidio Valereto</b> <img src="https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/wave.gif" width="16px"> Get in touch!

[![Linkedin Badge](https://img.shields.io/badge/-Emidio-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/emidiovalereto/)](https://www.linkedin.com/in/emidiovalereto/) [![Gmail Badge](https://img.shields.io/badge/-emidio.valereto@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:emidio.valereto@gmail.com)](mailto:emidio.valereto@gmail.com)