# Django Template 

###Installation

```commandline
mkdir PROJECT_NAME && cd $_
```
```commandline
python3.9 -m venv venv
```
```commandline
source venv/bin/activate
```
```commandline
pip install --upgrade pip
```
```commandline
pip install Django
pip install djangorestframework
pip install dynamic-rest
pip install django-cors-headers
pip install sentry-sdk
```
```commandline
python -m django startproject --template 'https://github.com/b93de3d/django-template/archive/master.zip' PROJECT_NAME .
```
Install the dummy config file and edit
```commandline
sudo cp example_config.json /etc/PROJECT_NAME_config.json
```
or use a local version with actual secrets:
```commandline
sudo cp /etc/example_config.json /etc/PROJECT_NAME_config.json
```
```commandline
git init
```
```commandline
git add .
```
```commandline
git commit -am "inital"
```
```commandline
python manage.py makemigrations
```
```commandline
python manage.py migrate
```
```commandline
python manage.py createsuperuser
```
```commandline
python manage.py runserver
```
