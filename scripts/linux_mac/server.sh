#! /bin/bash

cd $1
source server/.project_env/bin/activate
cd server/src

python3 manage.py makemigrations prompt_library
python3 manage.py migrate
python3 manage.py runserver ${SERVER_ADDRESS}:${SERVER_PORT}
read -n1 -r -p "Press any key to continue..." key