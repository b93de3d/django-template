# Django Template 

##Installation

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
python -m django startproject --template https://github.com/b93de3d/django-template.git PROJECT_NAME .
```
```commandline
sudo cp /etc/example_config.json /etc/PROJECT_NAME_config.json
```
