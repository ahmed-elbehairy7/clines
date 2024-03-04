# clines

## A program for counting number of lines of code in projects

## Table of contents: 
- [setup](#setup)
- [running](#running)
    - [file_path](#file_path)
    - [-i, --ignore regex](#i---ignore-regex)
    - [-v, --verbose](#v---verbose)

## setup

There's no much rare packages here, it's just argparse in the requirements.txt file. You can install with the following command if you have pip installed on your machine

    pip install -r requirements.txt

## Running

### file_path

The application needs one required path which is file_path. This don't have to be a file, it can be a directory also and the program will count lines in all files in the directory

### -i, --ignore regex

I don't know about you but I don't want the app to spend the whole day counting code lines in node_modules. So, there's an option to ignore some files by typing a regex like *.lnk to ignore shortcuts. 

you can open main.py and see hardcoded extensions and folders there, and whatever you type in will be appended to them. If you want to remove one of them, i'm sorry for this awful user experience but you have to edit them manually from the main file itself.

So, a command example using it will be like

    ./main.py project -i node_modules -i useless -i .*

### -v, --verbose

You're probably asking, what could go wrong with a program that just count some lines? Well, so sometimes when I use the app it throws errors because the encoding of the file is not utf-8. So, in order to know which folder/file cause the problem, I add this argument to inform you which file the application will do right now

    python main.py -v

