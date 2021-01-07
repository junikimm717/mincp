[ -d input ] || exit 127
[ ! -f input/*.in ] && echo "no tests." && exit 127

make fast || exit 1

cd input
for T in *.in; do
    NAME=$(echo $T | sed "s/.in//g")
    timeout 5s ../Main < $NAME.in > ../output/$NAME.txt
    if [ $? -eq 124 ]; then
        echo "TLE"
        exit 124
    elif [ $? -ne 0 ]; then
        exit 1
    fi
done