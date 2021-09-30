from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
import datetime as dt

# Create your tests here.
class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.Kahawa = neighbourhood(neighbourhood='bometcentral')

    def test_instance(self):
        self.assertTrue(isinstance(self.bometcentral,neighbourhood))

    def tearDown(self):
        neighbourhood.objects.all().delete()

    def test_save_method(self):
        self.bometcentral.save_neighbourhood()
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete_method(self):
        self.bometcentral.delete_neighbourhood('bometcentral')
        hood = Neighbourhood.objects.all()
        self.assertTrue(len(hood)==0)

class HealthservicesTestClass(TestCase):
    def setUp(self):
        self.Radiotherapy = healthservices(healthservices='Radiotherapy')

    def test_instance(self):
        self.assertTrue(isinstance(self.Radiotherapy,healthservices))

    def tearDown(self):
        Healthservices.objects.all().delete()

    def test_save_method(self):
        self.Radiotherapy.save_healthservices()
        health = Healthservices.objects.all()
        self.assertTrue(len(health)>0)

    def test_delete_method(self):
        self.Radiotherapy.delete_healthservices('Radiotherapy')
        health = Healthservices.objects.all()
        self.assertTrue(len(health)==0)
