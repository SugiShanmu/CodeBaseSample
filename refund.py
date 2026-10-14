class RefundService:
    def refund_payment(self, payment, reason_obj):
        # BUG: payment can be None
        if payment.status == "PAID":
            # BUG: reason_obj can be None
            log_msg = reason_obj.get_message()
            print(f"Refunding {payment.id}: {log_msg}")
            
            # BUG: DB connection leak
            import sqlite3
            conn = sqlite3.connect('bank.db')
            conn.execute("UPDATE payments SET status='REFUNDED' WHERE id=?", (payment.id,))
            conn.commit()
            # Missing conn.close()
            return True
        return False

    def get_refund_history(self, user):
        # BUG: user.refund_account can be null
        history = user.refund_account.history
        return history