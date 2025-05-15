import unittest
from task-3.py import Tm

class TestTuringMachine(unittest.TestCase):
    def test_valid_patterns(self):
        """Test that strings following the 0101 pattern are accepted"""
        self.assertTrue(Tm("0101"))
        self.assertTrue(Tm("00110011"))
        self.assertTrue(Tm("000111000111"))
    
    def test_invalid_patterns(self):
        """Test that strings not following the pattern are rejected"""
        self.assertFalse(Tm("001101"))
        self.assertFalse(Tm("00011100011"))
        self.assertFalse(Tm("1100110011"))
        self.assertFalse(Tm("0110"))
        self.assertFalse(Tm("00001111"))

if __name__ == '__main__':
    unittest.main()
