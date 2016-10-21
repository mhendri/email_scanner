# Email Scanner
## Scans outgoing emails for sensitive information

Set Up

```
$ sudo pip install virtualenv
$ virtualenv env
$ cd env
$ source bin/activate
(env) $ git clone https://github.com/johnplaydrums/email_scanner
(env) $ cd email_scanner
(env) $ sudo pip install -r requirements.txt
(env) $ python manage.py makemigrations
(env) $ python manage.py migrate
(env) $ python manage.py runserver
(env) $ python manage.py createsuperuser
```

#Admin Login
http://localhost:8000/admin/

username: cyqlo
password: cyqlo123
