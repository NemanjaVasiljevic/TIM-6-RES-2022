import sys
sys.path.append('../')
import unittest
from unittest.mock import MagicMock, patch
from ReaderComponent import Reader
from Database import DatabaseFunctions
from Model.DataModel import Data

class TestDatabase(unittest.TestCase):
    
    @patch('Database.DatabaseFunctions.ConnectDatabase')
    def test_upis(self, db_mock):
        test_data = Data(1,"CODE_ANALOG")
        db_mock = DatabaseFunctions.ConnectDatabase()
        self.assertEqual(DatabaseFunctions.AddToTable(test_data.value,test_data.code,"dataset1",db_mock),None)
        
     
if __name__ == '__main__':
    unittest.main()