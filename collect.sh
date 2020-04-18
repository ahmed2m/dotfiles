#!/bin/bash

echo Starting collecting config folders...

PWD=`pwd`
while read TARGET; do
    SOURCE=`echo $TARGET/ | sed "s,~,$HOME,g"`
    if [[ ${TARGET:0:1} == "~" ]]
    then
        DESTINATION=`echo $TARGET | sed "s,~,$PWD,g"`
    else
        DESTINATION="$PWD/root$TARGET"
    fi
    DESTINATIONDIR=`dirname $DESTINATION`
    mkdir -p $DESTINATIONDIR
    echo $TARGET
    rsync -r --exclude-from '.rsyncignore' $SOURCE $DESTINATION
done < ./list

echo $'\nStarting collecting config files...'

while read TARGET; do
    SOURCE=`echo $TARGET | sed "s,~,$HOME,g"`
    if [[ ${TARGET:0:1} == "~" ]]
    then
        DESTINATION=`echo $TARGET | sed "s,~,$PWD/files,g"`
    else
        DESTINATION="$PWD/files/root$TARGET"
    fi

    DESTINATIONDIR=`dirname $DESTINATION`
    mkdir -p $DESTINATIONDIR
    echo $TARGET
    rsync $SOURCE $DESTINATION
done < ./list_files

echo Done.
