import unittest
from unittest.mock import Mock
from unittest.mock import patch
from DataModel import Reader

testreader = Reader()
con = testreader.Connect()

class TestDataModel(unittest.TestCase):
    def test_Connect(self):
        self.assertEqual()

