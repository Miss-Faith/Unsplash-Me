# [Unsplash Me](https://github.com/Miss-Faith/Unsplash-Me)
#### By [Faith Mwangi](https://github.com/miss-faith)
### Description
A landing page that provides users with images. A User is able to view images, search images by category, view images by location and copy a shareable link to the images.
## Site
[Unsplash Me](https://unsplashme.herokuapp.com/)
### Setup Requirements

##Developer
## Prerequisites
**Installing Python**

Make sure that you have [Python3 installed](https://realpython.com/installing-python/) on your machine.

You may check your Python version by running:

```bash
$python --version
```

Depending on your installation you might have access to Python3 interpreter either by running `python` or `python3`.

```bash
$python
```
Note that in this repository whenever you see `python` it will be assumed that it is Python **3**.

**Cloning**
Fork the repository and Git clone to your local machine. Access the file and run the program on the code editor, ubuntu, mac or windows terminal.
```bash
$git clone https://github.com/user-name/Unsplash-Me/
$cd Unsplash-Me
```

**Creating a Virtual Environment**
Inside the Unsplash Me directory create a virtual environment by running
```bash
$ pip install pip-env
```
activate the virtual environment by running
```bash
$ pipenv shell
```
**Adding dependencies**
Dependencies are listed in the requirements.txt file. To install all dependencies run the command using pip, pip3 or pipenv while in the virtual environment
```bash
(virtual) $ pipenv install -r requirements.txt
```
**Adding dependencies**
```bash
$ psql
```
```bash
>>>CREATE DATABASE gallery;
```

**Migrate data** 
To run test cases:
```bash
(virtual) $python3 manage.py makemigrations gallery
```
To perform an sql migrate use the version number provided after each make migration
```bash
(virtual) $python3 manage.py manage.py sqlmigrate gallery 0001
```
```bash
(virtual) $python3 manage.py migrate
```

**Running tests** 
To run test cases:
```bash
(virtual) $python3 manage.py test
```
**Running the app** 
To run test cases:
```bash
(virtual) $python3 manage.py runserver
```

## Technology Used
### Frameworks
* Django
* Bootstrap
* Heroku
###Languages
* Python
* CSS
* HTML
### Other resources
* [Google Fonts](https://fonts.google.com/)


## Development
### Want to contribute? Great!
To fix a bug or enhance an existing module, follow these steps:
* Fork the repo
* Create a new branch ('git checkout -b improve-feature')
* Make the appropriate changes in the files
* Add changes to reflect the changes made
* Commit your changes ('git commit -am 'Improve feature')
* Push to the branch ('git push origin improve-feature')
* Create a Pull Request
### Bug / Feature Request
If you find a bug/error, kindly open an issue [here](https://github.com/miss-faith/Unsplash-Me/issues/new)
Include your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/miss-faith/Unsplash-Me/issues/new)
Include sample queries and their corresponding results.
## To-Do
Future update to include a data base that stores information accessible when the application is closed and re-opened
## Contact information
[Faith Mwangi](https://github.com/miss-faith)

[Email](faith.mwangi@student.moringaschool.com)
## License
MIT License
Copyright (c) 2022 **Faith Mwangi**
