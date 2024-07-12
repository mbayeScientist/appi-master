"""
simpleTest django TDD
"""
from app import calc
from django.test import SimpleTestCase
class Test_maker(SimpleTestCase):
    "tester le calcucl"
    def test_add_number(self):
        res=calc.add(3,8)
        self.assertEqual(res,11)
        

        