from unittest import TestCase
import some_functions

class TestSomeFunction(TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setting some global varivale")

    def setUp(self):
        print("Before starting test case")
    
    def test_add(self):
        self.assertEqual(some_functions.add(5,3), 8)
    
    def test_div(self):
        self.assertEqual(some_functions.div(25, 5), 5)
        # self.assertEqual(some_functions.div(25, 0), "Error")
        # self.assertRaises(ValueError, some_functions.div, 25, 0)
        with self.assertRaises(ValueError):
            some_functions.div(25, 0)

    def test_tokenize(self):
        self.assertEqual(some_functions.tokenize("A small string"), ["A", "small", "string"])
        self.assertNotEqual(some_functions.tokenize("A small string"), ["A", "Small", "String"])

    def test_load_pkl(self):
        self.assertIsInstance(some_functions.load_pkl("dcit.pkl"), dict)
        self.assertDictEqual(some_functions.load_pkl("dcit.pkl"), {"a": 12, "b": 13})

    def test_SomeFunc_add(self):
        sf = some_functions.SomeFunc("astr", "bstr")
        self.assertEqual(sf._add(), "astr : bstr")

    def testComplex_add(self):
        c1 = some_functions.Complex(4,3)
        c2 = some_functions.Complex(5,6)
        self.assertEqual(c1+c2, "9 + 9i")

    def tearDown(self):
        print("After every test case")

    @classmethod
    def tearDownClass(cls):
        print("Deleting some global varivale")

# python -m unittest test_some_function.py
