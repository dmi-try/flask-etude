from flask import json
import unittest

from app import app


class BasicTestCase(unittest.TestCase):
    def test_ok(self):
        assert(1)

    def test_ping(self):
        tester = app.test_client(self)
        response = tester.get('/ping', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'pong')

    def test_ping_json(self):
        tester = app.test_client(self)
        response = tester.get('/ping_json')
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        self.assertEqual(result['ping'], 'pong')


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
