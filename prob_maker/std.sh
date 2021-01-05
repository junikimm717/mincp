FILE=$1

[ -f "$FILE.cpp" ] && exit 1
cp -r "$CP_SETUP_DIR/templates/std_template" .
NAME=$1
mv std_template $NAME