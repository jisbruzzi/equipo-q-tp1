#!/bin/sh
set -e

python -m nose

if [ $? -eq 0 ]; then
    echo "Tests OK";
fi

