import sys
sys.path.append('../')
import unittest
from unittest import mock
from Database import DatabaseFunctions


class TestDatabase(unittest.TestCase):

    def test_Adding(self):
        with mock.patch('Database.DatabaseFunctions.AddToTable', return_value = 1):
            self.assertEqual(DatabaseFunctions.AddToTable(1,"CODE_ANALOG","dataset1"),1)
            self.assertEqual(DatabaseFunctions.AddToTable(2,"CODE_DIGITAL","dataset1"),1)
            self.assertEqual(DatabaseFunctions.AddToTable(3,"CODE_CUSTOM","dataset2"),1)
            self.assertEqual(DatabaseFunctions.AddToTable(4,"CODE_LIMITSET","dataset2"),1)
            self.assertEqual(DatabaseFunctions.AddToTable(5,"CODE_SINGLENOE","dataset3"),1)
            self.assertEqual(DatabaseFunctions.AddToTable(6,"CODE_MULTIPLENODE","dataset3"),1)
            self.assertEqual(DatabaseFunctions.AddToTable(7,"CODE_CONSUMER","dataset4"),1)
            self.assertEqual(DatabaseFunctions.AddToTable(8,"CODE_SOURCE","dataset4"),1)
    
    def test_ReadingLastValue(self):
        with mock.patch('Database.DatabaseFunctions.ReadFromTable', return_value = 1):
            self.assertEqual(DatabaseFunctions.ReadFromTable("CODE_ANALOG","CODE_DIGITAL","dataset1"),1)
            self.assertEqual(DatabaseFunctions.ReadFromTable("CODE_CUSTOM","CODE_LIMITSET","dataset2"),1)
            self.assertEqual(DatabaseFunctions.ReadFromTable("CODE_SINGLENOE","CODE_MULTIPLENODE","dataset3"),1)
            self.assertEqual(DatabaseFunctions.ReadFromTable("CODE_CONSUMER","CODE_SOURCE","dataset4"),1)
           
    @mock.patch('Model.DataModel.HistoricalValue') 
    def test_ReadingHistorical(self,HistoricalValue):
        with mock.patch('Database.DatabaseFunctions.ReadHistorical',return_value=1):
            self.assertEqual(DatabaseFunctions.ReadHistorical(HistoricalValue,"dataset1"),1)
            self.assertEqual(DatabaseFunctions.ReadHistorical(HistoricalValue,"dataset2"),1)
            self.assertEqual(DatabaseFunctions.ReadHistorical(HistoricalValue,"dataset3"),1)
            self.assertEqual(DatabaseFunctions.ReadHistorical(HistoricalValue,"dataset4"),1)
            


if __name__ == '__main__':
    unittest.main()