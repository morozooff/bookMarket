<h1 align = "center"> BookMarket </h1>
<h1 align = "center" ><img src = "https://static.wikia.nocookie.net/minecraft/images/7/7c/WrittenBookNew.gif/revision/latest?cb=20200428051712" height = 256></h1>
<h2>Description</h2>
<a> <i>Hello, this is Django book market project. I think that the market project its a great idea for development on Django web-framework. Such a project will help learn the basics of web development and apply them in the mentioned framework. Welcome to the "TolStore" market and Let's go!</i> <a>
<h2>Technology stack</h2>
  <a> Before we begin review TolStore functional, I would like to talk about technology that I used during development.<a>
  <img width="50" src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" alt="Python" title="Python"/>
  <img width="47" src="https://static-00.iconduck.com/assets.00/django-icon-1606x2048-lwmw1z73.png" alt="Django" title="Django">
  <img width="50" src="https://user-images.githubusercontent.com/25181517/192158954-f88b5814-d510-4564-b285-dff7d6400dad.png" alt="HTML" title="HTML"/>
  <img width="50" src="https://user-images.githubusercontent.com/25181517/183898674-75a4a1b1-f960-4ea9-abcb-637170a00a75.png" alt="CSS" title="CSS"/>
<h2>Problems</h2>
    <div>
      The developed market should have the following functionality:
      <ol>
        <li>Display basic market pages</li>
          <ul>
            <li>Home</li>
            <li>About</li>
            <li>Catalog</li>
            <li>User profile</li>
          </ul>
        <li>Possibility of registration and authorization</li>
        <li>Store data about user</li>
        <li>Place orders and store data about orders</li>
        <li>Possibility filling basket and store basket state</li>
        <li>Search books on title, tags, author name in book market storage</li>
      </ol>
    </div>
<h2>Getting Started</h2>
<p>First, you need Python on your computer. <a href = "https://www.python.org/downloads/">Install Python</a>, if you already didn't it.</p>
<a>Then clone the repo</a>
    
``` 
git clone https://github.com/morozooff/bookMarket.git
```
 
<a>Then create venv</a>
    
```
python -m venv env_name
```

<a>Then install required packages</a>

```
pip install django
pip install djangorestframework
pip install crispy-bootstrap5
pip install Pillow 
```

<a>No one project wont work without SECRET_KEY, that localed in settings.py, so you need to generate it</a>

```
python manage.py shell
from django.core.management import utils
utils.get_random_secret_key()
```

<a>Then create superuser with your parametrs (name, password)</a>

```
python manage.py createsuperuser
```

<a>Then create new migration from django models</a>

```
python manage.py makemigrations
```

<a>Migrate it</a>

```
python manage.py migrate
```

<a>Then run this market on localhost</a>

```
python manage.py runserver
```

<a>Done! Now you can use this makret. To add book on market go to the django admin interface (URL: http://127.0.0.1:8000/admin/)</a>
  
<h2>Apps</h2>
    <div>
      Django project structure consists of several apps, that implement a modular approach to development.
      The developed market consists of following apps:
      <h4>market</h4>
      <a>This app implement market navigation and search logic and view</a>
      <h4>user</h4>
      <a>This app implement user autorization and registraion logic, realize store data about user and display profile info</a>  
      <h4>order</h4>
      <a>This app implement the logic of the market basket and ordering</a>
    </div>
<h2>Functional</h2>
<h3>Market pages</h3>
<h3>Book catalog</h3>
<h3>Registration/Autorization</h3>
<h3>Market basket</h3>
<h3>Market order</h3>
<h3>Profile page</h3>
<h3>Search engine</h3>
