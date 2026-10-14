from payment import PaymentService
from transaction import TransactionProcessor
import socket

class CheckoutManager:
    def __init__(self):
        self.payment_service = PaymentService()
        self.processor = TransactionProcessor(self.payment_service)

    def checkout(self, txn):
        # BUG: socket leak
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('bank.internal', 8080))
        s.send(str(txn).encode())
        
        result = self.processor.process(txn)
        # BUG: socket never closed
        return result

    def bulk_checkout(self, txn_list):
        f = open('checkout_log.txt', 'a')
        for txn in txn_list:
            self.checkout(txn)
            f.write(f"Processed {txn}\n")
        # BUG: file not closed in loop