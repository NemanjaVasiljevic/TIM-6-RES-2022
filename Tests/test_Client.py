import socket
import sys
sys.path.append('../')
from decimal import Decimal
from tkinter.messagebox import NO
import unittest
from unittest import mock
from WriterComponent import Client
from unittest.mock import MagicMock, Mock, patch


class TestMeni(unittest.TestCase):
    
    def test_meni_ok(self):
        with mock.patch('builtins.input', return_value="2"):
            assert Client.Menu() == '2'
            
    def test_meni_van_opsega(self):
        with mock.patch('builtins.input', return_value="23"):
            assert Client.Menu() == None
        with mock.patch('builtins.input', return_value="-12"):
            assert Client.Menu() == None

    def test_meni_nije_broj(self):
        with mock.patch('builtins.input', return_value="test"):
            assert Client.Menu() == None
        with mock.patch('builtins.input', return_value=[]):
            assert Client.Menu() == None
            
            
class TestHistorical(unittest.TestCase):
    @patch('ReaderComponent.Reader.socket')
    def test_unos_ok(self,mock_socket_s):
        mock_socket = MagicMock(socket.socket)
        mock_socket_s.return_value = mock_socket
        
        with mock.patch('builtins.input', return_value=["datum1", "datum2", "CODE_ANALOG"]):
            assert Client.SendHistoricalRequest(mock_socket) == None
            
class TestCode(unittest.TestCase):
    @patch('ReaderComponent.Reader.socket')
    def test_unos_ok(self,mock_socket_s):
        mock_socket = MagicMock(socket.socket)
        mock_socket_s.return_value = mock_socket
        
        with mock.patch('builtins.input', return_value=["kod1","kod2"]):
            assert Client.SendCodeRequest(mock_socket) == None
        
if __name__ == '__main__':
    unittest.main()