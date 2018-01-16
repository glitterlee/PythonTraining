# PythonTraining

## Install Python Environment

### Windows

Note: For lines with multiple commands the first one is perffered, e.g. the `py -<version>`.  The other will only work if the python version you want to use is linked to the `python` command.

1. Go-to the python download page and download python 3.6
    1. https://www.python.org/downloads/
2. Run the installation tool and make sure that the pip box is checked so that pip is installed as well.  Also make sure to have it add python to your path.
3. Confirm that the python version by running one of the following commands in an Administrator PowerShell window (the output should be “Python 3.6.x”)
    1. `py -3.6 --version`
    2. `python --version`
4. Confirm that you have pip installed by running one of the following commands (the output should be `pip 9.0.1 from <path> (python 3.6)`)
    1. `py -3.6 -m pip --version`
    2. `python -m pip --version`
5. Install virtualenv from pip with one of the following commands
    1. `py -3.6 -m pip install virtualenv`
    2. `python -m pip install virtualenv`
6. Change directories to where you want to be developing your application
7. Create the virtual environment using one of the following commands
    1. `py -3.6 -m virtualenv <env_name>`
    2. `python -m virtualenv <env_name>`
8. Activate the virtual environment in your current shell from the directory you created the environment in (after activating “(env)” should appear in front of your terminal prompt)
    1. Powershell
        1. `.\<env_name>\Scripts\activate.ps1`
    2. Cmd
        1. `.\<env_name>\Scripts\activate.bat`
9. Confirm that python and pip are correctly linked
    1. Python
        1. Run `python --version`
        2. Should return `Python 3.6.x`
    2. Pip
        1. Run `pip --version`
        2. Should return `pip 9.0.1 from <path> (python 3.6)`
10. Install Django in the virtual env with the following command
    1. `pip install Django`
11. Confirm that Django is correctly installed by running the following command (should return `2.0.1` or something similar)
    1. `python -m django --version`
12. To exit from the virtual environment execute `deactivate` to re-enter the environment go to the folder that you originally created it in and execute step 8.
