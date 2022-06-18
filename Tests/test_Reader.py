import unittest
from unittest import mock
from Database import DatabaseFunctions


class TestReader(unittest.TestCase):

    def test_Adding(self):
        with mock.patch('Database.DatabaseFunctions.AddToTable', return_value = 1):
            self.assertEqual(DatabaseFunctions.AddToTable(1,"CODE_ANALOG","dataset1"),1)
            self.assertEqual(DatabaseFunctions.AddToTable(1,"CODE_DIGITAL","dataset1"),1)
            
    


if __name__ == '__main__':
    unittest.main()