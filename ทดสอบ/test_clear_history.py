import unittest
from unittest.mock import MagicMock, patch
from series_manager.jobs.store import delete_jobs_by_status, TERMINAL_STATUSES

class TestClearHistory(unittest.TestCase):
    @patch('series_manager.jobs.store.get_db')
    def test_delete_jobs_by_status_success(self, mock_get_db):
        mock_db = MagicMock()
        mock_get_db.return_value = mock_db
        
        for status in TERMINAL_STATUSES:
            result = delete_jobs_by_status(status)
            self.assertTrue(result)
            mock_db.tasks.delete_many.assert_called_with({"status": status})

    @patch('series_manager.jobs.store.get_db')
    def test_delete_jobs_by_status_invalid(self, mock_get_db):
        result = delete_jobs_by_status("invalid")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
