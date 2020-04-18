#!/bin/bash

echo Starting spreading configs...

PWD=`pwd`
MYHOME="/home/ahmed/"
while read TARGET; do
    if [[ ${TARGET:0:1} == "~" ]]
    then
        SOURCE=`echo $TARGET | sed "s,~,$PWD,g"`
        DESTINATION=`echo $TARGET | sed "s,~,$MYHOME,g"`
    else
        SOURCE="$PWD/root$TARGET"
        DESTINATION="$TARGET"
    fi
    DESTINATION=`dirname $DESTINATION`
    mkdir -p $DESTINATION
    echo $TARGET
    rsync -r $SOURCE $DESTINATION
done < ./list

while read TARGET; do
    if [[ ${TARGET:0:1} == "~" ]]
    then
        SOURCE=`echo $TARGET | sed "s,~,$PWD/files,g"`
        DESTINATION=`echo $TARGET | sed "s,~,$MYHOME,g"`
    else
        SOURCE="$PWD/files/root$TARGET"
        DESTINATION="$TARGET"
    fi
    DESTINATION=`dirname $DESTINATION`
    mkdir -p $DESTINATION
    echo $TARGET
    rsync -r $SOURCE $DESTINATION
done < ./list_files

echo Done.
