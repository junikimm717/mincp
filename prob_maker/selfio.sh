FILE=$1

[ -f "$FILE.cpp" ] && exit 1
cp -r "$CP_SETUP_DIR/templates/selfio_template" .
NAME=$1
mv selfio_template $NAME
