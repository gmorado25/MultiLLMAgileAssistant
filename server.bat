cd server
Call .project_env/Scripts/activate
cd src
python manage.py makemigrations app
python manage.py migrate
python manage.py runserver