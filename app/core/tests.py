from django.test import TestCase
from app.wsgi import *
from core.models import Persons, Inmueble

Query = Inmueble.objects.all()
print(Query)
