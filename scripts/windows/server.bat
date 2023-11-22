cd "%1"
Call server/.project_env/Scripts/activate
cd server/src

python manage.py makemigrations prompt_library
python manage.py migrate
python manage.py runserver %SERVER_ADDRESS%:%SERVER_PORT%
pause