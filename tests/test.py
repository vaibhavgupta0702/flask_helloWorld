import unittest
from urllib.request import urlopen
from flask import Flask
from flask_testing import TestCase

class MyTest(TestCase):
    port = '8080'

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def test_server_is_up_and_running(self):
        response = urlopen('http://127.0.0.1:' + str(self.port) )
        self.assertEqual(response.code, 200)

    def test_server_is_showing_correct_output(self):
        response = urlopen('http://127.0.0.1:' + str(self.port) )
        html = str(response.read())
        output = "b'Hello World! I am running on port " + str(self.port) + "'"
        self.assertEqual(html,output)

if __name__ == '__main__':
    unittest.main()
