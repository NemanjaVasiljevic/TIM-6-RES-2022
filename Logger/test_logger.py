from unittest.mock import Mock
import logger


def test_logWriter(self):
    mock_dogadjaj = Mock()
    mock_komponenta = Mock()
    logger.logWriter(mock_dogadjaj, mock_komponenta)
