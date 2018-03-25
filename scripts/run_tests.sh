#!/bin/sh

python -m unittest discover test/

if [ $? -eq 0 ]; then
    echo "Tests OK";
fi

