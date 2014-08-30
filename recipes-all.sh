#! /bin/bash
for dir in 0*
do
    cd $dir && make $1
    cd ../
done
