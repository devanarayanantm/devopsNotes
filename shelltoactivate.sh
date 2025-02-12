#!/bin/bash

venv_path="C:\Users\Administrator\devopsNotes\newenv3"

if [ ! -d $venv_path ]; then
    echo "Creating virtual environment at $venv_path"
    python -m venv "$venv_path"
else
  echo "Virtual environment already exists at $venv_path"
fi

source "$venv_path\scripts\activate"
echo "Activating"

echo "Installing packages"
# pip install flask

if [ -f requirement.txt ]; then
    pip install -r requirement.txt
else
    echo "bye"
fi


export FLASK_APP=001_webapps.py
flask run