import unittest
from mycode import hello_world

class MyFirstTest(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_world(),'helloworld')