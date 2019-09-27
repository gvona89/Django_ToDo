**DO NOTE COMMIT __pycache__  DIRECTORIES**

1. cd into the nix-custom directory
1. enter the django BASH environment

  nix-shell -A generalAssembly.environments.djangoenv ./shell.nix
1. cd to a directory where you want your project
1. start a new project

  django-admin startproject todolist
1. enter toplevel project directory 

  cd todolist
1. create a new app called todoitemApp

  python ./manage.py startapp todoitemApp
1. add the app to your settings.py

  ```
  INSTALLED_APPS = [
    ...
    'todoitemApp'
  ]
  ```
1. add django rest framework config to settings.py

  ```
  REST_FRAMEWORK = {
      'DEFAULT_PERMISSION_CLASSES': [
          'rest_framework.permissions.AllowAny',
      ]
  }
  ```
1. edit your todoitemApp/models.py to replicate the one in this project 
1. edit todoitemApp/serializers.py to replicate the one in this project
1. edit todoitemApp/views.py to replicate the one in this project 
1. edit todoitemApp/urls.py to replicate the one in this project
1. AFTER MODIFYING todoitemApp/models.py run:

		python ./manage.py makemigrations
		python ./manage.py migrate
1. run your server using the command described above
1. NOTE: you need to have the trailing slash for HTTP request coming from your
   client (or other tools such as postman)
