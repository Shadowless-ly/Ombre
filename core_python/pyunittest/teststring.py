import unittest
import time

class TestStringMethods(unittest.TestCase):
    
    def setUp(self):
        print('set up')

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)
    
def main():
    unittest.main()

if __name__ == '__main__':
    main()