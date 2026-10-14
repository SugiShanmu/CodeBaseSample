import sqlite3

class PaymentService:
    def get_user_payments(self, user_id):
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM payments WHERE user_id=?", (user_id,))
        data = cursor.fetchall()
        # BUG: conn, cursor never closed - RESOURCE_LEAK
        return data

    def read_config(self):
        f = open('payment_config.json')
        config = f.read()
        # BUG: file not closed
        return config