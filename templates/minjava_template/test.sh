#!/bin/bash
PROG="Main"

# compilation stage.
javac $PROG.java
if [ $? -ne 0 ]; then
    exit 1
fi

# diffing program output against actual output. (modified for java)
for i in *.in; do
    name=`echo $i|sed "s/.in//"`
    echo -e "running test: $name \n"
    echo -e "INPUT:"
    cat $name.in

    echo -e "\nOUTPUT:"
    # clearing the .res files.
    if [ -f $name.res ]; then
        rm $name.res
    fi
    touch $name.res
    timeout 5s java $PROG < $name.in > $name.res
    if [ $? -eq 124 ]; then
        echo -e "time limit exceeded."
        rm -rf $name.res
        exit 1
    fi
    if [ $? -ne 0 ]; then
        exit 1
    fi

    cat $name.res
    if [ -f $name.out ]; then
        echo -e "ANSWER:"
        cat $name.out
        echo -e "\nDIFF:"
        diff $name.res $name.out
    fi
    echo "___________________________________"
    echo -e "\n"
done
exit 0
