import sys

from mysqlx import DatabaseError
sys.path.append('../')
import unittest
from unittest.mock import MagicMock, patch
from ReaderComponent import Reader
from Database import DatabaseFunctions
from Model.DataModel import Data, HistoricalValue

class TestReader(unittest.TestCase):
    
    @patch('Model.DataModel.Data')
    @patch('Database.DatabaseFunctions.ConnectDatabase')
    def test_upis(self, db_mock,test_data):
        db_mock = DatabaseFunctions.ConnectDatabase()
        self.assertEqual(Reader.WriteData(test_data,"dataset1",db_mock),None)
        
    @patch('Database.DatabaseFunctions.ConnectDatabase')
    def test_citanje_Poslednjeg(self,db_mock):
        db_mock = DatabaseFunctions.ConnectDatabase()
        self.assertEqual(Reader.ReadData("CODE_ANALOG","dataset1",db_mock),None)
        
    @patch('Model.DataModel.HistoricalValue')
    @patch('Database.DatabaseFunctions.ConnectDatabase')
    def test_citanje_Po_Istoriji(self,db_mock,HC):
        db_mock = DatabaseFunctions.ConnectDatabase()
        self.assertEqual(Reader.ReadHistory(HC,"dataset1",db_mock),[])
        
    @patch('Model.DataModel.Data')
    @patch('Database.DatabaseFunctions.ConnectDatabase')
    def test_Deadbend(self,db_mock,test_data):
        db_mock = DatabaseFunctions.ConnectDatabase()
        self.assertEqual(Reader.CalculateDifference(test_data,"dataset1",db_mock),True or False)
        self.assertEqual(Reader.CalculateDifference(None,"dataset1",db_mock),-1)
        self.assertEqual(Reader.CalculateDifference(Data(1,"CODE_DIGITAL"),"dataset1",db_mock),True or False)

        
        
     
if __name__ == '__main__':
    unittest.main()