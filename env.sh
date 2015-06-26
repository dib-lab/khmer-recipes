#! /bin/bash
set -x
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

PYTHON_VIRTUALENV="$DIR/../ipy7/bin"
. ${PYTHON_VIRTUALENV}/activate
set -o nounset
set -o errexit
