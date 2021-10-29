# Django Rest Reference Archictecture

## In development
Make sure you have both docker and docker-compose installed on your machine.

```
$ docker-compose up --build
```

> When running the project for the first time you need to use the param **--build** after it unless you change a python dependency you don't will need it anymore.

---

## Accessing shell to run python manage.py and others commands

If you need to access the shell of the python container thats is running the django application just run:

```
$ docker-compose exec django bash
```

Then you'l be able to, for example, run:


```
$ python manage.py makemigrations
$ python manage.py migrate
...

$ python manage.py loaddata project/fixtures/*.json
...

$ django-admin startapp animals
$ django-admin startapp cars
$ django-admin startapp foos
$ django-admin startapp bars
...
```
---

## Generating a new Secret Key for Django
## **How to do it:**
### **1. Generating the new Secret Key**
To generate the secret key you can do it running a simple shell command in a python enviroment with django installed(like in this project).

Basically you can follow this article to do it:
https://humberto.io/pt-br/blog/tldr-gerando-secret-key-para-o-django/

Is super simple and there is a bunch of content out there in the web if this article goes down.

### **2. Setting the new Secret Key on settings.py file**

Now that you have a secret keys in your hands you just need to open the django settings file located inside the **django/project/settings.py** the look for the **SECRET_KEY** the update it to your secret key.

### Why do I need to do it?
We also highly recommend to generate new secret keys for each project you create using this reference architecture for security reasons. It will not break anything living as it is, but given the arq-ref repository is public for anyone in the internal organization and in case of a malicious unintended access someone can try to use it as a tool to do bad stuff.

It will only take a few minutes of work but can prevent a lot of trouble in the future, so like vacines, just do it!
