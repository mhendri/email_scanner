# Email Scanner
## Scans outgoing emails for sensitive information

Set Up

```
$ sudo pip install virtualenv
$ virtualenv env
$ cd env
$ source bin/activate
$ git clone https://github.com/johnplaydrums/email_scanner
$ cd email_scanner
$ sudo pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
$ python manage.py createsuperuser
```
