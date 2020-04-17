#!/bin/bash

echo Starting collecting configs...

PWD=`pwd`
while read TARGET; do
    SOURCE=`echo $TARGET/ | sed "s,~,$HOME,g"`
    DESTINATION=`echo $TARGET | sed "s,~,$PWD,g"`
    DESTINATIONDIR=`dirname $DESTINATION`
    mkdir -p $DESTINATIONDIR
    echo $TARGET
    rsync -r --exclude-from '.rsyncignore' $SOURCE $DESTINATION
done < ./list

echo Done.
