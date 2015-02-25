#! /bin/bash
. env.sh
for dir in 0[0-9][0-9]*
do
    cd $dir && make $1
    cd ../
done
