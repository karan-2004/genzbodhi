# Steps for set-up
## Run the following commands in your terminal(lines starting with # are annotations not for execution)
> #Creating a directory for the application

`mkdir genzbodhi`
> #Creating environment(make sure you have python and pip installed)

`pip install venv`

`python -m venv environment`

> #activating environment

> #for windows

`environment/Scripts/activate`

>#for linux

`source environment/bin/activate`

>#Cloning the repository

`git init .`

`git clone https://github.com/MANIKANDAN28072004/genzbodhi genzbodhi -b master`

>#changing the directory

`cd genzbodhi`

>#Installing dependencies

`pip install -r requirements.txt`

>#For database connectivity

`python manage.py makemigrations`

`python manage.py migrate`

# Now you are ready to run the application 
>#The final command

`python manage.py runserver`

## search `127.0.0.1:8000` in the browser







  
  
