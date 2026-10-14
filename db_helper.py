# Shared DB helper - will show impact
import sqlite3

def get_connection():
    conn = sqlite3.connect('bank.db')
    return conn  # Caller must close - pattern causes leaks everywhere