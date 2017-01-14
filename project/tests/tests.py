from django.test import TestCase

from django.utils import timezone
from .models import Naprava
# Create your tests here.

class NapravaTests(TestCase):
  def test_is_expensive(self):
    """
    is_expensive() should return True, if the price of gadget is more than ~1500+ €; 
                   False otherwise.
    """
    aG = Naprava(imeNaprave='test_1', opis='a', cena=8000, picture='null', video='null', pub_date=timezone.now())
    bG = Naprava(imeNaprave='test_2', opis='b', cena=1000, picture='null', video='null', pub_date=timezone.now())
    
    self.assertIs(aG.is_expensive(), True)
    self.assertIs(bG.is_expensive(), False)