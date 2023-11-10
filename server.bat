cd server
Call .project_env/Scripts/activate
cd src
Set "DEBUG=true"
python manage.py makemigrations prompt_library
python manage.py migrate
python manage.py runserver