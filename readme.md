## How to dpeloy on pythonanywhere

- Create a new web app
- Manual configuration
- Select my python<version> **very important must be same as python version mentioned in deploy.sh > create virtual env step, prefer 3.13 in both
- choose next and create app
- change virtual env path (just type myenv and it will asusme the path) (you can do this even if virtual env has not been created)

- Inside Web app
    - choose static url and path 
        - static url /static/
        - static path /fullpath to static folder inside same folder manage.py rests

    - choose media url and path 
        - media url /media/
        - media path /fullpath to media folder inside same folder manage.py rests

- WSGI configuration file
    - /var/www/hns499_pythonanywhere_com_wsgi.py
    - add project base directory
    - add settings.project_name
    - save

- Bash console
    - nano deploy.sh
    - paste deploy.sh code in there (pushed to the repo)
    - save and exit
    - chmod +x deploy.sh
    - run ./deploy.sh
    - cd repo folder (home/username/repo/)
    - nano .env
    - paste EMAIL_USER=""
            EMAIL_PASS=""
            DJANGO_SECRET_KEY = ""

