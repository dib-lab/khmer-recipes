#! /bin/bash
for dir in 0*
do
    cd $dir && make
    cd ../
done
