#!/bin//bash

DIRECTORY="Memoria/"
TESIS="Tesis"
MAIN="main"

if [ -d ".git" ]; then
	cd $DIRECTORY
    echo "pdflatex $MAIN"
    pdflatex $MAIN
    echo "make"
    make
    echo "make clean"
    make clean
    cd ../
    echo "git status"
    git status
    echo "git add ."
    git add .
    echo "git status"
    git status
    echo "What's the name of the commit?"
    read commit
    git commit -m "$commit"
    echo "Do you want to push the changes? (Y/N):"
    read push
    if [ $push == "Y" ]; then
        echo "Updating repository..."
        git push
    else echo "Changes saved locally"
    fi
else
    echo "This directory has not been initialized with git."
	exit 1
fi


