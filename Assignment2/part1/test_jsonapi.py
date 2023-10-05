import unittest
from jsonapi import dumps, loads

class TestJSONAPI(unittest.TestCase):

    # Test encoding and decoding complex numbers
    def test_complex(self):
        complex_obj = complex(2, 3)
        json_str = dumps({"number": complex_obj})
        decoded_obj = loads(json_str)

        self.assertIsInstance(decoded_obj, dict)
        self.assertIn("number", decoded_obj)
        self.assertIsInstance(decoded_obj["number"], complex)
        self.assertEqual(decoded_obj["number"], complex_obj)

    # Test encoding and decoding range objects using the default behavior
    # Note: The default encoder/decoder will not handle range objects
    # We're testing the expected behavior based on the provided jsonapi.py implementation
    def test_range(self):
        range_obj = range(5)
        with self.assertRaises(TypeError):
            json_str = dumps({"range": range_obj})

    # Test successful encoding and decoding with strings, ints, etc.
    def test_regular_objects(self):
        sample_dict = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        json_str = dumps(sample_dict)
        decoded_obj = loads(json_str)

        self.assertIsInstance(decoded_obj, dict)
        self.assertEqual(decoded_obj, sample_dict)

if __name__ == "__main__":
    unittest.main()
