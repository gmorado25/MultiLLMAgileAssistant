cd server
Call .project_env/Scripts/activate
cd src

Set "DEBUG=%1"
Set "AUTH_KEYS_FILE=%2"

python manage.py makemigrations prompt_library
python manage.py migrate
python manage.py runserver