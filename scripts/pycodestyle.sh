#!/bin/sh

set -e;

pycodestyle src/

if [ $? -eq 0 ]; then
    echo "Codestyle OK";
fi

