import sys
sys.path.append('../')
import unittest
from unittest import mock
from Model.DataModel import Reader

class TestReader(unittest.TestCase):

    @mock.patch('Model.DataModel.Data')
    def test_Adding(self,data):
        with mock.patch('Model.DataModel.Reader.WriteData',return_value=1):
            self.assertEqual(Reader.WriteData(data),1)


    def test_Reading(self):
        with mock.patch('Model.DataModel.Reader.ReadData', return_value=1):
            self.assertEqual(Reader.ReadData("CODE_ANALOG"),1)
            
    @mock.patch('Model.DataModel.HistoricalValue')
    def test_ReadingHistorical(self,HistoricalValue):
        with mock.patch('Model.DataModel.Reader.ReadHistory',return_value=1):
            self.assertEqual(Reader.ReadHistory(HistoricalValue),1)
         
    @mock.patch('Model.DataModel.Data')
    def test_CalcualtingDifference(self,data):
        with mock.patch('Model.DataModel.Reader.CalculateDifference',return_value=1):
            self.assertEqual(Reader.CalculateDifference(data),1)   
     
if __name__ == '__main__':
    unittest.main()