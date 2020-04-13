# ISD Livescore App

## About this project

This project is being developed for the "Information Systems Development" Course at the University of Liechtenstein. The goal is to setup and develop an application that allows tournaments to track and display the results for tournament games via an easy to use web UI. To achieve true "live" scores, this project aims to use the websocket technology to push new scores directly to the subscribed users.

This project is being developed by Marc Schlömmer and Felix Salcher

## Installation guide

This setup is going to guide you through the first time setup of this project.

Required dependencies are:

- Python 3.6

After installing python go to the directory where you want your project to be located and clone the github repository by opening your console in the desired folder and running the following command:

```
git clone https://github.com/ISD-Livescore/livescore-app.git
```

Now navigate your console into the newly created `livescore-app` folder. The next step is to create a virtual environment. To do this, we will use the `venv` package. On Windows this package comes with the python installation. On Linux you might have to run

```
sudo apt install -y python3-venv
```

To create a virtual environment you run 

```python3 -m venv <NAME OF YOUR VENV>```

The name of your virtual environment does not matter for this project. You just need to remember what it is because the next step is to activate the virtual environment. This step differs between Windows and UNIX systems:

WINDOWS
```
<NAME OF YOUR VENV>\Scripts\activate.bat
```

UNIX
```
source <NAME OF YOUR VENV>/bin/activate
```

After activating our virtual environment, the next step is to install all the required dependencies:

```
pip install -r requirements.txt
```

This commands gets all the packages that are saved in the `requirements.txt` file and installs the versions that are defined there. If at any point you add a package to the project you need to run `pip freeze > requirements.txt` to add the new dependency to the file.



## Important commands

TODO

## Project structure

TODO
