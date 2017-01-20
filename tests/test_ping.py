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

    def test_json_ping(self):
        tester = app.test_client(self)
        response = tester.get('/json_ping')
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        self.assertEqual(result['ping'], 'pong')
