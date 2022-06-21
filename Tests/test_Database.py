import sys
from typing import List

from mysqlx import DatabaseError
sys.path.append('../')
import unittest
from unittest import mock
from Database import DatabaseFunctions
import mysql.connector
from Model import DataModel

class TestDatabase(unittest.TestCase):
    def test_connection(self):
        with mock.patch('mysql.connector.connect', return_value=1):
            assert DatabaseFunctions.ConnectDatabase() == 1

    @mock.patch('Database.DatabaseFunctions.ConnectDatabase')
    def test_add(self, mock_konekcija):
        mock_kon = mock.MagicMock(mysql.connector.connect)
        mock_konekcija.return_value = mock_kon

        self.assertEqual(DatabaseFunctions.AddToTable(1,"CODE_ANALOG","dataset1", mock_konekcija), None)

    def test_add_error(self):
        mock_baza = mock.MagicMock()
        mock_baza.cursor.side_effect = DatabaseError

        self.assertEqual(DatabaseFunctions.AddToTable(1,"CODE_ANALOG","dataset1", mock_baza), DatabaseError)
    
    def test_read_from_table_1(self):
        db = DatabaseFunctions.ConnectDatabase()
        self.assertIsInstance(DatabaseFunctions.ReadFromTable("CODE_ANALOG", "CODE_DIGITAL", "dataset1", db), (DataModel.Data, DataModel.Data))

    def test_read_from_table_2(self):
        db = DatabaseFunctions.ConnectDatabase()
        self.assertIsInstance(DatabaseFunctions.ReadFromTable("CODE_ANALOG", "", "dataset1", db), DataModel.Data)
    
    def test_read_from_table_error(self):
        mock_baza = mock.MagicMock()
        mock_baza.cursor.side_effect = DatabaseError

        self.assertEqual(DatabaseFunctions.ReadFromTable("CODE_ANALOG", "", "dataset1", mock_baza), DatabaseError)

    @mock.patch('Model.DataModel.HistoricalValue')
    def test_read_historcal(self, mock_historical_value):
        mock_hv = mock.MagicMock(DataModel.HistoricalValue)
        mock_hv.code="CODE_ANALOG"
        mock_hv.fromTime ="2022-06-11 21:54:39"
        mock_hv.toTime="2022-06-17 15:39:19"
        mock_historical_value.return_value = mock_hv

        db = DatabaseFunctions.ConnectDatabase()
        self.assertIsInstance(DatabaseFunctions.ReadHistorical(mock_hv, "dataset1", db), List)

    '''@mock.patch('Model.DataModel.HistoricalValue')
    def test_read_historcal_error(self, mock_historical_value):
        mock_hv = mock.MagicMock(DataModel.HistoricalValue)
        mock_hv.code="CODE_ANALOG"
        mock_hv.fromTime ="2022-06-11 21:54:39"
        mock_hv.toTime="2022-06-17 15:39:19"
        mock_historical_value.return_value = mock_hv

        db = DatabaseFunctions.ConnectDatabase()
        self.assertRaises(Exception, DatabaseFunctions.ReadHistorical(mock_hv, "dataset5", db))'''

    def test_read_historcal_error(self):
        mock_baza = mock.MagicMock()
        mock_baza.cursor.side_effect = DatabaseError

        self.assertEqual(DatabaseFunctions.ReadHistorical("", "dataset1", mock_baza), DatabaseError)

if __name__ == '__main__':
    unittest.main()