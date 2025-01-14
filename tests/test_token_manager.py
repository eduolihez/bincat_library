"""
Unit tests for TokenManager class.
"""
import unittest
from bincat.token_manager import TokenManager

class TestTokenManager(unittest.TestCase):
    def setUp(self):
        self.manager = TokenManager(":memory:")

    def test_generate_token(self):
        token = self.manager.generate_token("user123")
        self.assertTrue(isinstance(token, str))

    def test_validate_token(self):
        token = self.manager.generate_token("user123")
        self.assertTrue(self.manager.validate_token(token))

    def test_revoke_token(self):
        token = self.manager.generate_token("user123")
        self.manager.revoke_token(token)
        self.assertFalse(self.manager.validate_token(token))

if __name__ == "__main__":
    unittest.main()
