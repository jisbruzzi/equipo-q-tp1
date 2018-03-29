#!/bin/sh

set -e;

pycodestyle .

if [ $? -eq 0 ]; then
    echo "Codestyle OK";
fi

