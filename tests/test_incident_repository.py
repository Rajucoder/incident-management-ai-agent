from unittest.mock import patch, MagicMock
from db.incident_repository import update_priority


@patch("db.incident_repository.get_connection")
def test_update_priority(mock_get_connection):

    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    mock_conn.cursor.return_value = mock_cursor
    mock_get_connection.return_value = mock_conn

    update_priority(1, "Critical")

    mock_cursor.execute.assert_called_once()

    mock_conn.commit.assert_called_once()