# Create-Flask-App [![Trello](https://img.shields.io/badge/Trello-Contact%20Us-blue)](https://trello.com/b/Ve14hIA0/create-flask-app) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-green.svg)](https://github.com/isakal/create-flask-app/pull/new/master)

Flask port of [create-react-app](https://facebook.github.io/create-react-app/) that is used for initializing project structure of your next application.

- [Creating an app](#creating-an-app) - How to create a new app.

Create Flask app works on macOS, Windows and Linux.
If something doesn't wrong, please [file an issue](https://github.com/isakal/create-flask-app/issues/new).
If you have questions, suggestions or need help, please ask in our [Discord](https://discord.gg/qEnuyK) community.


## Quick overview 

```sh
pip install createflaskapp
create-flask-app my-app
cd my-app
# activate venv
python run.py
```
*(use correct version of [pip](https://pip.pypa.io/en/stable/) and [python](https://python.org/) according to your OS and python install)*
Then open [http://localhost:5000](http://localhost:5000) to see your app.
When you are ready to deploy to production, set environment variable `PRODUCTION` to  `True` on your server of choice, clone the project onto your server and spin it up.


## Creating an app

**You'll need to have Python 3.6 or higher on your local development machine** (but it's not required on the server).
To create a new app, you can run :

### bash
```sh
create-flask-app my-app 
```

### python
```sh
python -m create-flask-app my-app
```
It will create a directory called my-app inside the current folder.
Inside that directory, it will generate the initial project structure :
```
my-app/
├──venv
├── app
│   ├── __init__.py     
│   ├── config.py       
│   ├── errors
│   │   ├── __init__.py 
│   │   └── handlers.py 
│   ├── home
│   │   ├── __init__.py 
│   │   └── routes.py   
│   ├── static
│   │   └── css
│   │       └── main.css
│   └── templates     
│       ├── about.html
│       ├── base.html 
│       ├── error.html
│       └── home.html 
├── requirements.txt  
└── run.py
```

No complicated configuration or folder structures, only the files you need to build and deploy your app.
Once the installation is done, you can open your project folder:
```sh
cd my-app
```
Inside the newly created project, you can run some commands:

### `source venv/bin/activate` or `.\venv\Scripts\activate`
Activates the virutal environment required for the project dependency isolation.

[Read more about venv.](https://https://docs.python.org/3/library/venv.html)  

### `pip install -r requirements.txt`
Installs libraries and dependencies listed in `requirements.txt` in active environment.

### `python run.py`
Starts the app in development mode. 
Open [http://localhost:5000](http://localhost:5000) to view it in browser.

The page will automatically reload if you make changes to the code. 
You will see errors in app reload or startup in the console.


## How to Update to New Versions?

Create-Flask-App can be simply upgraded using pip:

```sh
pip install createflaskapp --upgrade
# or
pip install createflaskapp -U
```

## What's Included?

Your environment after installing everything from `requirements.txt` will have everything you need to build simple but modern Flask app:
- Isolated Python environment with fully functional pip.
- [Flask](https://www.palletsprojects.com/p/flask/), lightweight WSGI web application framework.
- A live development server that warns about errors and exceptions.
- [Jinja](https://jinja.palletsprojects.com/en/2.10.x/) template engine that is very fast and has very similar syntax to python.
- [Click](https://click.palletsprojects.com/en/7.x/), composable command line interface toolkit.

Check out [this guide](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) for an overview of how these tools fit toghether.
