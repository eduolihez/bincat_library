"""
Token Manager for managing secure tokens using Fernet encryption.
"""
from cryptography.fernet import Fernet
import sqlite3

class TokenManager:
    def __init__(self, db_path="tokens.db"):
        self.db_path = db_path
        self._initialize_database()

    def _initialize_database(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS tokens (id INTEGER PRIMARY KEY, token TEXT UNIQUE)")
        conn.commit()
        conn.close()

    def generate_token(self, user_id):
        key = Fernet.generate_key()
        token = Fernet(key).encrypt(user_id.encode()).decode()
        self._store_token(token)
        return token

    def _store_token(self, token):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tokens (token) VALUES (?)", (token,))
        conn.commit()
        conn.close()

    def validate_token(self, token):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tokens WHERE token = ?", (token,))
        result = cursor.fetchone()
        conn.close()
        return result is not None

    def revoke_token(self, token):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tokens WHERE token = ?", (token,))
        conn.commit()
        conn.close()
