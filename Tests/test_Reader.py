import pickle
import socket
import sys
from typing import Tuple
sys.path.append('../')
import unittest
import mysql.connector
from unittest.mock import MagicMock, patch
from ReaderComponent import Reader
from Database import DatabaseFunctions
from Model import DataModel
from Logger.Logger import logWriter

class TestReader(unittest.TestCase):

    @patch('Database.DatabaseFunctions.AddToTable')
    @patch('Database.DatabaseFunctions.ConnectDatabase')
    @patch('Model.DataModel.Data')
    def test_write(self, mock_add_to_table, mock_konekcija, mock_data):
        mock_add = MagicMock(DatabaseFunctions.AddToTable)
        mock_add_to_table.return_value = mock_add

        mock_kon = MagicMock(mysql.connector.connect)
        mock_konekcija.return_value = mock_kon

        mock_d = MagicMock(DataModel.Data)
        mock_data.return_value = mock_d

        self.assertEqual(Reader.WriteData(mock_data, "dataset1", mock_konekcija), None)
        
    #@patch('Model.DataModel.Data')
    def test_read_data(self):
        #mock_kon = MagicMock(mysql.connector.connect)
        #mock_konekcija.return_value = mock_kon

        baza = DatabaseFunctions.ConnectDatabase()
        data = DataModel.Data(1,"CODE_ANALOG")
        with patch('Database.DatabaseFunctions.ReadFromTable', return_value = data):
            self.assertIsInstance(Reader.ReadData("CODE_DIGITAL", "dataset1", baza), type(data))

    @patch('Database.DatabaseFunctions.ConnectDatabase')
    @patch('Model.DataModel.HistoricalValue')
    def test_read_history(self, mock_konekcija, mock_historical_value):
        mock_kon = MagicMock(mysql.connector.connect)
        mock_konekcija.return_value = mock_kon

        mock_hv = MagicMock(DataModel.HistoricalValue)
        mock_hv.code="CODE_ANALOG"
        mock_hv.fromTime ="2022-06-11 21:54:39"
        mock_hv.toTime="2022-06-17 15:39:19"
        mock_historical_value.return_value = mock_hv

        with patch('Database.DatabaseFunctions.ReadHistorical', return_value=[]):
            assert Reader.ReadHistory(mock_historical_value, "dataset1", mock_konekcija) == []


############## TEST CALCULATING DIFFERENCE #####################


    @patch('Database.DatabaseFunctions.ConnectDatabase')
    @patch('Model.DataModel.Data')
    def test_calculate_difference_1(self, mock_konekcija, mock_d):
        mock_kon = MagicMock(mysql.connector.connect)
        mock_konekcija.return_value = mock_kon

        mock_d = MagicMock(DataModel.Data)
        mock_d.code = "CODE_DIGITAL"
        mock_d.value = 1
        #new = DataModel.Data(1, "CODE_DIGITAL")
        
        self.assertEqual(Reader.CalculateDifference(mock_d, "dataset1", mock_konekcija), True)

    @patch('Database.DatabaseFunctions.ConnectDatabase')
    @patch('Model.DataModel.Data')
    def test_calculate_difference_2(self, mock_konekcija, mock_d):
        mock_kon = MagicMock(mysql.connector.connect)
        mock_konekcija.return_value = mock_kon

        mock_d = MagicMock(DataModel.Data)
        mock_d.code = "CODE_ANALOG"
        mock_d.value = 1
        #new = DataModel.Data(1, "CODE_DIGITAL")

        with patch('Database.DatabaseFunctions.ReadFromTable', return_value=None):
            assert Reader.CalculateDifference(mock_d, "dataset1", mock_konekcija) == True


############### TEST WRITE #####################################################################################################


    @patch('Database.DatabaseFunctions.ConnectDatabase')
    @patch('Logger.Logger.logWriter')
    def test_write_in_database_1(self, mock_konekcija, mock_logger):
        mock_kon = MagicMock(mysql.connector.connect)
        mock_konekcija.return_value = mock_kon
        
        mock_l = MagicMock(logWriter)
        mock_logger.return_value = mock_l

        historicalCollection = [DataModel.Data(1, "CODE_ANALOG"), DataModel.Data(2, "CODE_CUSTOM"), DataModel.Data(3, "CODE_SINGLENOE"), DataModel.Data(4, "CODE_CONSUMER"),DataModel.Data(1, "CODE_ANALOG"), DataModel.Data(2, "CODE_CUSTOM"), DataModel.Data(3, "CODE_SINGLENOE"), DataModel.Data(4, "CODE_CONSUMER"),DataModel.Data(1, "CODE_ANALOG"), DataModel.Data(2, "CODE_CUSTOM")]

        cd1 = DataModel.CollectionDescription(historicalCollection, "CODE_ANALOG")
        cd2 = DataModel.CollectionDescription(historicalCollection, "CODE_CUSTOM")
        cd3 = DataModel.CollectionDescription(historicalCollection, "CODE_SINGLENOE")
        cd4 = DataModel.CollectionDescription(historicalCollection, "CODE_CONSUMER")

        cdArray = [cd1, cd2, cd3, cd4]

        with patch('ReaderComponent.Reader.CalculateDifference', return_value=True):
            assert Reader.WriteInDatabase(cdArray, mock_konekcija) == None


    @patch('Database.DatabaseFunctions.ConnectDatabase')
    @patch('Logger.Logger.logWriter')
    def test_write_in_databas_2(self, mock_konekcija2, mock_logger2):
        mock_kon2 = MagicMock(mysql.connector.connect)
        mock_konekcija2.return_value = mock_kon2
        
        mock_l2 = MagicMock(logWriter)
        mock_logger2.return_value = mock_l2

        historicalCollection1 = [DataModel.Data(1, "CODE_ANALOG"), DataModel.Data(2, "CODE_CUSTOM"), DataModel.Data(3, "CODE_SINGLENOE"), DataModel.Data(4, "CODE_CONSUMER"),DataModel.Data(1, "CODE_ANALOG"), DataModel.Data(2, "CODE_CUSTOM"), DataModel.Data(3, "CODE_SINGLENOE"), DataModel.Data(4, "CODE_CONSUMER"),DataModel.Data(1, "CODE_ANALOG"), DataModel.Data(2, "CODE_CUSTOM")]
        

        cd11 = DataModel.CollectionDescription(historicalCollection1, "CODE_ANALOG")
        cd21 = DataModel.CollectionDescription(historicalCollection1, "CODE_CUSTOM")
        cd31 = DataModel.CollectionDescription(historicalCollection1, "CODE_SINGLENOE")
        cd41 = DataModel.CollectionDescription(historicalCollection1, "CODE_CONSUMER")

        cdArray = [cd11, cd21, cd31, cd41]

        with patch('ReaderComponent.Reader.CalculateDifference', return_value=False):
            assert Reader.WriteInDatabase(cdArray, mock_konekcija2) == None




################ TEST READ LAST VALUES ###############################################################################################


    
    @patch('Database.DatabaseFunctions.ConnectDatabase')
    def test_read_last_values_1(self, mock_konekcija):
        mock_kon = MagicMock(mysql.connector.connect)
        mock_konekcija.return_value = mock_kon

        # mock_socket = MagicMock(socket.socket)
        # mock_socket.recv = MagicMock(return_value = pickle.dumps([]))

        r = DataModel.Request("ReadRequest", DataModel.Data("CODE_ANALOG", "CODE_ANALOG"))

        with patch('ReaderComponent.Reader.ReadData', return_value= DataModel.Data(1,"CODE_ANALOG")):
            assert Reader.ReadLastValues(r, mock_konekcija) == None

    @patch('Database.DatabaseFunctions.ConnectDatabase')
    def test_read_last_values_2(self, mock_konekcija):
        mock_kon = MagicMock(mysql.connector.connect)
        mock_konekcija.return_value = mock_kon

        # mock_socket = MagicMock(socket.socket)
        # mock_socket.recv = MagicMock(return_value = pickle.dumps([]))

        r = DataModel.Request("ReadRequest", DataModel.Data("CODE_CUSTOM", "CODE_CUSTOM"))

        with patch('ReaderComponent.Reader.ReadData', return_value=DataModel.Data(1, "CODE_CUSTOM")):
            assert Reader.ReadLastValues(r, mock_konekcija) == None

    @patch('Database.DatabaseFunctions.ConnectDatabase')
    def test_read_last_values_3(self, mock_konekcija):
        mock_kon = MagicMock(mysql.connector.connect)
        mock_konekcija.return_value = mock_kon

        # mock_socket = MagicMock(socket.socket)
        # mock_socket.recv = MagicMock(return_value = pickle.dumps([]))

        r = DataModel.Request("ReadRequest", DataModel.Data("CODE_SINGLENOE", "CODE_SINGLENOE"))

        with patch('ReaderComponent.Reader.ReadData', return_value=DataModel.Data(1, "CODE_SINGLENOE")):
            assert Reader.ReadLastValues(r, mock_konekcija) == None

    @patch('Database.DatabaseFunctions.ConnectDatabase')
    def test_read_last_values_4(self, mock_konekcija):
        mock_kon = MagicMock(mysql.connector.connect)
        mock_konekcija.return_value = mock_kon

        # mock_socket = MagicMock(socket.socket)
        # mock_socket.recv = MagicMock(return_value = pickle.dumps([]))

        r = DataModel.Request("ReadRequest", DataModel.Data("CODE_CUSTOMER", "CODE_CUSTOMER"))

        with patch('ReaderComponent.Reader.ReadData', return_value=DataModel.Data(1, "CODE_CUSTOMER")):
            assert Reader.ReadLastValues(r, mock_konekcija) == None



################ TEST TIME STAMP READ ##################################################################################


    @patch('Database.DatabaseFunctions.ConnectDatabase')
    def test_read_from_table_using_timestamp_1(self, mock_konekcija):
        mock_kon = MagicMock(mysql.connector.connect)
        mock_konekcija.return_value = mock_kon

        r = DataModel.Request("HistoricalRequest", DataModel.Data(1, "CODE_ANALOG"))

        with patch('ReaderComponent.Reader.ReadHistory', return_value=[]):
            assert Reader.ReadFromTableUsingTimeStamp(r, mock_konekcija) == []

    @patch('Database.DatabaseFunctions.ConnectDatabase')
    def test_read_from_table_using_timestamp_2(self, mock_konekcija):
        mock_kon = MagicMock(mysql.connector.connect)
        mock_konekcija.return_value = mock_kon

        r = DataModel.Request("HistoricalRequest", DataModel.Data(1, "CODE_CUSTOM"))

        with patch('ReaderComponent.Reader.ReadHistory', return_value=[]):
            assert Reader.ReadFromTableUsingTimeStamp(r, mock_konekcija) == []

    @patch('Database.DatabaseFunctions.ConnectDatabase')
    def test_read_from_table_using_timestamp_3(self, mock_konekcija):
        mock_kon = MagicMock(mysql.connector.connect)
        mock_konekcija.return_value = mock_kon

        r = DataModel.Request("HistoricalRequest", DataModel.Data(1, "CODE_SINGLENOE"))

        with patch('ReaderComponent.Reader.ReadHistory', return_value=[]):
            assert Reader.ReadFromTableUsingTimeStamp(r, mock_konekcija) == []

    @patch('Database.DatabaseFunctions.ConnectDatabase')
    def test_read_from_table_using_timestamp_4(self, mock_konekcija):
        mock_kon = MagicMock(mysql.connector.connect)
        mock_konekcija.return_value = mock_kon

        r = DataModel.Request("HistoricalRequest", DataModel.Data(1, "CODE_CUSTOMER"))

        with patch('ReaderComponent.Reader.ReadHistory', return_value=[]):
            assert Reader.ReadFromTableUsingTimeStamp(r, mock_konekcija) == []



################# TEST SEND RESPONSE ##########################################################################

    @patch('ReaderComponent.Reader.socket')
    def test_sending_response(self, mock_socket_s):
        mock_socket = MagicMock(socket.socket)
        mock_socket_s.return_value = mock_socket

        self.assertEqual(None, Reader.SendResponse(""))



if __name__ == '__main__':
    unittest.main()