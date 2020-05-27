# PROJECT
### Pics-World Album
![Screenshot from 2020-05-27 13-29-13](https://user-images.githubusercontent.com/58691817/83008899-98213e80-a01e-11ea-9ef4-7a2fdc1a681f.png)


## AUTHOR
### Joan Kinyua

## USER STORIES
View my photos as posted. Click on a single photo to expand it and also view the details of that specific photo.
The photo details must appear on a modal within the same route as the main page. Search for different categories
of photos. (ie. HIking, code) Copy a link to the photo to share with your friends.

## SetUp / Installation Requirements
* Clone the repo by running: ```https://github.com/Joan-w/gallery.git```
* Navigate to the project directory;
* cd Gallery-Photo
* Create a virtual environment and activate it python3 -m venv virtual . virtual/bin/activate
* Create a database using postgress, type the following commands; $psql
* Then run the command to create a new database create database gallery
* Install dependencies pip install -r requirements.txt
* Create database migrations python3 manage.py makemigrations photoz python3 manage.py migrate
* Run the app python3 manage.py runserver

## TECHNOLOGIES USED
```
Python
Django
Bootstrap
```

## License
MIT License

Copyright (c) 2020 Joan Kinyua

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
