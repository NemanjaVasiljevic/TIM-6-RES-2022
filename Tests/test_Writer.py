import socket
import sys
sys.path.append('../')
import unittest
from unittest.mock import patch,MagicMock
from unittest import mock
from WriterComponent import Writer

class TestWriter(unittest.TestCase):
    
    @patch('WriterComponent.Writer.socket')
    def test_sending_response(self, mock_socket_s):
        mock_socket = MagicMock(socket.socket)
        mock_socket_s.return_value = mock_socket

        self.assertEqual(None, Writer.SendData(mock_socket_s))
        
if __name__ == '__main__':
    unittest.main()