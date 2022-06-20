import sys
sys.path.append('../')
import unittest
from unittest import mock
from ReaderComponent import Reader

class TestReader(unittest.TestCase):

    @mock.patch('ReaderComponent.Reader',return_value=1)
    @mock.patch('ReaderComponent.Reader.Reader')
    @mock.patch('Model.DataModel.Data')
    def test_Adding(self,data,database,reader):
        self.assertEqual(Reader.WriteData(data,database),1)
        self.assertEqual(Reader.WriteData("",database),-1)
        


    @mock.patch('ReaderComponent.Reader.ReadData', return_value=1)
    @mock.patch('ReaderComponent.Reader.Reader')
    def test_Reading(self,database,readData):
        self.assertEqual(Reader.ReadData("CODE_ANALOG",database),1)
        
            

    @mock.patch('ReaderComponent.Reader.ReadHistory',return_value=1)  
    @mock.patch('ReaderComponent.Reader.Reader')
    @mock.patch('Model.DataModel.HistoricalValue')
    def test_ReadingHistorical(self,HistoricalValue,database,readHistory):
        self.assertEqual(Reader.ReadHistory(HistoricalValue,database),1)
        
 
         
    @mock.patch('ReaderComponent.Reader.CalculateDifference',return_value=1)
    @mock.patch('ReaderComponent.Reader.Reader')
    @mock.patch('Model.DataModel.Data')
    def test_CalcualtingDifference(self,data,database,calculateDifference):
        self.assertEqual(Reader.CalculateDifference(data,database),1)
        
     
if __name__ == '__main__':
    unittest.main()