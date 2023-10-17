cd server
source .project_env/bin/activate
cd src
python manage.py makemigrations app
python manage.py migrate
python manage.py runserver