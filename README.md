# DjangoWebApp

## Virtuelle Umgebung erstellen & aktivieren:
```
python -m venv venv
```
Zum Aktivieren der virtuellen Umgebung unter Windows:
```
venv\Scripts\activate
```
Unter Linux:
```
source venv/bin/activate
```

Siehe auch: https://docs.python.org/3/tutorial/venv.html

## Requirements installieren:
```
pip install -r requirements.txt
```

## App starten:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Job Queue füllen:
```
python manage.py filljobqueue
```

## Jobs ausführen:
```
python manage.py executejobs
```
