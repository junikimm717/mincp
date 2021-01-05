FILE=$1

[ -f "$FILE.rs" ] && exit 1
cp -r "$CP_SETUP_DIR/templates/rust_template" .
NAME=$1
mv rust_template $NAME
