<img src="./readme-files/imgs/mockup.jpg">

# Candy Care Dublin

The live link can be found <a href="https://candycaredublin.herokuapp.com/" target="_blank" rel="noopener">here</a>.

This project was created as part of the Full Stack Software Development course offered by Code Institute.

# Table of Contents

- [Candy Care Dublin](#candy-care-dublin)
- [Table of Contents](#table-of-contents)
- [Business Model](#business-model)
  - [Business to Consumer (B2C)](#business-to-consumer-b2c)
- [Client Briefing](#client-briefing)
- [The challenge](#the-challenge)
- [Business Rules](#business-rules)
  - [Screens](#screens)
- [Marketing Strategy](#marketing-strategy)
  - [Facebook Business Page](#facebook-business-page)
    - [Highlights](#highlights)
  - [Instagram Business Profile](#instagram-business-profile)
    - [Highlights](#highlights-1)
- [User Experience | UX](#user-experience--ux)
  - [System Usability Scale](#system-usability-scale)
  - [User Stories](#user-stories)
    - [User](#user)
    - [Admin](#admin)
    - [Developer](#developer)
  - [Design Choices](#design-choices)
    - [Typography](#typography)
    - [Color palette](#color-palette)
- [User Interface | UI](#user-interface--ui)
  - [Skeleton](#skeleton)
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
    - [Inner pages](#inner-pages)
    - [Admin Panel](#admin-panel)
    - [Features to be implemented](#features-to-be-implemented)
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
    - [Newsletter Table](#newsletter-table)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
    - [Front-end](#front-end)
    - [Back-end](#back-end)
  - [Frameworks](#frameworks)
  - [Libraries](#libraries)
  - [Tools](#tools)
- [Testing 🔎](#testing-)
  - [HTML Validator](#html-validator)
  - [CSS Validator](#css-validator)
  - [JavaScript Validator (JSHint)](#javascript-validator-jshint)
  - [Accessibility and Performance testing](#accessibility-and-performance-testing)
  - [Test Driven Development (TDD)](#test-driven-development-tdd)
  - [Manual tests](#manual-tests)
  - [Testing User Stories](#testing-user-stories)
  - [Bugs Report 🐞](#bugs-report-)
  - [Bugs resolution 👷⛏](#bugs-resolution-)
- [Deployment](#deployment)
  - [Forking the GitHub Repository and Running this Project Locally](#forking-the-github-repository-and-running-this-project-locally)
    - [Installing virtualenv](#installing-virtualenv)
    - [Creating a new virtualenv](#creating-a-new-virtualenv)
    - [Activating a virtualenv](#activating-a-virtualenv)
  - [Database setup](#database-setup)
  - [Stripe | Payment Processing Platform for the Internet](#stripe--payment-processing-platform-for-the-internet)
  - [Testing Payment Intents with Stripe](#testing-payment-intents-with-stripe)
  - [Setting up heroku](#setting-up-heroku)
- [Credits](#credits)
  - [Media](#media)
- [Acknowledgements](#acknowledgements)
- [Disclaimer](#disclaimer)
- [Author](#author)

# Business Model

## Business to Consumer (B2C)

B2C is the process of selling products or services from businesses to individual consumers. In this case, **Candy Care Dublin** is the business and the cakes/sweeties are our products.

# Client Briefing

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

# Business Rules

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

# Marketing Strategy

## Facebook Business Page

 - [Candy Care Dublin - Facebook Business Page](https://www.facebook.com/people/Candy-Care/100038339116419/)
  <img src="./readme-files/imgs/facebook_page.jpg" alt="Facebook Business Page of Candy Care Dublin Store">
  <img src="./readme-files/imgs/facebook_page_2.jpg" alt="Facebook Business Page of Candy Care Dublin Store">

### Highlights

 - Cover photo matches the **Candy Care Dublin** site.
 - Profile pictute matches the **Candy Care Dublin** logo.

## Instagram Business Profile

 - [Candy Care Dublin - Instagram Business Profile](https://www.instagram.com/candycaredublin/)
  <img src="./readme-files/imgs/instagram_page.jpg" alt="Instagram Business Page of Candy Care Dublin Store">
  <img src="./readme-files/imgs/instagram_page_2.jpg" alt="Instagram Business Page of Candy Care Dublin Store">

### Highlights

 - Profile pictute matches the **Candy Care Dublin** logo.


[Back to top ⇧](#table-of-contents)

# User Experience | UX

## System Usability Scale

In order to test the user's feeling when using the system, I applied the System Usability Scale test which includes 10 questions (in this case I added 3 more) which users of your website will answer. Participants will rank each question from 1 to 5 based on how much they agree with the statement they are reading. 5 means they agree completely, 1 means they disagree vehemently.

The questionnaire contains the following questions:

 1. I think I would like to use this system often.
 2. I found the system unnecessarily complex.
 3. I found the system easy to use.
 4. The features of this system were very well integrated.
 5. I found this system very inconsistent.
 6. I think most people would learn to use this system quickly.
 7. I found this website very cumbersome/awkward to use.
 8. I felt very confident using this system.
 9. I needed to learn a number of things before I could start using this system.
 10. It was easy to find the information I was looking for.
 11. I liked using the system interface.
 12. The system interface is enjoyable.
 13. The organization of system information is clear.

The form can be found in this [link](https://forms.gle/qSztkzuxcuVgKFwC7).

Five people, 3 women and 2 men, participated as volunteers in the survey and I share the result below.

<details>
    <summary>Google Forms</summary>
        <img src="./readme-files/imgs/usability_test.jpg" alt="Usability Test Results">
</details>


## User Stories

### User

- As a **Shopper** I want to be able to **quickly identify deals, clearance items and special offers** so that **I can take advantage of special savings on products I would like to purchase**.
- As a **Shopper** I want to be able to **easily view the total of my purchases at any time** so that **be aware of how much I've already spent and avoid spending too much**.
- As a **Shopper** I want to be able to **easily register for an account** so that **I can have a personal account and be able to view my profile**.
- As a **Shopper** I want to be able to **easily login or logout from my account** so that **I can access my personal account information**.
- As a **Shopper** I want to be able to **easily recover my password in case I forget it** so that **I can recover access to my account**.
- As a **Shopper** I want to be able to **receive a confirmation email after registering** so that **I can verify that my account registration was successful**.
- As a **Shopper** I want to be able to **have a personalized user profile** so that **I can view my personal order history and order confirmations, and save my payment information**.
- As a **Shopper**, I want to be able to **sort the list of available products** so that **I can easily identify the best priced and categorically sorted products**.
- As a **Shopper**, I want to be able to **sort a specific category of product** so that **I can find the best-priced product in a specific category, or sort the products in that category by name**.
- As a **Shopper**, I want to be able to **sort multiple categories of products simultaneously** so that **I can find the best-priced or best-rated product across broad categories, such as "vegan" or "best sellers.**.
- As a **Shopper**, I want to be able to **search for products by occasion, such as "birthdays" or "father's day"**.
- As a **Shopper**, I want to be able to **easily see what I have searched for and the number of results** so that **I can quickly decide whether the product I want is available**.

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

## Skeleton

The wireframes were created in [Figma](https://www.figma.com/) which can be explored in details by clicking on the image below 👇

<div style="text-align: center;">
  <a href="https://www.figma.com/file/SuUHR3EYW8leyM4RSbryf8/Candy-Care-Dublin---Wireframes-(Desktop)?node-id=0%3A1">
    <img src="./readme-files/imgs/mockup_figma.jpg" alt="Mockup Figma">
  </a>
</div>

## Features

### Existing Features

#### Main Navigation Bar

<img src="./readme-files/imgs/main_nav.jpg" alt="Main Navigation">

#### Secondary Navigation Bar

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

#### Thank you Page

<img src="./readme-files/imgs/thank_you.jpg" alt="Thank you Page">

#### Social Networks

<img src="./readme-files/imgs/social.jpg" alt="Social Networks">

#### Footer

<img src="./readme-files/imgs/footer.jpg" alt="Footer">

### Inner pages

<details>
    <summary>Shop page</summary>
        <img src="./readme-files/imgs/shop.jpg" alt="Shop page">
</details>

<details>
    <summary>Product details page</summary>
        <img src="./readme-files/imgs/product_detail.jpg" alt="Product details page">
</details>


<details>
    <summary>Shopping bag page</summary>
        <img src="./readme-files/imgs/shopping_bag.jpg" alt="Shopping bag page">
</details>


<details>
    <summary>Checkout page</summary>
        <img src="./readme-files/imgs/checkout.jpg" alt="Checkout page">
</details>

<details>
    <summary>Profile page</summary>
        <img src="./readme-files/imgs/profile.jpg" alt="Profile page">
</details>


### Admin Panel


<details>
    <summary>Management page</summary>
        <img src="./readme-files/imgs/management.jpg" alt="Management page">
</details>


<details>
    <summary>Add product page</summary>
        <img src="./readme-files/imgs/add_product.jpg" alt="Add product page">
</details>


<details>
    <summary>Edit products page</summary>
        <img src="./readme-files/imgs/edit_products.jpg" alt="FoEdit products pageoter">
</details>


<details>
    <summary>Edit an individual product page</summary>
        <img src="./readme-files/imgs/edit_product.jpg" alt="Edit an individual product page">
</details>

### Features to be implemented

Due to time constraints I haven't been able to implement some of the changes I had planned.

<img src="./readme-files/imgs/todo.jpg" alt="Features to be implemented">

[Back to top ⇧](#table-of-contents)

# Project Architecture

<img src="./readme-files/imgs/architecture_design.jpg"/>

## Project settings structure

The configuration file is one of the most important elements in any Django project. Knowing this, I decided to divide the configuration files structure into four files, one of them being the base file, which will contain everything that is needed in any project environment, be it **production**, **development** or **testing**. The other three files are for development, testing and finally production environments.

For that, create a folder called `settings` inside the main project folder. Inside it, add the `development.py`, `testing.py`, `production.py` and `__init__.py` files. After that, take the base `settings.py` file (which is in the root of the main project folder) and move it into the settings folder.

We will do this so that within the `settings.py` file there are only elements that will be used in any of the environments, be it production, testing or development. However, whatever we need to create differently for each environment, we will put it in the files we just created.

For this project, both the development and test environments use the `sqlite` database locally, while the production environment uses the `Postgresql` database. That way, development and testing data doesn't mix with the data that will be in production. To do this kind of separation, we must place the database settings in their respective files.

See below how the project structure should look 👇

<img src="./readme-files/imgs/project_structure.jpg"/>

Now, we will need to open each file and add some settings.

[Back to top ⇧](#table-of-contents)

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

<img src="./readme-files/imgs/db_schema.jpg" alt="Database Schema">

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

### Newsletter Table

| Title      | Key in Database | Form Validation         | Data Type     |
| ---------- | --------------- | ----------------------- | ------------- |
| Id         | id              | Auto-increment          | Primary Key   |
| User email | user_email      | null=False, blank=False | EmailField    |
| Created At | created_at      | auto_now_add=True       | DateTimeField |

[Back to top ⇧](#table-of-contents)

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
- [Privacy Policy Generator](https://www.privacypolicygenerator.info/)

[Back to top ⇧](#table-of-contents)

# Testing 🔎

## HTML Validator

Page tested using [W3C HTML Checker](https://validator.w3.org/). No errors or warnings were found.

<img src="./readme-files/imgs/html_pass.jpg" alt="Screenshot of HTML validator">

## CSS Validator

Stylesheet tested using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/). No errors or warnings were found.

<img src="./readme-files/imgs/css_pass.jpg" alt="Screenshot of CSS validator">

## JavaScript Validator (JSHint)

All Javascript was tested using [JSHint]. No errors were found.

<img src="./readme-files/imgs/js_pass.jpg" alt="Screenshot of Javascript validator">

Three warnings related to Javascript version were raised but does not affect the code.

`eversion`: This option is used to specify the ECMAScript version to which the code must adhere.

`6` - To tell JSHint that your code uses ECMAScript 6 specific syntax. Note that not all browsers implement them.

You can find more explanation at [JSHint Docs](https://jshint.com/docs/options/).

## Accessibility and Performance testing

I used the Lighthouse automated tool from Developer Tools to perform site quality tests. The result is shown below.

<figure>
  <img src="./readme-files/imgs/lighthouse.jpg" alt="Acessilibity and Performance testing">
  <figcaption align="center">Performance/Accessibility</figcaption>
</figure>

## Test Driven Development (TDD)

<header>
    <div class="content">
        <h1>Coverage report:
            <span class="pc_cov">87%</span>
        </h1>
        <p class="text">
            <a class="nav" href="https://coverage.readthedocs.io">coverage.py v6.4.4</a>,
            created at 2022-10-26 17:11 +0000
        </p>
    </div>
</header>
<main id="index">
    <table class="index" data-sortable>
        <thead>
            <tr class="tablehead" title="Click to sort">
                <th class="name left" aria-sort="none" data-shortcut="n">Module</th>
                <th aria-sort="none" data-default-sort-order="descending" data-shortcut="s">statements</th>
                <th aria-sort="none" data-default-sort-order="descending" data-shortcut="m">missing</th>
                <th aria-sort="none" data-default-sort-order="descending" data-shortcut="x">excluded</th>
                <th class="right" aria-sort="none" data-shortcut="c">coverage</th>
            </tr>
        </thead>
        <tbody>
            <tr class="file">
                <td class="name left">candycaredublin/__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">candycaredublin/settings/__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">candycaredublin/settings/development.py</a></td>
                <td>8</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="8 8">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">candycaredublin/settings/settings.py</a></td>
                <td>29</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="29 29">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">candycaredublin/settings/testing.py</a></td>
                <td>8</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="8 8">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">candycaredublin/urls.py</a></td>
                <td>3</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="3 3">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">env.py</a></td>
                <td>8</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="8 8">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">home/__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">home/admin.py</a></td>
                <td>1</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="1 1">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">home/apps.py</a></td>
                <td>4</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="4 4">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">home/migrations/__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">home/models.py</a></td>
                <td>1</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="1 1">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">home/tests.py</a></td>
                <td>10</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="10 10">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">home/urls.py</a></td>
                <td>3</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="3 3">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">home/views.py</a></td>
                <td>3</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="3 3">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">manage.py</a></td>
                <td>12</td>
                <td>2</td>
                <td>0</td>
                <td class="right" data-ratio="10 12">83%</td>
            </tr>
            <tr class="file">
                <td class="name left">products/__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">products/admin.py</a></td>
                <td>9</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="9 9">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">products/apps.py</a></td>
                <td>4</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="4 4">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">products/migrations/0001_initial.py</a></td>
                <td>6</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="6 6">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">products/migrations/__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">products/models/Models_Category.py</a></td>
                <td>10</td>
                <td>1</td>
                <td>0</td>
                <td class="right" data-ratio="9 10">90%</td>
            </tr>
            <tr class="file">
                <td class="name left">products/models/Models_Product.py</a></td>
                <td>12</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="12 12">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">products/models/__init__.py</a></td>
                <td>3</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="3 3">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">products/tests/__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">products/tests/test_models.py</a></td>
                <td>29</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="29 29">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">products/tests/test_views.py</a></td>
                <td>13</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="13 13">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">products/urls.py</a></td>
                <td>3</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="3 3">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">products/views.py</a></td>
                <td>41</td>
                <td>26</td>
                <td>0</td>
                <td class="right" data-ratio="15 41">37%</td>
            </tr>
            <tr class="file">
                <td class="name left">profiles/__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">profiles/admin.py</a></td>
                <td>1</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="1 1">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">profiles/apps.py</a></td>
                <td>4</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="4 4">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">>profiles/forms.py</a></td>
                <td>18</td>
                <td>1</td>
                <td>0</td>
                <td class="right" data-ratio="17 18">94%</td>
            </tr>
            <tr class="file">
                <td class="name left">profiles/migrations/0001_initial.py</a></td>
                <td>8</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="8 8">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">profiles/migrations/__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">profiles/models/Models_Profile.py</a></td>
                <td>21</td>
                <td>1</td>
                <td>0</td>
                <td class="right" data-ratio="20 21">95%</td>
            </tr>
            <tr class="file">
                <td class="name left">profiles/tests/__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">profiles/tests/test_forms.py</a></td>
                <td>9</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="9 9">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">profiles/tests/test_models.py</a></td>
                <td>41</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="41 41">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">profiles/tests/test_views.py</a></td>
                <td>13</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="13 13">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">profiles/urls.py</a></td>
                <td>3</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="3 3">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">profiles/views.py</a></td>
                <td>18</td>
                <td>11</td>
                <td>0</td>
                <td class="right" data-ratio="7 18">39%</td>
            </tr>
            <tr class="file">
                <td class="name left">shopping_bag/__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">shopping_bag/admin.py</a></td>
                <td>1</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="1 1">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">shopping_bag/apps.py</a></td>
                <td>4</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="4 4">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">shopping_bag/migrations/__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">shopping_bag/models.py</a></td>
                <td>1</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="1 1">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">shopping_bag/templatetags/__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">shopping_bag/templatetags/bag_tools.py</a></td>
                <td>5</td>
                <td>1</td>
                <td>0</td>
                <td class="right" data-ratio="4 5">80%</td>
            </tr>
            <tr class="file">
                <td class="name left">shopping_bag/tests/__init__.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">shopping_bag/tests/test_views.py</a></td>
                <td>24</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="24 24">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">shopping_bag/urls.py</a></td>
                <td>3</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="3 3">100%</td>
            </tr>
            <tr class="file">
                <td class="name left">shopping_bag/views.py</a></td>
                <td>17</td>
                <td>11</td>
                <td>0</td>
                <td class="right" data-ratio="6 17">35%</td>
            </tr>
        </tbody>
        <tfoot>
            <tr class="total">
                <td class="name left">Total</td>
                <td>411</td>
                <td>54</td>
                <td>0</td>
                <td class="right" data-ratio="357 411">87%</td>
            </tr>
        </tfoot>
    </table>
    <p id="no_rows">
        No items found using the specified filter.
    </p>
</main>

---

## Manual tests

Some manual tests were performed to ensure the correct functioning of the application.

 <strong>Implementation</strong> 🔨:
When I had set up the products.json and loaded into the database I could then view all available products. That way, I could ensure all ones were loaded as expected and that products information was visible when selected.

- <strong>Test</strong> 🔎:
To test this, I went through each product and loaded the its information page, then looked at changing the url to ensure each item was loading correctly.

- <strong>Result</strong> 🏆:
All products were loaded as expected to the main store page. When amending the url all products again loaded as expected. However, if I tried to access an product slug that didn't exist I was presented with a 404 page.

- <strong>Verdict</strong> ✅:
This test passed and no amendments were required.

---

 <strong>Implementation</strong> 🔨:
The system admin will only be able to access the 'Add product' or 'Edit an existing product' pages if they are properly logged into the system.

- <strong>Test</strong> 🔎:
To test this, I went through the browser and tried to access the endpoint `/api/add_product` or `/api/edit_product`. 

- <strong>Result</strong> 🏆:
As a result, I was automatically redirected to the login page and the endpoint that appears in the URL is `auth/login/?next=/api/add_product/`, which means that after being properly logged in I will be redirected to the 'Add product' page.

- <strong>Verdict</strong> ✅:
This test passed and no amendments were required.

---

 <strong>Implementation</strong> 🔨:
What happen if another user (non admin) try to access the 'Add product' or 'Edit an existing product' pages by the URL endpoints even if they are properly logged into the system?

- <strong>Test</strong> 🔎:
To test this, I went through the browser and tried to access the endpoint `/api/add_product` or `/api/edit_product`. Then I was automatically redirected to the login page and the endpoint that appears in the URL is `auth/login/?next=/api/add_product/`.

- <strong>Result</strong> 🏆:
As a result, I was automatically redirected to the home page and an error message was shown: *It appears you tried to access a page that you do not have permission. Please contact the store owner for assistance.*.

- <strong>Verdict</strong> ✅:
This test passed and no amendments were required.

---

 <strong>Implementation</strong> 🔨:
To make sure that the user can navigate the site easily, I have tested the navigation of all items, links, buttons, etc., in order to ensure that the user does not get lost within the application sessions.

- <strong>Test</strong> 🔎:
This test was performed in a systematic way, so that each page was navigated, clicked on all the links, in order to ensure that the user knew how to "find himself" within the site.

- <strong>Result</strong> 🏆:
Every page and link was checked and each provided a positive result, in no time was the user sent to an unexpected destination.

- <strong>Verdict</strong> ✅:
This test completed as expected without bugs.

---

## Testing User Stories

| Issue ID                                                                          | User Story                                           | Requirement to be met                                                                                                                                                                                     | Requirement met                                                                                                                                                                                                                 | Test result         |
| --------------------------------------------------------------------------------- | ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| [[#1](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/1)]   | View a list of products                              | As a Shopper I want to be able to view a list of products so that I can select some to purchase.                                                                                                          | The list with all products is displayed as soon as the user clicks on "Shop"                                                                                                                                                    | Passed ✅            |
| [[#2](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/2)]   | View individual product details                      | As a Shopper I want to be able to view individual product details so that I can identify the price, description, and product image.                                                                       | A product's detail page is displayed once the user clicks on the chosen product.                                                                                                                                                | Passed ✅            |
| [[#3](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/3)]   | Identify deals                                       | As a Shopper I want to be able to quickly identify deals, clearance items and special offers so that I can take advantage of special savings on products I would like to purchase.                        | This feature was not implemented in this project.                                                                                                                                                                               | To be implemented 🔨 |
| [[#4](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/4)]   | View total of my purchase                            | As a Shopper I want to be able to easily view the total of my purchases at any time so that I can be aware of how much I've already spent and avoid spending too much.                                    | The user can see the total expenses as they add items to the shopping bag                                                                                                                                                       | Passed ✅            |
| [[#5](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/5)]   | Register for an account                              | As a Site user I want to be able to easily register for an account so that I can have a personal account and be able to view my profile.                                                                  | 🐞 Bug Report: Verification email is not sent after sign up. [[#32](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/32)]                                                                                   | Fixed ✅             |
| [[#6](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/6)]   | login or logout                                      | As a Site user I want to be able to easily login or logout from my account so that I can access my personal account information.                                                                          | There's a 'Sign in' link in the top of the page where the user can easily login into the application. Once they're logged, a 'Sign out' link appears.                                                                           | Passed ✅            |
| [[#7](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/7)]   | Recover password                                     | As a Site user I want to be able to easily recover my password in case I forget it so that I can recover access to my account.                                                                            | The user is able to request a password recovery.                                                                                                                                                                                | Passed ✅            |
| [[#8](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/8)]   | Confirmation email after registering                 | As a Site user I want to be able to receive a confirmation email after registering so that I can verify that my account registration was successful.                                                      | 🐞 Bug Report: Verification email is not sent after sign up. [[#32](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/32)]                                                                                   | Fixed ✅             |
| [[#9](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/9)]   | Personalized profile                                 | As a Site user I want to be able to have a personalized user profile so that I can view my personal order history and order confirmations, and save my payment information.                               | Not implemented yet                                                                                                                                                                                                             | Passed ✅            |
| [[#10](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/10)] | List of available products                           | As a Shopper I want to be able to sort the list of available products so that I can easily identify the best priced and categorically sorted products.                                                    | The user can see the list of all available products.                                                                                                                                                                            | Passed ✅            |
| [[#11](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/11)] | Specific product category                            | As a Shopper I want to be able to sort a specific category of product so that I can find the best-priced or best-rated product in a specific category, or sort the products in that category by name.     | This feature was not implemented in this project.                                                                                                                                                                               | To be implemented 🔨 |
| [[#12](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/12)] | Multiple categories                                  | As a Shopper I want to be able to sort multiple categories of products simultaneously so that I can find the best-priced or best-rated product across broad categories, such as "vegan" or "best sellers. | This feature was not implemented in this project.                                                                                                                                                                               | To be implemented 🔨 |
| [[#13](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/13)] | Searching by occasion                                | As a shopper, I want to be able to search for products by occasion, such as "birthdays" or "father's day".                                                                                                | Feature partially implemented                                                                                                                                                                                                   | Passed ✅            |
| [[#14](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/14)] | Feedback about my searching                          | As a Shopper I want to be able to easily see what I have searched for and the number of results so that I can quickly decide whether the product I want is available.                                     | This feature was not implemented in this project.                                                                                                                                                                               | To be implemented 🔨 |
| [[#15](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/15)] | Select the type and quantity                         | As a Shopper I want to be able to easily select the type and quantity of a chocolate/cake/sweet when purchasing it so that I can ensure I don't accidentally select the wrong product, quantity or type.  | The user can update the shopping bag by adding quantity or removing items.                                                                                                                                                      | Passed ✅            |
| [[#16](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/16)] | Items in my shopping bag                             | As a Shopper I want to be able to view items in my bad to be purchased so that I can identity the total cost of my purchase and all items I will receive.                                                 | The user is able to clearly identify items in their bag before purchase as well as the total cost of the purchase.                                                                                                              | Passed ✅            |
| [[#17](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/17)] | Make changes to a individual product                 | As a Shopper I want to be able to adjust the quantity of a individual product in my shopping bag so that I can easily make changes to my purchase before checkout.                                        | The user can update the shopping bag by adding quantity or removing items.                                                                                                                                                      | Passed ✅            |
| [[#18](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/18)] | Payment information                                  | As a Shopper I want to be able to easily enter my payment information so that I can check out quickly and with no hassles.                                                                                | The user can easily enter their payment information.                                                                                                                                                                            | Passed ✅            |
| [[#19](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/19)] | Personal and payment information are safe and secure | As a Shopper I want to be able to ensure my personal and payment information are safe and secure so that I can confidently provide the needed information to make a purchase.                             | The user can note a  ”https” at the beginning of the URL as well as the closed lock or unbroken key in the browser, which indicates all data will be secure and encrypted when submitted on that website.                       | Passed ✅            |
| [[#20](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/20)] | Order confirmation                                   | As a Shopper I want to be able to view an order confirmation right after checkout so that I can verify that I haven't made any mistakes.                                                                  | The user can see right after checkout an order summary, detailing the purchase. Also, the user receives an email with the order confirmation.                                                                                   | Passed ✅            |
| [[#21](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/21)] | Email confirmation after purchase.                   | As a Shopper I want to be able to receive an email confirmation after checking out so that I can keep the confirmation of what I have purchased for my records.                                           | 🐞 Bug Report: Confirmation email not sent after checkout. [[#31](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/31)                                                                                      | Fixed ✅             |
| [[#22](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/22)] | Add a product.                                       | As a Store Owner I want to be able to add a product so that I can add new items to my store.                                                                                                              | Once the store owner is logged in, it is possible to see the 'Product Management' link in the menu at the top of the page. Upon clicking, the admin will see the option to add a new product and edit an existing product. yet. | Passed ✅            |
| [[#23](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/23)] | Edit/update a product                                | As a Store Owner I want to be able to edit/update a product so that I can change product prices, descriptions, images and other product criteria.                                                         | Once the store owner is logged in, it is possible to see the 'Product Management' link in the menu at the top of the page. Upon clicking, the admin will see the option to add a new product and edit an existing product. yet. | Passed ✅            |
| [[#24](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/24)] | Delete a product                                     | As a Store Owner I want to be able to delete a product so that I can remove items that are no longer for sale.                                                                                            | On the product editing page, at the bottom of the page you can see a field with information for deleting the product and a button to confirm the action. When clicking, a modal opens. yet.                                     | Passed ✅            |
| [[#25](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/25)] | Searching by keywords.                               | As a Shopper I want to be able to search for a product by keywords such as "chocolate" or "cakes" so that I can receive recommendations of the best products according to my search criteria.             | This feature won't be implemented in this project.                                                                                                                                                                              | To be implemented 🔨 |
| [[#26](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/26)] | Action messages.                                     | As a Shopper I want to be able to see a message informing me of an action I took on the site so that I can be aware of what I've done, such as when I remove an item or add an item to the shopping bag.  | The user can see a message box pops up upon they make any change such as login/logout, add/update/delete a product, checkout, and so on.                                                                                        | Passed ✅            |
| [[#33](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/33)] | Add a newsletter signup form to the application.     | As a Site user I want to be able to sign up for a newsletter so that I can stay on top of store news.                                                                                                     | The user is able to sign up to the newsletter and their contact will be saved in the store database for further promotions and deals. yet.                                                                                      | Passed ✅            |

---

## Bugs Report 🐞

| Bug ID                                                                            | Bug description                               | Current behaviour                                                                                                                   | Expected behaviour                                                                                                                          | Status  |
| --------------------------------------------------------------------------------- | --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| [[#31](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/31)] | Confirmation email not sent after checkout.   | After the user completes the purchase, the purchase summary is displayed, however, the confirmation email is not sent.              | After the user completes the purchase, it is expected that a confirmation email will be sent to the email provided at the time of purchase. | Fixed ✅ |
| [[#32](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/32)] | Verification email is not sent after sign up. | After the user signs up for the application, the verification email is not sent, resulting in a 404 error/crashing the application. | After the user signs up for the application, an email is expected to be sent to the email address provided at the time of sign-up.          | Fixed ✅ |
| [[#34](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/34)] | Issues in sign in/sign up form are present    | Once I access the sign in and sign up form, I see that there are navigability issues. The form works, but it's not visibly nice.    | That it is visibly pleasant and without navigability problems.                                                                              | Fixed ✅ |


## Bugs resolution 👷⛏

| Bug ID                                                                            | Bug description                             | Current behaviour                                                                                                      | Expected behaviour                                                                                                                          | Status  |
| --------------------------------------------------------------------------------- | ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| [[#31](https://github.com/emidiovaleretto/candy-care-dublin-ecommerce/issues/31)] | Confirmation email not sent after checkout. | After the user completes the purchase, the purchase summary is displayed, however, the confirmation email is not sent. | After the user completes the purchase, it is expected that a confirmation email will be sent to the email provided at the time of purchase. | Fixed ✅ |


I was trying to connect the `EMAIL_BACKEND` with the smtp service from Google. I already had use this services previously, so I set up all my credentials as usual in `env.py` and exported them into `settings.py` in order to send confirmation email to customers as well as send email to users upon their registration in the application, password recovery, and so on. Basically, I had to go into my Google Account and turn off the **Less secupe apps** verification. As a result, it was possible for third-party applications to gain access to the account. However, as per Google Documentation, which can be find [here](https://support.google.com/accounts/answer/6010255), *"To help keep your account secure, from May 30, 2022, ​​Google no longer supports the use of third-party apps or devices which ask you to sign in to your Google Account using only your username and password."*

Given that, Google now requires that you have **2-Step-Verification** enabled before you can set up an application password.

_Note: If you are seeing a message “The setting that you are looking for is not available for your account.” you should enable 2-Step-Verification first._

To fix it, I went through my Google Account, then **Security** and finally click in **App passwords**.

<img src="./readme-files/imgs/google_steps.jpg" alt="Google Steps">

Once this is done, the **App password** window will open and you needed to generate a password to use in the application.

<img src="./readme-files/imgs/app_passwords.jpg" alt="App password">

In the Select app dropdown menu, choose the app you’re using. You can also select Other and enter you own custom app name.

<img src="./readme-files/imgs/app_passwords_2.jpg" alt="App password">

And then a password will be generated.

<img src="./readme-files/imgs/app_passwords_3.jpg" alt="App password">

Make sure to copy and secure your generated password before click in *Done*.

Once this is done, just replace the default password of your email with the generated password and the application will be able to send emails using Google's smtp service.

---

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

[Back to top ⇧](#table-of-contents)

## Database setup

1. To set up your database you will first need to run the following command:

   python3 manage.py migrate

2. Then you need to create a **superuser**. This will allow you to access the application's admin panel. To do so, run the following command in your terminal and fill in the required information as prompted.

   python3 manage.py createsuperuser

3. Now you should be able to run the server using the following command:

   python3 manage.py runserver

If everything has been correctly configure you should not get a message giving you a link to your locally hosted site usually at http://127.0.0.1:8000

1. Finally, stop the server by pressing CTRL + C (or cmd + C on Mac) and run the following command to populate the database.

   python3 manage.py loaddata category.json
   python3 manage.py loaddata occasions.json
   python3 manage.py loaddata products.json

After running this command, all information contained in the `category.json`, `occasions.json` and `products.json` files will be saved in the database. Once that's done, run the `python3 manage.py runserver` command again and you should be able to see the application working.

## Stripe | Payment Processing Platform for the Internet

Before we move forward deploying the app to Heroku, it is recommended that you create a account on Stripe to use the payment processing functionality.

_Note: the application is set up for test payments only._

Follow the steps below to create an account and retrieve the necessary keys that you will need later:

1. Create an account at [Stripe](https://dashboard.stripe.com/register).
2. Upon the account was created, goto the [Account Dashboard](https://dashboard.stripe.com/test/dashboard).
3. After that, click in *Developers* - you will find on the right side, at the top of the page -, then click in [API keys](https://dashboard.stripe.com/test/apikeys).

You will see something like this:

<img src="./readme-files/imgs/api_keys.jpg" alt="API keys">

4. You will see the `Publishable key` and `Secret key`. _**Caution**: Make sure to **DO NOT** expose your Secret Key._ Keep both keys private by using environment variables. Later, you will need them to set the Heroku `Config Vars`.

|       Stripe Key       |          Value           |
| :--------------------: | :----------------------: |
| STRIPE_PUBLISHABLE_KEY |  [Your Publishable Key]  |
|   STRIPE_SECRET_KEY    | [Your Stripe Secret Key] |

## Testing Payment Intents with Stripe

As a way of exemplifying how the payment functionality works, Stripe provides three types of payment events and their respective card numbers: successful payment, requires authentication and failed payment. Below you will see a table with these events and their card numbers. _Note that when using the application, you **MUST NOT** enter any real card numbers. Therefore, Stripe already makes these cards available for testing._ 

|      Payment event      |     Card Number     |
| :---------------------: | :-----------------: |
|   Successful payment    | 4242 4242 4242 4242 |
| Requires authentication | 4000 0025 0000 3155 |
|     Failed payment      | 4000 0000 0000 9995 |

**Additional information**:

- Use a valid future date, such as 12/34.
- Use any three-digit CVC.
- Use any value you like for other form fields (you may be asked to enter a ZIP code).

<img src="./readme-files/imgs/payment_field.jpg" alt="A screenshot of the payment field">

## Setting up heroku

To set up heroku you must:

1. If your requirements.txt file has not changed you can skip this step. Otherwise, in your terminal type `pip freeze > requirements.txt` then save and push the changes.
2. Go to Heroku.com and sign in to your account or create a free one at [Heroku](https://www.heroku.com/).
3. From the heroku dashboard click the 'Create new app' button.
4. Name the app something unique and choose what region you are in then click 'Create app'.
5. In the resources section, in the _add-ons_ field, type `Heroku Postgreslq` and select the free cost option.
6. Now, go to the settings tab and find the Config Vars section. Click 'Reveal Config Vars'.

In the settings tab, select Reveal Config Vars and copy the pre populated `DATABASE_URL` into your `settings.py` file in your project in the Config Vars in Heroku you will need to populate with the following keys:

|          Key           |          Value           |
| :--------------------: | :----------------------: |
| SECRET_KEY_PRODUCTION  |    [Your Secret Key]     |
|    DEBUG_PRODUCTION    |          False           |
|       HEROKU_DB        |   [Your DATABASE URL]    |
|      HEROKU_HOST       |    [Your Heroku Host]    |
| STRIPE_PUBLISHABLE_KEY |  [Your Publishable Key]  |
|   STRIPE_SECRET_KEY    | [Your Stripe Secret Key] |

7.  Then head over to the deploy section by clicking deploy from the nav bar at the top of the page.
8.  From the 'Deployment method' section select GitHub and click 'Connect to GitHub'.
9.  Enter the repository name as it is in GitHub and click 'search'.
10.  Click the 'connect' button next to the repository to link it to heroku.
11.  To deploy, scroll down and click the 'Deploy Branch' button.
12.  Heroku will notify you that the app was successfully deployed with a button to view the app.
13.  If you want to rebuild your app automatically you can also select the 'Enable Automatic Deploys' button which will then rebuild the app every time you push any changes.

[Back to top ⇧](#table-of-contents)

# Credits

## Media

   - [Pexels](https://www.pexels.com/) - All images were downloaded from the website.
   - [Freepik](https://www.freepik.com/) - For icons.
   - [Table of contents](https://ecotrust-canada.github.io/markdown-toc/)
   - [Code Institute](https://codeinstitute.net/)


# Acknowledgements

I would like to take the opportunity to thank:

- To God first, to my family, friends and colleagues for their advice, support and help with testing.
- To my mentor Richard Wells for their feedback, advices, support and, above all, for their patience.
- All Code Institute Tutors, Student Care and Community on Slack for the peer reviews and advice.

# Disclaimer

> \***_Disclaimer_**: The following Context is completely fictional, the company, the context, the CEO, the business questions exist only in my imagination.

> \*\*For educational purposes only.

# Author

Made with ❤️ by <b>Emidio Valereto</b> <img src="https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/wave.gif" width="16px"> Get in touch!

[![Linkedin Badge](https://img.shields.io/badge/-Emidio-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/emidiovalereto/)](https://www.linkedin.com/in/emidiovalereto/) [![Gmail Badge](https://img.shields.io/badge/-emidio.valereto@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:emidio.valereto@gmail.com)](mailto:emidio.valereto@gmail.com)

[Back to top ⇧](#table-of-contents)
