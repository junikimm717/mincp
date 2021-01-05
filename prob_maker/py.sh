FILE=$1

[ -f "$FILE.py" ] && exit 1
cp -r "$CP_SETUP_DIR/templates/python_template" .
NAME=$1
mv python_template $NAME