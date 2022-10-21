<img src="./readme-files/imgs/mockup.jpg">

# Candy Care Dublin

The live link can be found <a href="https://candycaredublin.herokuapp.com/" target="_blank" rel="noopener">here</a>.

This project was created as part of the Full Stack Software Development course offered by Code Institute.

# Table of Contents

- [Candy Care Dublin](#candy-care-dublin)
- [Table of Contents](#table-of-contents)
- [Briefing](#briefing)
- [The challenge](#the-challenge)
  - [Business Rules](#business-rules)
  - [Screens](#screens)
- [User Experience | UX](#user-experience--ux)
  - [User Stories](#user-stories)
    - [User](#user)
    - [Admin](#admin)
    - [Developer](#developer)
  - [Design Choices](#design-choices)
    - [Typography](#typography)
    - [Color palette](#color-palette)
- [User Interface | UI](#user-interface--ui)
  - [Features](#features)
    - [Existing Features](#existing-features)
      - [Main Navigation Bar](#main-navigation-bar)
        - [Secondary Navigation Bar](#secondary-navigation-bar)
      - [Hero Image](#hero-image)
      - [About](#about)
      - [Product Showcase](#product-showcase)
      - [Occasions](#occasions)
      - [Newsletter Form](#newsletter-form)
        - [Thank you Page](#thank-you-page)
      - [Social Networks](#social-networks)
      - [Footer](#footer)
- [Project Architecture](#project-architecture)
  - [Project settings structure](#project-settings-structure)
    - [Development environment](#development-environment)
    - [Testing environment](#testing-environment)
    - [Production environment](#production-environment)
  - [Data Storage](#data-storage)
    - [Database schema](#database-schema)
    - [User Table](#user-table)
    - [Profile Table](#profile-table)
    - [Product Table](#product-table)
    - [Category Table](#category-table)
    - [Occasion Table](#occasion-table)
    - [Order Table](#order-table)
    - [Order Line Table](#order-line-table)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
    - [Front-end](#front-end)
    - [Back-end](#back-end)
  - [Frameworks](#frameworks)
  - [Libraries](#libraries)
  - [Tools](#tools)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Forking the GitHub Repository and Running this Project Locally](#forking-the-github-repository-and-running-this-project-locally)
    - [Installing virtualenv](#installing-virtualenv)
    - [Creating a new virtualenv](#creating-a-new-virtualenv)
    - [Activating a virtualenv](#activating-a-virtualenv)
  - [Database setup](#database-setup)
  - [Setting up heroku](#setting-up-heroku)
- [Credits](#credits)
  - [Media](#media)
- [Acknowledgements](#acknowledgements)
- [Disclaimer](#disclaimer)
- [Author](#author)

# Briefing

**Candy Care Dublin** is a small company that started in a homely environment, with the idea of ​​making homemade cakes for the people who lived nearby. However, people liked it and recommended it to other people. The business has expanded and today **Candy Care Dublin** has clients that go beyond the surroundings, as well as in other cities. The main means of publicizing the business is through a page on social networks (Facebook and Instagram) but, with the exponential growth of the business, there was a need to create a website, where people could access, see the products available, add to cart and finally checkout the purcharse. In this way, it would no longer be necessary to make sales via Instagram or Facebook, which would facilitate the administration of the business.

# The challenge

With this idea in mind, the person in charge of **Candy Care Dublin** hired me to develop a fullstack web application for the company.

An e-commerce web application is expected to be delivered that meets the following needs:

> 1. A website whose purpose of the company is immediately understood by the user.
> 2. Have a clear information on what the site is about and what it provides
> 3. Have an easy navigation that is consistent throughout the website
> 4. That the user can easily view the list of available products.
> 5. That the user can easily add an specific item to the bag and identity the total cost of the purchase and all items they will receive.
> 6. That the user can easily enter their payment information and be sure their personal and payment information are safe and secure.

_For admin_

> 7. A functionality where the app admin can easily add one or more products, edit and/or delete an specific product.

## Business Rules

The application's administrative functions are intended to manage what each user can do within the system. Permissions such as adding, editing or removing a property, for example, should under no circumstances be given to the user of the application. Such functionalities must be assigned exclusively to the administrator.

In the system, there will be the following user functionalities:

- Admin: has permission in all areas of the system.
- Users: can edit your own profile like change profile picture or change password. The user can list all the available products and sort them by **Price** and **Name**, add one or more products to their bag, identity the total cost of their purchase and all items they will receive, edit their bag by removing an specific product from the bag or adding another one, before checkout. The user should be able to receive an e-mail containing all the details about their purchase such as the list of products, the total cost, the delivery address, and so on.

## Screens

- Admin:
  - Add/Edit/Remove products.
  - View all screens users can view as well.
- Users:
  - Can log in and out of the application.
  - Can manage their own profile.
  - Can sign up to the newsletter form.
  - Can add one or more products to their bag.

[Back to top ⇧](#table-of-contents)

# User Experience | UX

## User Stories

### User

- As a **Shooper** I want to be able to **quickly identify deals, clearance items and special offers** so that **I can take advantage of special savings on products I would like to purchase**.
- As a **Shooper** I want to be able to **easily view the total of my purchases at any time** so that **be aware of how much I've already spent and avoid spending too much**.
- As a **Shooper** I want to be able to **easily register for an account** so that **I can have a personal account and be able to view my profile**.
- As a **Shooper** I want to be able to **easily login or logout from my account** so that **I can access my personal account information**.
- As a **Shooper** I want to be able to **easily recover my password in case I forget it** so that **I can recover access to my account**.
- As a **Shooper** I want to be able to **receive a confirmation email after registering** so that **I can verify that my account registration was successful**.
- As a **Shooper** I want to be able to **have a personalized user profile** so that **I can view my personal order history and order confirmations, and save my payment information**.
- As a **Shooper**, I want to be able to **sort the list of available products** so that **I can easily identify the best priced and categorically sorted products**.
- As a **Shooper**, I want to be able to **sort a specific category of product** so that **I can find the best-priced product in a specific category, or sort the products in that category by name**.
- As a **Shooper**, I want to be able to **sort multiple categories of products simultaneously** so that **I can find the best-priced or best-rated product across broad categories, such as "vegan" or "best sellers.**.
- As a **Shooper**, I want to be able to **search for products by occasion, such as "birthdays" or "father's day"**.
- As a **Shooper**, I want to be able to **easily see what I have searched for and the number of results** so that **I can quickly decide whether the product I want is available**.

### Admin

- As a **Site Admin** I want to be able to **easily add a product** so that **I can add new items to my store**.
- As a **Site Admin** I want to be able to **see all existing products** in a simple and easy manner.
- As a **Site Admin** I want to be able to **edit/update a product** so that **I can change product prices, descriptions, images and other product criteria**.
- As a **Site Admin** I want to be able to **delete a product** so that **I can remove items that are no longer for sale**.

### Developer

- As a **Developer** I want to ensure that **all application features work** as they were implemented to work.
- As a **Developer** I want to ensure **an authenticated user can access** all required information correctly.
- As a **Developer** I want to **work together with the administrator** of the site for **improvements** for the user of the same.

## Design Choices

### Typography

As a primary font, I have chosen to use [Roboto](https://fonts.google.com/specimen/Roboto) since Roboto has been designed for screens and includes 12 different font weights, from thin to black. Roboto also allows letters to take up as much space as it needs and ultimately, making for an improved experience for the user.

As a secondary font I have chosen to use [Montserrat](https://fonts.google.com/specimen/Montserrat) once Montserrat really shines for short pieces of all caps and the geometric simplicity of the letters. It is classified as a _sans serif_ with 18 styles and 9 weights. This typeface is similar to Proxima Nova, Gotham, Futura, Arial and Helvetica.

<img src="./readme-files/imgs/design_choices.jpg"/>

### Color palette

The colors used throughout the project were extracted from the logo.

<img src="./readme-files/imgs/color_reference.jpg"/>

[Back to top ⇧](#table-of-contents)

# User Interface | UI

<div style="text-align: center;">
  <img src="./readme-files/imgs/home_desktop.jpg" alt="Home Desktop">
</div>

## Features

### Existing Features

#### Main Navigation Bar

<img src="./readme-files/imgs/main_nav.jpg" alt="Main Navigation">

##### Secondary Navigation Bar

<img src="./readme-files/imgs/secondary_nav.jpg" alt="Secondary Navigation">

#### Hero Image

<img src="./readme-files/imgs/hero_image.jpg" alt="Hero Image">

#### About

<img src="./readme-files/imgs/about.jpg" alt="About section">

#### Product Showcase

<img src="./readme-files/imgs/products.jpg" alt="Product Showcase">

#### Occasions

<img src="./readme-files/imgs/occasions.jpg" alt="Occasions">

#### Newsletter Form

<img src="./readme-files/imgs/newsletter_form.jpg" alt="Newsletter Form">

##### Thank you Page

<img src="./readme-files/imgs/thank_you.jpg" alt="Thank you Page">

#### Social Networks

<img src="./readme-files/imgs/social.jpg" alt="Social Networks">

#### Footer

<img src="./readme-files/imgs/footer.jpg" alt="Footer">

[Back to top ⇧](#table-of-contents)

# Project Architecture

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

## Data Storage

### Database schema

<img src="./readme-files/imgs/db_schema.png" alt="Database Schema">

### User Table

| Title          | Key In Database | Form Validation           | Data Type   |
| -------------- | --------------- | ------------------------- | ----------- |
| id             | id              | auto-increment            | Primary Key |
| Username       | username        | max_length 20             | CharField   |
| First Name     | first_name      | max_lenght 20             | CharField   |
| Last Name      | last_name       | max_lenght 20             | CharField   |
| E-mail Address | email           | Must contain @ & .com etc | EmailField  |
| Password       | password        | max length 50             | CharField   |

### Profile Table

Once a user registers in the system, a profile is automatically created for that user.

| Title                    | Key In Database          | Form Validation                              | Data Type    |
| ------------------------ | ------------------------ | -------------------------------------------- | ------------ |
| Id                       | id                       | auto-increment                               | Primary Key  |
| user                     | user                     | max length 50                                | Foreign Key  |
| Default Phone Number     | default_phone_number     | max_length=20, null=True, blank=True         | CharField    |
| Default Street Address 1 | default_street_address_1 | max_length=80, null=True, blank=True         | CharField    |
| Default Street Address 2 | default_street_address_2 | max_length=80, null=True, blank=True         | CharField    |
| Default Town or City     | default_town_or_city     | max_length=40, null=True, blank=True         | CharField    |
| Default County           | default_county           | max_length=80, null=True, blank=True         | CharField    |
| Default PostCode         | default_postcode         | max_length=20, null=True, blank=True         | CharField    |
| Default Country          | default_country          | blank_label='Country', null=True, blank=True | CountryField |

### Product Table

|    Title    | Key In Database |                    Form Validation                     |  Data Type   |
| :---------: | :-------------: | :----------------------------------------------------: | :----------: |
|     Id      |       id        |                     Auto-increment                     | Primary Key  |
|  Category   |    category     | 'Category', null=True, unique=True, on_delete=SET_NULL | Foreign Key  |
|  Occasion   |    occasion     | 'Occasion', null=True, unique=True, on_delete=SET_NULL | Foreign Key  |
|     SKU     |       sku       |             default=uuid4, editable=False              |  UUIDField   |
|    Name     |      name       |                     max_length=254                     |  CharField   |
|    Slug     |      slug       |        max_length=100, null=False, unique=True         |  SlugField   |
| Description |   description   |                     No validation                      |  TextField   |
|    Price    |      price      |         max_digits=6, null=False, unique=True          | DecimalField |
|    Image    |      image      |                 null=True, blank=True                  |  ImageField  |

### Category Table

| Title         | Key in Database | Form Validation                   | Data Type   |
| ------------- | --------------- | --------------------------------- | ----------- |
| Id            | id              | Auto-increment                    | Primary Key |
| Name          | name            | max length=254                    | CharField   |
| Friendly Name | friendly_name   | max_length=254, null=True, blank= | CharField   |

### Occasion Table

| Title         | Key in Database | Form Validation                       | Data Type   |
| ------------- | --------------- | ------------------------------------- | ----------- |
| Id            | id              | Auto-increment                        | Primary Key |
| Name          | name            | max length=254                        | CharField   |
| Friendly Name | friendly_name   | max_length=254, null=True, blank=True | CharField   |

### Order Table

| Title             | Key in Database   | Form Validation                                                               | Data Type    |
| ----------------- | ----------------- | ----------------------------------------------------------------------------- | ------------ |
| Id                | id                | Auto-increment                                                                | Primary Key  |
| Order Number      | order_number      | max length=32, null=False, editable=False                                     | CharField    |
| User Profile      | user_profile      | UserProfile, null=True, blank=True, on_delete=SET_NULL, related_name="orders" | Foreign Key  |
| Fullname          | full_name         | max_length=50, null=False, blank=False                                        | CharField    |
| E-mail            | email             | max_length=254, null=False, blank=False, Must contain @ & .com etc            | Email        |
| Phone Number      | phone_number      | max_length=20, null=True, blank=True                                          | CharField    |
| Country           | country           | blank_label='Country', null=False, blank=False                                | CountryField |
| Post Code         | postcode          | max_length=20, null=False, blank=False                                        | CharField    |
| Town or City      | town_or_city      | max_length=40, null=True, blank=True                                          | CharField    |
| Street Address 1  | street_address_1  | max_length=80, null=True, blank=True                                          | CharField    |
| Street Address 2  | street_address_2  | max_length=80, null=True, blank=True                                          | CharField    |
| County            | county            | max_length=80, null=True, blank=True                                          | CharField    |
| Date              | date              | auto_now_add=True                                                             | CharField    |
| Delivery Cost     | delivery_cost     | max_digits=6, decimal_places=2, null=False, default=0                         | DecimalField |
| Order Total       | order_total       | max_digits=10, decimal_places=2, null=False, default=0                        | DecimalField |
| Grand Total       | grand_total       | max_digits=10, decimal_places=2, null=False, default=0                        | DecimalField |
| Original Cart     | original_cart     | null=False, blank=False, default=''                                           | TextField    |
| Stripe Payment ID | stripe_payment_id | max_length=254, null=False, blank=False, default=''                           | CharField    |

### Order Line Table

| Title           | Key in Database | Form Validation                                                                    | Data Type    |
| --------------- | --------------- | ---------------------------------------------------------------------------------- | ------------ |
| Id              | id              | Auto-increment                                                                     | Primary Key  |
| Order           | order           | Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' | Foreign Key  |
| Product         | product         | Product, null=False, blank=False, on_delete=models.CASCADE                         | Foreign Key  |
| Quantity        | quantity        | null=False, blank=False, default=0                                                 | IntegerField |
| Line Itam Total | lineitem_total  | max_digits=6, decimal_places=2, null=False, editable=False                         | DecimalField |


# Technologies Used

## Languages

### Front-end

1. **HTML5, or Hyper Text Markup Language:** Used to construct the page within this app -  
   https://developer.mozilla.org/en-US/docs/Web/HTML

2. **CSS3, or Cascading Style Sheets:** Used to style the various elements on the app's pages via coloring, fonts, spacing, etc. -
   https://www.w3.org/Style/CSS/Overview.en.html

### Back-end

3. **Javascript:** Used to create iterations across the page. - https://www.javascript.com/

4. **Python 3:** Used to develop all application logic. (https://www.python.org/)

## Frameworks

- [Bootstrap 4](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- [Django](https://www.djangoproject.com/)
- [Jquery](https://jquery.com/)

## Libraries

- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)

## Tools

- [Heroku](https://www.heroku.com)
- [Git](https://git-scm.com/)
- [Postgres](https://www.postgresql.org/)
- [Db Diagram](https://dbdiagram.io/home)
- [Diagrams](https://www.diagrams.net/)
- [Cloudinary](https://cloudinary.com/)
- [Figma](https://figma.com)
- [Stripe](https://stripe.com)

[Back to top ⇧](#table-of-contents)

# Testing

Some manual tests were performed to ensure the correct functioning of the application.

[Back to top ⇧](#table-of-contents)

# Deployment

## Forking the GitHub Repository and Running this Project Locally

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original
repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)

2. In the Repository header (not at the top of the page), find a "Code" drop-down button. By clicking this button, you will find some options to clone the project repository. If you have your SSH key configured, choose to select the 'SSH' option and then click on the button right after the url. This button will copy the url and you will paste it in your terminal. If you have not configured your SSH key, you can choose to use the HTTPS protocol. In the same way as was done in the SSH option, when selecting 'HTTPS' you must click on the button right after the url to copy and then paste it into your terminal.

   https://github.com/emidiovaleretto/candy-care-dublin-ecommerce.git

3. You should now have a copy of the original repository in your GitHub account.

4. Ideally you will want to work within a virtual environment to allow all packages to be kept within the project, this can be installed using the following command (please note some IDE's require pip3 instead of pip, please check with the documentation for your chosen IDE). To create a virtual environment, run the command

### Installing virtualenv

The installation of a virtualenv is done using pip, Python's package manager. It is with it that we install, remove and update packages in our projects. One note is that PIP is already installed when we are using IDE's like VSCode or PyCharm for our Python projects. So, just run the command below to install the virtualenv package on our computer:

    pip install virtualenv

Once this is done, the package will be installed and ready to be used. Now you can create and manage your virtual environments.

### Creating a new virtualenv

The process of creating a virtualenv is quite simple and can be done using a single command, as seen below:

    virtualenv your_virtualenv_name

_Hint: I usually choose to name my virtual environments after the project name, rather than just writing 'venv', for example, the project is called `MyBlogProject`, so the name of the virtual environment would be something like `myblogenv`. If you need to return to a certain project after a while, you'll easily find the respective environment for that project. But that is totally up to you._

### Activating a virtualenv

After creating a virtualenv, it's needed to activate it so that you can install the necessary packages for the project. To do this, run the following command:

`source your_virtualenv_name/bin/activate (Linux ou macOS)`

`your_virtualenv_name/Scripts/Activate (Windows)`

3. Once that's done, you need to install the project's dependencies. To do this, just run the following command:

   pip3 install -r requirements.txt

4. Next you need to create a new file within the root directory called `env.py`. This file will contain all your secret keys, public keys, production database settings etc. Everything you think should not be exposed, you should put within this file.

So add the following lines to configure the environmental variables.

```
import os

# SECRET KEYS
os.environ.setdefault("SECRET_KEY_DEVELOPMENT", "YOUR SECRET KEY")
os.environ.setdefault("SECRET_KEY_PRODUCTION", "YOUR SECRET KEY")
os.environ.setdefault("SECRET_KEY_TESTING", "YOUR SECRET KEY")

# DATABASE URL
os.environ.setdefault("DATABASE_URL", "YOUR DATABASE URL")

```

## Database setup

1. To set up your database you will first need to run the following command:

   python3 manage.py migrate

2. Then you need to create a **superuser**. This will allow you to access the application's admin panel. To do so, run the following command in your terminal and fill in the required information as prompted.

   python3 manage.py createsuperuser

3. From there you need to delete any objects from the database that are not in the fixture. To do this, run the following commands:

   python3 manage.py shell

A terminal screen should appear. In the terminal, paste the following command:

    from django.contrib.contenttypes.models import ContentType

    ContentType.objects.all().delete()

4. Now you should be able to run the server using the following command:

   python3 manage.py runserver

If everything has been correctly configure you should not get a message giving you a link to your locally hosted site usually at http://127.0.0.1:8000

1. Finally, stop the server by pressing CTRL + C (or cmd + C on Mac) and run the following command to populate the database.

   python3 manage.py loaddata category.json
   python3 manage.py loaddata products.json

After running this command, all information contained in the `category.json` and `products.json` files will be saved in the database. Once that's done, run the `python3 manage.py runserver` command again and you should be able to see the application working.

## Setting up heroku

To set up heroku you must:

1. If your requirements.txt file has not changed you can skip this step. Otherwise, in your terminal type 'pip freeze > requirements.txt' then save and push the changes.
2. Go to Heroku.com and sign in to your account or create a free one.
3. From the heroku dashboard click the 'Create new app' button.
4. Name the app something unique and choose what region you are in then click 'Create app'.
5. In the resources section, in the _add-ons_ field, type `Heroku Postgreslq` and select the free cost option.
6. Now, go to the settings tab and find the Config Vars section. Click 'Reveal Config Vars'.

In the settings tab, select Reveal Config Vars and copy the pre populated `DATABASE_URL` into your `settings.py` file in your project in the Config Vars in Heroku you will need to populate with the following keys:

|          Key          |        Value        |
| :-------------------: | :-----------------: |
| SECRET_KEY_PRODUCTION |  [Your Secret Key]  |
|   DEBUG_PRODUCTION    |        False        |
|     DATABASE_URL      | [Your DATABASE URL] |
|      HEROKU_HOST      | [Your Heroku Host]  |

7.  Then head over to the deploy section by clicking deploy from the nav bar at the top of the page.
8.  From the 'Deployment method' section select GitHub and click 'Connect to GitHub'.
9.  Enter the repository name as it is in GitHub and click 'search'.
10. Click the 'connect' button next to the repository to link it to heroku.
11. To deploy, scroll down and click the 'Deploy Branch' button.
12. Heroku will notify you that the app was successfully deployed with a button to view the app.
13. If you want to rebuild your app automatically you can also select the 'Enable Automatic Deploys' button which will then rebuild the app every time you push any changes.

# Credits

## Media

   - [Pexels](https://www.pexels.com/) - All images were downloaded from the website.
   - [Freepik](https://www.freepik.com/) - For icons.
   - [Table of contents](https://ecotrust-canada.github.io/markdown-toc/)
   - [Code Institute](https://codeinstitute.net/)


# Acknowledgements

I would like to take the opportunity to thank:

- To God first, to my family, friends and colleagues for their advice, support and help with testing.
- To my mentors Felipe Alarcon & Richard Wells for their feedback, advices, support and, above all, for their patience.
- All Code Institute Tutors and Community on Slack for the peer reviews and advice.

# Disclaimer

> \***_Disclaimer_**: The following Context is completely fictional, the company, the context, the CEO, the business questions exist only in my imagination.

> \*\*For educational purposes only.

# Author

Made with ❤️ by <b>Emidio Valereto</b> <img src="https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/wave.gif" width="16px"> Get in touch!

[![Linkedin Badge](https://img.shields.io/badge/-Emidio-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/emidiovalereto/)](https://www.linkedin.com/in/emidiovalereto/) [![Gmail Badge](https://img.shields.io/badge/-emidio.valereto@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:emidio.valereto@gmail.com)](mailto:emidio.valereto@gmail.com)

[Back to top ⇧](#table-of-contents)
