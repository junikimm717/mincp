FILE=$1

[ -f "$FILE.java" ] && exit 1
cp -r "$CP_SETUP_DIR/templates/minjava_template" .
NAME=$1
mv minjava_template $NAME