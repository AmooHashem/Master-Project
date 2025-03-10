import datetime


class PaymentProcessor:
    def __init__(self, config):
        # 'config' holds API endpoints and keys for external services
        self.config = config

    def process_payment(self, payment_type, amount, currency, customer_info, payment_details):
        """
        Processes a payment by validating input and delegating processing based on payment type.
        This method handles multiple responsibilities and has high coupling.
        """
        # Validate payment details
        if not self.validate_payment(payment_type, amount, currency, customer_info, payment_details):
            return {"status": "failed", "message": "Validation error"}

        # Process payment based on type using a large if-elif block
        if payment_type == "credit_card":
            result = self.process_credit_card(
                amount, currency, customer_info, payment_details)
        elif payment_type == "digital_wallet":
            result = self.process_digital_wallet(
                amount, currency, customer_info, payment_details)
        elif payment_type == "bank_transfer":
            result = self.process_bank_transfer(
                amount, currency, customer_info, payment_details)
        else:
            return {"status": "failed", "message": "Unknown payment type"}

        # Log transaction (duplicated logging logic)
        self.log_transaction(payment_type, amount, currency,
                             customer_info, payment_details, result)
        return result

    def validate_payment(self, payment_type, amount, currency, customer_info, payment_details):
        """
        Performs basic validation on the payment data.
        Violates the Single Responsibility Principle by mixing different validations.
        """
        if amount <= 0:
            return False
        if currency not in ["USD", "EUR", "GBP"]:
            return False
        if not customer_info.get("email"):
            return False

        # Payment type-specific validations
        if payment_type == "credit_card":
            if len(payment_details.get("card_number", "")) < 12:
                return False
        elif payment_type == "digital_wallet":
            if not payment_details.get("wallet_id"):
                return False
        elif payment_type == "bank_transfer":
            if not payment_details.get("account_number"):
                return False

        return True

    def process_credit_card(self, amount, currency, customer_info, payment_details):
        """
        Simulates processing a credit card payment.
        This method includes both API integration and business logic.
        """
        print("Connecting to Credit Card API at",
              self.config.get("credit_card_endpoint"))
        transaction_id = "CC" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        print("Processing credit card payment for", customer_info.get("name"))
        return {"status": "success", "transaction_id": transaction_id}

    def process_digital_wallet(self, amount, currency, customer_info, payment_details):
        """
        Simulates processing a digital wallet payment.
        """
        print("Connecting to Digital Wallet API at",
              self.config.get("digital_wallet_endpoint"))
        transaction_id = "DW" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        print("Processing digital wallet payment for", customer_info.get("name"))
        return {"status": "success", "transaction_id": transaction_id}

    def process_bank_transfer(self, amount, currency, customer_info, payment_details):
        """
        Simulates processing a bank transfer.
        """
        print("Connecting to Bank Transfer API at",
              self.config.get("bank_transfer_endpoint"))
        transaction_id = "BT" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        print("Processing bank transfer payment for", customer_info.get("name"))
        return {"status": "success", "transaction_id": transaction_id}

    def log_transaction(self, payment_type, amount, currency, customer_info, payment_details, result):
        """
        Logs the transaction details.
        In a better design, logging would be handled by a separate logging component.
        """
        log_entry = (f"{datetime.datetime.now()} - {payment_type} payment of {amount} {currency} "
                     f"for {customer_info.get('name')}: {result}")
        print("LOG:", log_entry)


# Example usage (for testing purposes)
if __name__ == "__main__":
    config = {
        "credit_card_endpoint": "https://api.creditcard.com/process",
        "digital_wallet_endpoint": "https://api.digitalwallet.com/process",
        "bank_transfer_endpoint": "https://api.banktransfer.com/process"
    }
    processor = PaymentProcessor(config)
    customer = {"name": "John Doe", "email": "john@example.com"}
    # Example credit card details (for illustration)
    payment_details = {"card_number": "123456789012",
                       "expiry": "12/25", "cvv": "123"}
    result = processor.process_payment(
        "credit_card", 100, "USD", customer, payment_details)
    print("Final Result:", result)
