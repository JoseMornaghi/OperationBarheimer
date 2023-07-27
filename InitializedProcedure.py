import unittest
from data import Batman

class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        batman = Batman('Barto',25)
        self.assertEqual(batman.myfunc(), "Hello my name is Barto")

if __name__ == '__main__':
    unittest.main()
