import unittest
from task-2 import pda

class TestPDA(unittest.TestCase):
    def test_odd_length_palindrome(self):
        """Test that odd-length palindromes are accepted"""
        self.assertTrue(pda("aba"))
        self.assertTrue(pda("abcba"))
        self.assertTrue(pda("a"))
        self.assertTrue(pda("bbb"))
    
    def test_non_palindromes(self):
        """Test that non-palindromes and even-length strings are rejected"""
        self.assertFalse(pda("abba"))
        self.assertFalse(pda("abcd"))
        self.assertFalse(pda("ab"))
        self.assertFalse(pda("aabb"))

if __name__ == '__main__':
    unittest.main()
