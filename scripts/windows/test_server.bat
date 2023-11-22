cd "%1"
Call server/.project_env/Scripts/activate
cd server/src
python manage.py test
pause