cd server
source .project_env/bin/activate
cd src
export DEBUG=$1
python3 manage.py makemigrations prompt_library
python3 manage.py migrate
python3 manage.py runserver