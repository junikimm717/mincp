FILE=$1

[ -f "$FILE.java" ] && exit 1
cp -r "$CP_SETUP_DIR/templates/java_template" .
NAME=$1
mv java_template $NAME