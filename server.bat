cd server
Call .project_env/Scripts/activate
cd src
python manage.py makemigrations prompt_library
python manage.py migrate
python manage.py runserver