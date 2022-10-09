from unittest.mock import patch, MagicMock
from what_is_year_now import what_is_year_now
import unittest


class TestWhatIsYearNow(unittest.TestCase):
    def test_ymd(self):
        with patch('what_is_year_now.urllib.request') as requests_mock, patch('what_is_year_now.json') as json_mock:
            requests_mock.urlopen.return_value = MagicMock()
            json_mock.load.return_value = {'currentDateTime': '2019-03-01'}
            self.assertEqual(what_is_year_now(), 2019)

    def test_dmy(self):
        with patch('what_is_year_now.urllib.request') as requests_mock, patch('what_is_year_now.json') as json_mock:
            requests_mock.urlopen.return_value = MagicMock()
            json_mock.load.return_value = {'currentDateTime': '01.03.2019'}
            self.assertEqual(what_is_year_now(), 2019)

    def test_fails(self):
        with patch('what_is_year_now.urllib.request') as requests_mock, patch('what_is_year_now.json') as json_mock:
            requests_mock.urlopen.return_value = MagicMock()
            json_mock.load.return_value = {'currentDateTime': '01-03-2019'}
            with self.assertRaises(Exception):
                what_is_year_now()