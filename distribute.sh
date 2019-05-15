#!/bin/bash
python3 setup.py sdist bdist_wheel
twine upload dist/* --verbose
read -p "Delete build/ and dist/ [y/n/n]: "  answer
if [ "$answer" = "y" ]
then
    rm -d -r build/ dist/
fi
