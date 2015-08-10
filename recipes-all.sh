#! /bin/bash
set -o errexit
. env.sh
for dir in 0[0-9][0-9]*
do
    echo "**** working in $dir"
    cd $dir && make $1
    cd ../
    echo "DONE $dir"
done
