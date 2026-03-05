# test_aivault.py
"""
Tests for AIVault module.
"""

import unittest
from aivault import AIVault

class TestAIVault(unittest.TestCase):
    """Test cases for AIVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AIVault()
        self.assertIsInstance(instance, AIVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AIVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
