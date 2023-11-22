cd $1
source server/.project_env/bin/activate
cd server/src
python3 manage.py test
read -n1 -r -p "Press any key to continue..." key