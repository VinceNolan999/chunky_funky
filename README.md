# Chunky Funky Furninture

### [Link to Live Heroku hosted website](https://chunky-funky.herokuapp.com/)

## <u>Screenshots</u>

![screenshots](static/readme-docs/Preview.png) 

## A Python and Data Centric Development Project

- This is my Forth and final Milestone Project with Code Institute. Its purpose is to build a Full Stack Frameworks with Django site that allows users to purchase goods using a tested authentication procedure to prevent users bypassing the sites security mechanisms.  I have chosen a Custom furniture shop where users are able to view and purchase items.

---
## <u>Table of Contents</u>
- [Screenshots](#screenshots)
- [UX](#UX)
    - [User goals](#user-goals)
    - [User stories](#user-stories)
    - [Structure of the website](#structure-of-the-website)
- [Features](#features)
- [Technology Used](#technology-used)
- [Testing](#testing)
    - [Functionality testing](#functionality-testing)
    - [Compatibility testing](#compatibility-testing)
    - [Code Validation](#code-validation)
    - [User stories testing](#user-stories-testing)
    - [Issues found during site development](#issues-found-during-site-development)
    - [Performance testing](#performance-testing)
- [Deployment](#deployment)
- [Credits](#credits)
 
 ---
## <u>UX</u>

 ### User Goals
  
 #### New user Goals

- To create an account that enable the user to login and to logout.

- 

- To show A user profile that matches the registration details.

- 

- 

- 

- 

- 
 

#### Returning User Goals

-  

- 

### User Stories

#### As A New user.

- 

- I want to be able to log in and log out having a unique user account and password known only to me. 

- 
 
- 

- 

- 

#### As A returning user.

- I want to be able to log in and log out using a unique user account and password created by myself

- 

- 

- 

- 

#### Admin Owner Goals

- 

- Each user to have a unique login and secure password only known to them.

- ability for users to log out of the account.

- 

- 

- 

- 

- A Profile section for the user to verify there details.


### Structure of the website

- I want the website to be easily accessible, simple to navigate and user friendly. It must also be displayed 
  for various devices (desktop ,Tablet, Mobile Phone) whilst maintaining a great user experience . Links within the website taking me to other features

#### Database Schema

![MongoDB Schema](static/readme-docs/ms3schema.jpeg)

---
## <u>Features</u>

-  

- 
- 
- 

- 

#### Fonts

- The main font used is 'lato'  [Google-fonts](www.fonts.google.com)
   - Logo fonts of Bunge and  Monoton used. (also google fonts)

#### Images

- URL links to images displayed on the product page.

- Background Image of main landing page

#### Navbar and footer

- low profile navigation bar and footer

- Navbar located at top with brand name to the left and a responsive menu on the right for the account section.
    - When not logged in it displays the options of Login and Register. 
    - Logged in for a user will show options of profile and Logout. 
    - Logged in as a superuser will reveal the product management setion that allows the adding of products.
    - Logging in Removes login/register and replaces with logout.
- Shopping bag and Value Link (if applicable) - Links to Users shopping Bag.

#### Search section

- A selection of Buttons allowing searches by product type, split into two main categories of Indoors and Outdoors furniture (each has there own product category types revealed within). An all products link which can sort the products by Price, Rating and Category.

- A search bar allowing searches by Product name or description text.

- On mobile view the search categories are available as a Hamburger Drop down menu

- Footers located at the bottom with placeholder links to social media sites. In addition there is a section about the company.

#### Hero Image

- Fixed image wood workshop.

#### Toast Message display area. 

- To the right, a toast message will appear for the following actions.

    - 
    - 
    - 
    - 

#### Profile Page

-  Profile page displaying the username and delivery address details of the user. The address is displayed as a form and can be edited and updated. Username cannot be changed.  In addition the profile page displays the users previous orders,  this links to the order which contains information to that order including, date, product purchased , delivery address and Grand total.  A toast is also shown scecifying that this is a previous purchase made.

#### Product Page

#### Shopping Bag

#### Checkout Section

### Existing Features

- unique username creation

- password validation on registration form. 

- Customer orders and delivery details that are stored on a database and accessible to the user. 

- Superuser able to add new products to the database

#### Future Features 

- Facility for users to log in via existing social media accounts. 
  
- 

[Back to Table of contents](#table-of-contents)

---
## <u>Technology Used</u>


* [Django](https://www.djangoproject.com/)

  - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design

* [Amazon S3 via AWS](https://aws.amazon.com/)
  
  -  Object storage built to store and retrieve any amount of data from anywhere

* [Heroku](https://www.heroku.com/)

  - cloud platform for project deployment

* [Python](https://www.python.org/)

  - programming language. Utilizing the following tools:
  - Pymongo used to link python with mongo DB
  - Werkzeug password hash and username.

* [HTML5](https://en.wikipedia.org/wiki/HTML5)

  - Main Programming language

* [CSS](https://en.wikipedia.org/wiki/CSS) 

  - Style sheet language

* [JS](https://www.javascript.com/)

  - Used to create interactive functionality

* [Jquery](https://jquery.com/)

  - JavaScript library

* [Google Fonts:](https://fonts.google.com/)

  - Used to import custom fonts

* [Icons:](https://fontawesome.com/) 

  - Used to import icons

* [GitHub:](https://www.github.com.com)

  - Used to store projects created in gitpod. 

* [Gitpod:](https://www.gitpod.io.com)

   - Used to develop the project, including version control (using commits and comments.)
 
* [windows Photo editor](https://www.microsoft.com/en-us/p/photo-editor-for-windows-10/9mzwk7vt6b3g?activetab=pivot:overviewtab)

   - Basic photo editor

[Back to Table of contents](#table-of-contents)

---
## <u>Testing</u>

Continuous ongoing testing during development to ensure functions working correctly and as intended. Below is final test regime to confirm.

### User Not logged In
- Navbar 
    - Only access is to the Home and Login section.
    - Brand and Home button takes to correct page.
    - Pressing log in takes to correct screen.
    - Register link present. 
    - Registration form displays correctly.
    - form validation working correctly.
    - password validation works correctly.  Validation shows message 'passwords do not match'.
    - user created on MongoDB and profile page present when logged in.
    - Hamburger menu appears at relevant view width and drop down menu works correctly and correct links present and working.

- Search Section
  - all genre select buttons and the Wishlist button displaying the correct movie from the movie card details.
  - Search bar correctly display the movies by name or by movie description. 
  - Search and Reset button working as intended.

- Product categorys
  - displayed as inteneded. Pressing the card reveals information about the movie.  Movies without a correct Url image link display a stock
    placeholder image.
  - No access to edit facility

  - Shopping Bag

  - Checkout 

### User Logged In  

- Navbar 
  - Confrirmed that there is no access to the admin section.
  - Logged in user lands at the profile page, flash message displayed welcoming User.
  - flash message displayed if entering incorrect username or password.
  - Menu options goto the correct page.
  - Log Out works correctly.  Only options of home and Log in present, no ability to edit movies.

- Shopping Bag

- Search Section
  - all genre select buttons and the Wishlist button displaying the correct movie from the movie card details.
  - Search bar correctly display the movies by name or by movie description. 
  - Search and Reset button working as intended.

- Product Categorys
  - displayed as inteneded. Pressing the card reveals information about the film.  Films without a correct Url image link display a stock
    placeholder image.
  - access to edit facility. pressing the edit button takes you to the correct edit screen for the movie.

- Profile Section.
  - pressing takes you to the profile page, displaying username 

- Log out
  - session cookie is removed. No access to other features.
  - toast message confirming 'you are now logged out'

### Admin Logged In 

- 

- Product management
  
- Product views  ( edit and delete options)


### Functionality testing

- chrome Browser used to run Gitpod and developer tools used to test , solve problems, style and responsiveness.
Chrome developer tools used to check compatibility during project and to check on consistency.

- Mozilla Dev tools used to test in addition to chrome dev tools.    

- No issues detected.

### Compatibility testing

- I have tested the website on the virtual devices (including landscape orientation) contained with the Dev Tools of Mozilla and Chrome with no 
issues seen on either. A wide range of screen sizes tested from mobile, tablet and desktop.

- I have tested compatibility on the heroku published website of the project on a 1920 x 1080 monitor, a galaxy s7 
and a Motorola  one+ mobile phone with no issues noted

- The website was isubmtted for peer review and no Issues were mentioned

### Code Validation

-  https://jigsaw.w3.org/css-validator/   

    - This document validates as CSS level 3 + SVG.  Tested on each specific app address (products, bag etc) 

-  https://validator.w3.org/

    -  passes except for script type="text/javascript".  I have left these unchanged for legacy browsers.

-  https://wave.webaim.org/ - A web accessibility checker

    - Checked on all major pages. Showed 2 errors in connection with a missing label on the search bar and the empty button associated with it. I have left this as is as have inclused text in the button and also an aria-label.  no other errors or issues.

-  Pep8 validation.  This was completed using "python3 -m flake8" in the terminal interface. 

    - The code was refactored to a high level.  Most queries that remain are in the migrate or built in files.  The remaining items are mostly line too long for which I decided to leave as they were for readability purposes.



### User stories testing

- I want to be able to create a user account that allows further access

      -  The website has a user registration section where they can create an account and password 
         which allows access to other features, such as Adding or editing movie cards.         

- I want to be able to log in and log out having a unique user account and password known only to me.

      -  The username and password are stored on a server with the password being encrypted by 
         werkzeug (password_hash). This means even the admin does not have access to the password. 
         A log out function is also present that removes the session cookie and thus the user.

- I want to see Information about movies that are on the database

      -  On the main page there are Movie card tiles, pressing these tiles reveals 
         further information about the movie.
 
- I want to be able to add and edit movies on the database which records my user details within the database

      -  Only once registered and logged in, the user is able to edit existing movies and 
         add new movies to the database.

- I want to be able to delete movies from the database

      -  There is a delete button in the edit movie function. This requires 
         a confirmationary button press to delete.

- I want to be able to tag a movie that I would like and that shows in a separate search.

      -  A 'wish-list' toggle button has been included in the movie information. 
         This can be selected in the edit movie function or when you create a new movie.
         A specific 'Wish list' seach button is present in the main search area for quick access to 
         the wish list movies.


### Returning User Stories Testing

- I want to be able to log in and log out using a unique user account and password created by myself

      -  Unique Username, profile and password present on the site.

- I want to edit and add movies and have that action attributed to my account.

      -  As a registered user, you are able to edit and add movies. Doing so will 
         attribute the addition/change to that user by means of a 'created by' 
         section in the movie card listing.

- I want to be able to delete movies from the database

      -  A registered user is able to delete movies by way of a delete button, 
         a confirmationary button also needs to be pressed.

- I want to be able to search the database for movies

      -  The website includes 2 forms of searching. A button selection by Movie Genre's 
         (including 'Wish list' movies) and by a search bar that can search by movie title 
         or words in the description.

- I want to be able to flag movies that I would like to have.

      -  A toggle switch for a 'Wish list' is included in the edit and add movie forms. 
         This then allows all movies in the 'Wish list' to be displayed 
         by clicking the appropriate button in the seach menu.


### Admin Stories testing

- To create a website that users can access a catalog of Movies that they own or that they would like to own or watch.
          
      -  The website allows registered users to add there own movies and details about the movies. 
         They can flag a movie to place it in the wish list section for easier locating.

- Each user to have a unique login and secure password only known to them.

      -  Users can create there own username during registration and a password known only to them. 
         This is stored in a database with the password being encrypted using a password_hash. 

- ability for users to log out of the account.

      -  A log out facility is present once the user is logged in.  
         Logging out remove the session cookie for that user.

- Tasks such as editing and adding movies should display the users details.

      -  The movie card will display a 'created by' section in the Movie information. 
         This will display the users name.

- deleting movies should require a conformationally request to prevent accidental deletion.

      -  Movies can be deleted in the edit movie mode.  
         Pressing delete will bring up a modal button to confirm deletion.

- users should be able to search for movies, this to be by movie name, description, genre type or by 'wish list'

      -  The website includes 2 forms of searching. A button selection by Movie Genre's 
         (including 'Wish list' movies) and by a search bar that can search by movie title 
         or words in the description.

- A function that allows users to flag a movie that they would like to watch/own.  A Wish list.

      -  A toggle switch for a 'Wish list' is included in the edit and add movie forms.  
         This then allows all movies in the 'Wish list' to be displayed 
         by clicking the appropriate button in the seach menu.

- A Profile section for the user to verify there details.

      -  A basic profile page which displays the username and email is included once the user is logged in.

### Issues found during development

  - Checkout page not displaying correctly on mobile view.  To address this issue I created a mobile only view by using bootstrap display- none and block commands at certain break points. This worked as a good fix for the code, however a problem with the increment buttons was present. I decided to remove these as the mobile view was presented differently and this was the cleanest and quickest fix.

  - During the deployment of the project to Heroku, Gitpod has changed the installed apps that show in the requirements.txt.  This has caused Over 100+ entries into the req's file. In addition to this upon restart of the gitpod repository several apps require to be reinstalled each time via a terminal. However once this is done the site runs correclty on gitpod.  Testing has shown that this causes no issues with heroku (albeit a rather large Req's file.).  I was left with several options from cloneing the repo to creating a new branch.  This possibly could effect the continuity of the course material, So I have decided to leave the changes made by gitpod. To minimise the impact I created a copy of the actual required Requirements.txt file (named _copy),  and also a seperate file of the dependencies that I need to reinstall everytime the gitpod server is started.  This is a simple terminal command of "pip3 install -r reinstall.txt" . Although not ideal, at so close to submission deadline, with no other adverse effects present this was my safest option and the deployment via Heroku appears to be un-affected. 

### Performance testing

  - I have used [Lighthouse](https://developers.google.com/web/tools/lighthouse/) for the performance testing. No relevant errors present. Screen shots of the result are shown below.

#### Desktop performance

![Performance desktop](static/readme-docs/lh-desktop.jpg)

#### Mobile Performance

![Performance mobile](static/readme-docs/lh-mobile.png)


[Back to Table of contents](#table-of-contents)

---
## <u>Deployment</u>

Github used as version control for this project with deployment of the website via Heroku.

To deploy the project you will first need to clone the repository located at github.

A full walk-through from github is available here [cloning a repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository)

- Once cloned in the command terminal type:

- touch gitignore (if not present) and add the following:

      env.py
      --pycache--/
      *.sqlite3
      *.pyc

#### Create Environment Variables

- Create `env.py` file, add `import os` to the top of file and add these environment variables. Ensure that env.py is included in gitignore before you push to the repository or  include them in the heroku Config vars instead  (key , value).

      Env variables 
      ------------- 
      os.environ['DEVELOPMENT'] = True
      os.environ['SECRET_KEY'] = <your value> 
      os.environ['STRIPE_PUBLIC_KEY'] = <your value>
      os.environ['STRIPE_SECRET_KEY'] = <your value>
      os.environ['STRIPE_WH_SECRET'] = <your value>
      os.environ['AWS_ACCESS_KEY_ID'] = <your value>
      os.environ['AWS_S3_REGION_NAME'] = <your value>
      os.environ['AWS_SECRET_ACCESS_KEY'] = <your value> 
      os.environ['AWS_STORAGE_BUCKET_NAME'] = <your value> 
      os.environ['EMAIL_HOST_PASS'] = <your value> 
      os.environ['EMAIL_HOST_USER'] = <your value>
      os.environ['DEFAULT_FROM_EMAIL'] = <your value> 
      os.environ['UNSUBSCRIBE_URL'] = <your value> 
      os.environ['HEROKU_HOSTNAME'] = <your value> 

- The requirements.txt should contain the following dependencies:

  - To install the project dependencies type  ` "pip3 install -r requirements.txt"`

        asgiref==3.2.3
        boto3==1.12.42
        botocore==1.15.42
        chardet==3.0.4
        dj-database-url==0.5.0
        Django==3.0.1
        django-allauth==0.41.0
        django-countries==6.0
        django-crispy-forms==1.8.1
        django-storages==1.9.1
        docutils==0.15.2
        gunicorn==20.0.4
        idna==2.8
        jmespath==0.9.5
        oauthlib==3.1.0
        Pillow==7.0.0
        psycopg2-binary==2.8.5
        python3-openid==3.1.0
        pytz==2019.3
        requests==2.22.0
        requests-oauthlib==1.3.0
        s3transfer==0.3.3
        sqlparse==0.3.0
        stripe==2.42.0
        urllib3==1.25.7

- Add Procfile that contains:

      web: gunicorn chunky_funky.wsgi:application

#### Create SuperUser

- Type `"python3 manage.py createsuperuser"` and follow the instructions in the terminal.

#### Migrate

- Apply model migrations `"python3 manage.py makemigrations" (test by adding --dry-run)` followed by `"python3 manage.py migrate" (test by adding --plan)`.

#### Run Locally

- type '"python3 manage.py runserver"'

### How to deploy to deploy the project to the hosting platform Heroku:

- Create new app (must use dash or minus , use similar to repo name(or same as)

        - Region = europe (or your location)
        - CREATE APP
        - Deployment method  =  Github
        - Search for repo to connect to  (PRESS CONNECT)

- Under resources, search and select the add-on 'heroku postgres' database

Do not auto deploy just yet!!

- Goto settings at top. then reveal config vars.

    - Input values from the env.py file   (As listed above),  however exclude Development = True
      - Add to vars

               USE AWS = True
               DATADASE_URL = <your value>

    - You must push the new files to github (procfile and requirements.txt)  =  git status then gitcommits.

Enable automatic deploys  then Deploy branch (main)

### AWS

- Instructions for hosting media and static files with AWS S3 Bucket can be found [here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html)


[Back to Table of contents](#table-of-contents)

---
## <u>Credits</u>

### knowledge base and design ideas

* [Slack](https://slack.com/)

* [w3schools.com](https://www.w3schools.com)

* [codeinstitute](https://codeinstitute.net/) - On-going course progression and specifically the teaching material throught-out the course.

  - Specific credit for the walkthrough project of boutique ado for general help in creating the website

### Code Templates

- Various [Bootstrap](https://getbootstrap.com/) templates used.

### Content

- All content is added by the user.

- [icons8](https://icons8.com/icons/set/favicon) - Icons and favicons. 

### Media

- Images are dynamically loaded via a Url and added by a user.                                    

### Acknowledgments.

- Code Institute Pre-loaded github tools

[Back to Table of contents](#table-of-contents)