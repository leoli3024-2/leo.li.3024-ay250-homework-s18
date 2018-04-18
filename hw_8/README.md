# HW08 - Flask-based website framework

## Purpose:
Create a flask-based website that provides a query interface to BibTeX bibliographic data. The website must allow a user to upload a BibTeX file, store the contents of the file in a database, and provide a query interface to the database.

## Files:
* README.md
* hw_8-web-framework.pdf
* bib_server.py
* hw8test.py
  - testfile for running Travis CI & Codecov
* hw_8_data
  - homework_8_refs.bib
  - a sample database for interaction
* templates
  - Contains the front-end designs for this local app

## How to run this app/program?
Simply download, pull or fork this repository, then cd to the local directory then run the following command in your terminal.
```
python bib_server.py
```
Your may encounter errors saying "There is no module 'pybtex'" or "There is no module 'flask_sqlalchemy'". If you ever encounter such errors, install the missing modules by running the code below, and run the above command again:
```
pip install pybtes
pip install flask_sqlalchemy
```
Now your terminal should have told you where to interactive with this app. In hw_8_data, you could find a sample bibTex database for practice, named homework_8_refs.bib. Upload this file to the local webpage, and try querying. You do not need to put your query strings in quotes. Simply just enter the query string (eg. year < 1910) should work. This assignment is running with Travis CI, and Code Coverage (30.40% covered). It should be above 70%, but I could not figure out what to improve. 