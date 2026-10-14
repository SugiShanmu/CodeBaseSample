from payment import PaymentService

class TransactionProcessor:
    def __init__(self, payment_service):
        self.payment_service = payment_service

    def process(self, txn_obj):
        # BUG: txn_obj can be None - NULL_DEREFERENCE
        # BUG: txn_obj.account can be None - nested null
        amount = txn_obj.account.balance
        txn_obj.process()
        
        payments = self.payment_service.get_user_payments(txn_obj.user_id)
        return payments

    def validate(self, user):
        # BUG: user.profile is checked but user can be None
        if user.profile.is_verified:
            return True
        return False