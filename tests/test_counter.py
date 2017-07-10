import unittest

from app import app


class DayCounterTestCase(unittest.TestCase):
    def test_counter_complete(self):
        tester = app.test_client(self)
        response = tester.get(
            '/days_counter?since=2010-01-01&title=text&needed=1')
        assert b'Congrat' in response.data

    def test_counter_no_since(self):
        tester = app.test_client(self)
        response = tester.get('/days_counter?title=txt&needed=1')
        assert b"Please provide 'since' parameter" in response.data

    def test_counter_no_deadline(self):
        tester = app.test_client(self)
        response = tester.get('/days_counter?since=2017-01-01&title=txt')
        assert b"Today is the" in response.data

    def test_counter_no_title(self):
        tester = app.test_client(self)
        response = tester.get('/days_counter?since=2017-01-01&needed=1')
        assert b"None" not in response.data

    def test_counter_title(self):
        tester = app.test_client(self)
        response = tester.get('/days_counter?since=2017-01-01&title=thetitle')
        assert b"thetitle" in response.data

    def test_final_date(self):
        tester = app.test_client(self)
        response = tester.get('/days_counter?since=2017-01-01&needed=2')
        assert b"Finish is on 2017-01-02" in response.data
