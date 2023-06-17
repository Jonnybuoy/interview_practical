# Backend

This is the backend part of the project.

# How to install the project

## Prerequisites

Make sure you have the following before beginning:

```bash
python3-dev
git
pip
virtualenv
```

## Setting up the projects dependencies

Navigate into the projects directory from the terminal.
```bash
$ cd path/to/your/directory/interview_practical/practical_backend
```
Create a virtual environment for your project
```bash
$ python3 -m venv name-of-your-virtualenv
```
Activate your virtual environment.
```bash
$ source name-of-your-virtualenv/bin/activate
```
Install the requirements.
```bash
(name-of-your-virtualenv)$ pip3 install -r requirements.txt
```

## Running the project
To run the project:
```bash
(name-of-your-virtualenv)$ ./manage.py runserver # the information below will be displayed if everything is okay
Performing system checks...

System check identified no issues (0 silenced).
January 18, 2020 - 18:55:56
Django version 3.0, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Leave it running so that it can communicate with the frontend.