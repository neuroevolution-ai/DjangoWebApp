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
Bevor die App ausgeführt werden kann, muss der Secret Key für Django über eine Umgebungsvariable gesetzt werden. Dieser darf nicht leer sein.
```
export SECRET_KEY=${SECRET_KEY}
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Job Queue füllen:
```
python manage.py filljobqueue
```

## Jobs ausführen:
Bevor die Jobs ausgeführt werden können, müssen zwei Umgebungsvariablen erstellt werden. Die erste sollte auf python3 in der venv, die von NeuroEvolution-CTRNN_new benutzt wird (unter Linux: venv/bin/python3) gesetzt werden, die zweite auf train.py.
```
export NEURO_EVOLUTION_PYTHON=${PATH_TO_PYTHON}
export TRAINING=${PATH_TO_TRAIN.PY}
python manage.py executejobs
```
