# banking_system/models.py

import threading
from dataclasses import dataclass
from pprint import pprint
from threading import Thread
from typing import Dict, Optional, List

import schedule


@dataclass
class Account:
    account_id: str
    balance: int
    created_timestamp: int
    total_outgoing: int = 0  # Track total outgoing transactions for Level 2


@dataclass
class Payment:
    payment_id: str
    account_id: str
    amount: int
    timestamp: int
    status: str  # "IN_PROGRESS" or "CASHBACK_RECEIVED"
    cashback_due_timestamp: int


class BankingSystem:
    def __init__(self):
        self.accounts: Dict[str, Account] = {}
        self.payments: Dict[str, Payment] = {}  # Track payments by payment_id
        self.payment_counter = 0
        self._lock = threading.Lock()  # Thread safety for cashback processing
        self._scheduler_thread = None
        self._scheduler_running = False
        self._start_scheduler()

        # Constants for Level 3
        self.MILLISECONDS_IN_1_DAY = 24 * 60 * 60 * 1000

    def _start_scheduler(self):
        """Start the scheduler in a separate thread"""
        if not self._scheduler_running:
            self._scheduler_running = True
            self._scheduler_thread = Thread(target=self._run_scheduler, daemon=True)
            self._scheduler_thread.start()

    def _run_scheduler(self):
        """Run the scheduler continuously"""
        while self._scheduler_running:
            schedule.run_pending()
            time.sleep(1)  # Check every second

    def _stop_scheduler(self):
        """Stop the scheduler (useful for cleanup)"""
        self._scheduler_running = False
        schedule.clear()

    def create_account(self, timestamp: int, account_id: str) -> bool:
        """
        Creates a new account with the given identifier if it doesn't already exist.

        Args:
            timestamp: Stringified timestamp in milliseconds
            account_id: Account identifier

        Returns:
            True if the account was successfully created, False if an account with account_id already exists
        """
        if account_id in self.accounts:
            return False

        account = Account(
            account_id=account_id,
            balance=0,
            created_timestamp=timestamp
        )

        self.accounts[account_id] = account
        return True

    def deposit(self, timestamp: int, account_id: str, amount: int) -> Optional[int]:
        """
        Deposits the given amount of money to the specified account after the operation has been processed.

        Args:
            timestamp: Stringified timestamp in milliseconds
            account_id: Account identifier
            amount: Amount to deposit

        Returns:
            Returns the balance of the account after the operation or None if account doesn't exist
        """
        if account_id not in self.accounts:
            return None

        # Process any pending cashbacks up to current timestamp
        self._process_pending_cashbacks(timestamp)

        account = self.accounts[account_id]
        account.balance += amount
        return account.balance

    def transfer(self, timestamp: int, source_account_id: str, target_account_id: str, amount: int) -> Optional[int]:
        """
        Transfers the given amount of money from source_account_id to target_account_id.

        Args:
            timestamp: Stringified timestamp in milliseconds
            source_account_id: Source account identifier
            target_account_id: Target account identifier
            amount: Amount to transfer

        Returns:
            Returns the balance of source_account_id if the transfer was successful or None otherwise
        """
        source_account = self.accounts.get(source_account_id)
        target_account = self.accounts.get(target_account_id)

        # Return None if source_account_id or target_account_id doesn't exist
        if source_account is None or target_account is None:
            return None

        # Return None if source_account_id and target_account_id are the same
        if source_account_id == target_account_id:
            return None

        # Return None if account source_account_id has insufficient funds to perform the transfer
        if source_account.balance < amount:
            return None

        # Perform the transfer
        source_account.balance -= amount
        target_account.balance += amount

        # Track outgoing transaction for Level 2 (but not for Level 3 pay operations)
        source_account.total_outgoing += amount

        return source_account.balance

    def get_balance(self, account_id: str) -> Optional[int]:
        """Helper method to get account balance (useful for testing)"""
        account = self.accounts.get(account_id)
        return account.balance if account else None

    def account_exists(self, account_id: str) -> bool:
        """Helper method to check if account exists (useful for testing)"""
        return account_id in self.accounts

    def top_spenders(self, timestamp: int, n: int) -> List[str]:
        """
        Returns the identifiers of the top n accounts with the highest outgoing transactions.

        Args:
            timestamp: Stringified timestamp in milliseconds
            n: Number of top spenders to return

        Returns:
            List of account identifiers sorted by total outgoing transactions (descending),
            then alphabetically by account_id in case of tie.
            Format: ["<account_id_1>(<total_outgoing_1>)", "<account_id_2>(<total_outgoing_2>)", ...]
        """
        if n <= 0:
            return []

        # Process any pending cashbacks up to current timestamp
        self._process_pending_cashbacks(timestamp)

        # If less than n accounts exist, return all accounts
        if len(self.accounts) < n:
            n = len(self.accounts)

        # top_spenders should now also account for the total amount of money withdrawn from accounts
        # Sort accounts by total_outgoing (descending), then by account_id (ascending) for ties
        sorted_accounts = sorted(
            self.accounts.values(),
            key=lambda acc: (-acc.total_outgoing, acc.account_id)
        )

        # Take top n and format as required
        top_n = sorted_accounts[:n]
        return [f"{acc.account_id}({acc.total_outgoing})" for acc in top_n]

    def pay(self, timestamp: int, account_id: str, amount: int) -> Optional[str]:
        """
        Withdraws the given amount of money from the specified account.
        Provides 2% cashback after 24 hours.

        Args:
            timestamp: Stringified timestamp in milliseconds
            account_id: Account identifier
            amount: Amount to withdraw

        Returns:
            Payment identifier string if successful, None otherwise
        """
        account = self.accounts.get(account_id)

        # Return None if account_id doesn't exist
        if account is None:
            return None

        # Return None if account has insufficient funds
        if account.balance < amount:
            return None

        # Perform withdrawal
        account.balance -= amount

        # Track outgoing for top_spenders (Level 2 requirement)
        account.total_outgoing += amount

        # Create payment record
        self.payment_counter += 1
        payment_id = f"payment{self.payment_counter}"

        cashback_due_timestamp = timestamp + self.MILLISECONDS_IN_1_DAY

        payment = Payment(
            payment_id=payment_id,
            account_id=account_id,
            amount=amount,
            timestamp=timestamp,
            status="IN_PROGRESS",
            cashback_due_timestamp=cashback_due_timestamp
        )

        self.payments[payment_id] = payment

        # Schedule cashback processing
        self._schedule_cashback(payment_id, cashback_due_timestamp)

        return payment_id

    def get_payment_status(self, timestamp: int, account_id: str, payment: str) -> Optional[str]:
        """
        Returns the status of the payment transaction for the given payment.

        Args:
            timestamp: Stringified timestamp in milliseconds
            account_id: Account identifier
            payment: Payment identifier

        Returns:
            Payment status string or None if conditions not met
        """
        # Return None if account_id doesn't exist
        if account_id not in self.accounts:
            return None

        # Return None if the given payment doesn't exist for the specified account
        if payment not in self.payments:
            return None

        payment_record = self.payments[payment]

        # Return None if the payment transaction was for an account with different identifier
        if payment_record.account_id != account_id:
            return None

        return payment_record.status

    def _schedule_cashback(self, payment_id: str, due_timestamp: int):
        """Schedule cashback processing for a payment using schedule library"""

        def process_cashback():
            with self._lock:
                if payment_id in self.payments:
                    payment = self.payments[payment_id]
                    if payment.status == "IN_PROGRESS":
                        # Calculate 2% cashback (rounded down)
                        cashback_amount = int(payment.amount * 0.02)

                        # Add cashback to account
                        account = self.accounts.get(payment.account_id)
                        if account:
                            account.balance += cashback_amount

                        # Update payment status
                        payment.status = "CASHBACK_RECEIVED"

            # Remove the job after execution
            return schedule.CancelJob

        # Convert timestamp to datetime format for scheduling
        due_time = time.localtime(due_timestamp / 1000.0)
        due_time_str = time.strftime('%H:%M:%S', due_time)

        # Schedule the job to run at the specific time
        # Note: schedule library works with daily schedules, so we need a different approach
        # For testing purposes, we'll use a simpler approach with direct time comparison

        # Create a unique job tag for this payment
        job_tag = f"cashback_{payment_id}"

        # Schedule a job that checks if it's time to process this cashback
        schedule.every(1).seconds.do(self._check_and_process_cashback, payment_id, due_timestamp).tag(job_tag)

    def _check_and_process_cashback(self, payment_id: str, due_timestamp: int):
        """Check if it's time to process cashback and do so if needed"""
        current_timestamp = int(time.time() * 1000)  # Current time in milliseconds

        if current_timestamp >= due_timestamp:
            with self._lock:
                if payment_id in self.payments:
                    payment = self.payments[payment_id]
                    if payment.status == "IN_PROGRESS":
                        # Calculate 2% cashback (rounded down)
                        cashback_amount = int(payment.amount * 0.02)

                        # Add cashback to account
                        account = self.accounts.get(payment.account_id)
                        if account:
                            account.balance += cashback_amount

                        # Update payment status
                        payment.status = "CASHBACK_RECEIVED"

            # Cancel this specific job
            schedule.clear(f"cashback_{payment_id}")
            return schedule.CancelJob

    def _process_pending_cashbacks(self, current_timestamp: int):
        """Process any pending cashbacks that are due (used for testing)"""
        with self._lock:
            for payment in self.payments.values():
                if (payment.status == "IN_PROGRESS" and
                        current_timestamp >= payment.cashback_due_timestamp):

                    # Calculate 2% cashback (rounded down)
                    cashback_amount = int(payment.amount * 0.02)

                    # Add cashback to account
                    account = self.accounts.get(payment.account_id)
                    if account:
                        account.balance += cashback_amount

                    # Update payment status
                    payment.status = "CASHBACK_RECEIVED"


class TestBankingSystem:

    def setup_method(self):
        self.banking_system = BankingSystem()

    def test_create_account(self):
        # Test creating a new account
        assert self.banking_system.create_account(1, "account1") is True
        assert self.banking_system.account_exists("account1") is True

        # Test creating account that already exists
        assert self.banking_system.create_account(2, "account1") is False

        # Test creating another account
        assert self.banking_system.create_account(3, "account2") is True
        assert self.banking_system.account_exists("account2") is True

    def test_deposit(self):
        # Test deposit to non-existing account
        assert self.banking_system.deposit(4, "non-existing", 2700) is None

        # Create account and test deposit
        self.banking_system.create_account(1, "account1")
        assert self.banking_system.deposit(5, "account1", 2700) == 2700
        assert self.banking_system.get_balance("account1") == 2700

    def test_transfer(self):
        # Create accounts
        self.banking_system.create_account(1, "account1")
        self.banking_system.create_account(2, "account2")

        # Add some money to account1
        self.banking_system.deposit(3, "account1", 3000)

        # Test transfer with insufficient funds (3000 < 3001)
        assert self.banking_system.transfer(6, "account1", "account2", 3001) is None

        # Test successful transfer
        assert self.banking_system.transfer(7, "account1", "account2", 500) == 2500
        assert self.banking_system.get_balance("account1") == 2500
        assert self.banking_system.get_balance("account2") == 500

        # Test transfer to non-existing account
        assert self.banking_system.transfer(8, "account1", "non-existing", 100) is None

        # Test transfer from non-existing account
        assert self.banking_system.transfer(9, "non-existing", "account1", 100) is None

        # Test transfer to same account
        assert self.banking_system.transfer(10, "account1", "account1", 100) is None

    def test_top_spenders(self):
        # Create accounts
        self.banking_system.create_account(1, "account3")
        self.banking_system.create_account(2, "account2")
        self.banking_system.create_account(3, "account1")

        # Add money to accounts
        self.banking_system.deposit(4, "account1", 2000)
        self.banking_system.deposit(5, "account2", 3000)
        self.banking_system.deposit(6, "account3", 4000)

        # Test with no outgoing transactions
        assert self.banking_system.top_spenders(7, 3) == ["account1(0)", "account2(0)", "account3(0)"]

        # Make some transfers
        self.banking_system.transfer(8, "account3", "account2", 500)  # account3 total: 500
        self.banking_system.transfer(9, "account3", "account1", 1000)  # account3 total: 1500
        self.banking_system.transfer(10, "account1", "account2", 2500)  # account1 total: 2500

        # Test top spenders
        assert self.banking_system.top_spenders(11, 3) == ["account1(2500)", "account3(1500)", "account2(0)"]

    def test_pay_and_cashback(self):
        # Create account and add money
        self.banking_system.create_account(1, "account1")
        self.banking_system.deposit(2, "account1", 2000)

        # Test pay operation
        payment1 = self.banking_system.pay(4, "account1", 1000)
        assert payment1 == "payment1"
        assert self.banking_system.get_balance("account1") == 1000

        # Test payment status
        assert self.banking_system.get_payment_status(5, "account1", "payment1") == "IN_PROGRESS"

        # Test pay to non-existing account
        assert self.banking_system.pay(6, "non-existing", 100) is None

        # Test pay with insufficient funds
        assert self.banking_system.pay(7, "account1", 2000) is None

        # Test get_payment_status edge cases
        assert self.banking_system.get_payment_status(8, "non-existing", "payment1") is None
        assert self.banking_system.get_payment_status(9, "account1", "non-existing") is None

        # Create second account to test different account access
        self.banking_system.create_account(10, "account2")
        assert self.banking_system.get_payment_status(11, "account2", "payment1") is None

        # Test cashback processing (simulate time passing)
        MILLISECONDS_IN_1_DAY = 24 * 60 * 60 * 1000
        self.banking_system._process_pending_cashbacks(4 + MILLISECONDS_IN_1_DAY)

        # Check cashback received
        assert self.banking_system.get_payment_status(12, "account1", "payment1") == "CASHBACK_RECEIVED"
        # Balance should be 1000 + (1000 * 0.02 = 20) = 1020
        assert self.banking_system.get_balance("account1") == 1020

        # Test multiple payments
        payment2 = self.banking_system.pay(100, "account1", 1000)
        assert payment2 == "payment2"
        assert self.banking_system.get_balance("account1") == 20

        # Test top_spenders includes withdrawn amounts
        assert self.banking_system.top_spenders(104, 2) == ["account1(2000)", "account2(0)"]

    def test_example_scenario(self):
        # Following the example from the requirements
        assert self.banking_system.create_account(1, "account1") is True
        assert self.banking_system.create_account(2, "account1") is False  # this account already exists
        assert self.banking_system.create_account(3, "account2") is True
        assert self.banking_system.deposit(4, "non-existing", 2700) is None
        assert self.banking_system.deposit(5, "account1", 2700) == 2700
        assert self.banking_system.transfer(6, "account1", "account2", 2701) is None  # insufficient funds (2700 < 2701)
        assert self.banking_system.transfer(7, "account1", "account2", 200) == 2500

        # Test Level 2 functionality
        assert self.banking_system.top_spenders(8, 2) == ["account1(200)", "account2(0)"]

        # Test Level 3 functionality
        payment1 = self.banking_system.pay(9, "account1", 100)
        assert payment1 == "payment1"
        assert self.banking_system.get_payment_status(10, "account1", "payment1") == "IN_PROGRESS"

    def sort_by_acc_number(self, items):
        """
        Sort a list of strings in ascending order based on the number between "acc" and "(".

        Args:
            items (list): List of strings in format "acc{number}({value})"

        Returns:
            list: Sorted list in ascending order by account number
        """

        def extract_acc_number(item):
            # Find the position after "acc"
            start = item.find("acc") + 3
            # Find the position of "("
            end = item.find("(")
            # Extract and convert to integer
            return int(item[start:end])

        return sorted(items, key=extract_acc_number)

    def test_level_3_case_10(self):
        # Create multiple accounts
        assert self.banking_system.create_account(1, 'acc1') is True
        assert self.banking_system.create_account(2, 'acc2') is True
        assert self.banking_system.create_account(3, 'acc3') is True
        assert self.banking_system.create_account(4, 'acc4') is True
        assert self.banking_system.create_account(5, 'acc5') is True
        assert self.banking_system.create_account(6, 'acc6') is True
        assert self.banking_system.create_account(7, 'acc7') is True
        assert self.banking_system.create_account(8, 'acc8') is True
        assert self.banking_system.create_account(9, 'acc9') is True
        assert self.banking_system.create_account(10, 'acc10') is True

        # Deposit to non-existing account
        assert self.banking_system.deposit(11, 'acc0', 6255) is None

        # Deposit to existing accounts
        assert self.banking_system.deposit(12, 'acc1', 6460) == 6460
        assert self.banking_system.deposit(13, 'acc2', 6555) == 6555
        assert self.banking_system.deposit(14, 'acc3', 6648) == 6648
        assert self.banking_system.deposit(15, 'acc4', 7372) == 7372
        assert self.banking_system.deposit(16, 'acc5', 5964) == 5964
        assert self.banking_system.deposit(17, 'acc6', 6559) == 6559
        assert self.banking_system.deposit(18, 'acc7', 8653) == 8653
        assert self.banking_system.deposit(19, 'acc8', 8284) == 8284
        assert self.banking_system.deposit(20, 'acc9', 8832) == 8832

        # Make payments
        assert self.banking_system.pay(21, 'acc1', 134) == 'payment1'
        assert self.banking_system.pay(22, 'acc2', 493) == 'payment2'
        assert self.banking_system.pay(23, 'acc3', 493) == 'payment3'
        assert self.banking_system.pay(24, 'acc4', 256) == 'payment4'
        assert self.banking_system.pay(25, 'acc5', 425) == 'payment5'
        assert self.banking_system.pay(26, 'acc6', 373) == 'payment6'
        assert self.banking_system.pay(27, 'acc7', 158) == 'payment7'
        assert self.banking_system.pay(28, 'acc8', 211) == 'payment8'
        assert self.banking_system.pay(29, 'acc9', 469) == 'payment9'

        # Try to pay from non-existing account
        assert self.banking_system.pay(30, 'acc10', 205) is None
        time.sleep(1)

        # Check payment statuses before cashback
        assert self.banking_system.get_payment_status(31, 'acc1', 'payment1') == 'IN_PROGRESS'
        assert self.banking_system.get_payment_status(32, 'acc2', 'payment2') == 'IN_PROGRESS'
        assert self.banking_system.get_payment_status(33, 'acc3', 'payment3') == 'IN_PROGRESS'
        assert self.banking_system.get_payment_status(34, 'acc4', 'payment4') == 'IN_PROGRESS'
        assert self.banking_system.get_payment_status(35, 'acc5', 'payment5') == 'IN_PROGRESS'
        assert self.banking_system.get_payment_status(36, 'acc6', 'payment6') == 'IN_PROGRESS'
        assert self.banking_system.get_payment_status(37, 'acc7', 'payment7') == 'IN_PROGRESS'
        assert self.banking_system.get_payment_status(38, 'acc8', 'payment8') == 'IN_PROGRESS'
        assert self.banking_system.get_payment_status(39, 'acc9', 'payment9') == 'IN_PROGRESS'

        # Try to get payment status from non-existing account
        assert self.banking_system.get_payment_status(40, 'acc10', 'payment10') is None

        # Check top spenders before cashback
        expected = ['acc1(134)', 'acc2(493)', 'acc3(493)', 'acc4(256)', 'acc5(425)', 'acc6(373)',
                    'acc7(158)', 'acc8(211)', 'acc9(469)', 'acc10(0)']
        assert set(self.banking_system.top_spenders(41, 10)) == set(expected)

        # Test deposit after cashback time (86400000 milliseconds = 24 hours)
        assert self.banking_system.deposit(86400022, 'acc1', 313) == 6641  # 6460 - 134 + 2 (cashback) + 313
        assert self.banking_system.deposit(86400023, 'acc2', 590) == 6561  # 6555 - 493 + 9 (cashback) + 590
        assert self.banking_system.deposit(86400024, 'acc3', 213) == 6377  # 6648 - 493 + 9 (cashback) + 213
        assert self.banking_system.deposit(86400025, 'acc4', 519) == 7648  # 7372 - 256 + 5 (cashback) + 519
        assert self.banking_system.deposit(86400026, 'acc5', 290) == 5843  # 5964 - 425 + 8 (cashback) + 290
        assert self.banking_system.deposit(86400027, 'acc6', 447) == 6640  # 6559 - 373 + 7 (cashback) + 447
        assert self.banking_system.deposit(86400028, 'acc7', 875) == 9373  # 8653 - 158 + 3 (cashback) + 875
        assert self.banking_system.deposit(86400029, 'acc8', 485) == 8562  # 8284 - 211 + 4 (cashback) + 485
        assert self.banking_system.deposit(86400030, 'acc9', 90) == 8478  # 8832 - 469 + 9 (cashback) + 90

        # Check payment statuses after cashback
        assert self.banking_system.get_payment_status(86400031, 'acc1', 'payment1') == 'CASHBACK_RECEIVED'
        assert self.banking_system.get_payment_status(86400032, 'acc2', 'payment2') == 'CASHBACK_RECEIVED'
        assert self.banking_system.get_payment_status(86400033, 'acc3', 'payment3') == 'CASHBACK_RECEIVED'
        assert self.banking_system.get_payment_status(86400034, 'acc4', 'payment4') == 'CASHBACK_RECEIVED'
        assert self.banking_system.get_payment_status(86400035, 'acc5', 'payment5') == 'CASHBACK_RECEIVED'
        assert self.banking_system.get_payment_status(86400036, 'acc6', 'payment6') == 'CASHBACK_RECEIVED'
        assert self.banking_system.get_payment_status(86400037, 'acc7', 'payment7') == 'CASHBACK_RECEIVED'
        assert self.banking_system.get_payment_status(86400038, 'acc8', 'payment8') == 'CASHBACK_RECEIVED'
        assert self.banking_system.get_payment_status(86400039, 'acc9', 'payment9') == 'CASHBACK_RECEIVED'

        # Try to get payment status from non-existing account
        assert self.banking_system.get_payment_status(86400040, 'acc10', 'payment10') is None

        # Make additional payments
        assert self.banking_system.pay(86400041, 'acc1', 286) == 'payment10'
        assert self.banking_system.pay(86400042, 'acc2', 365) == 'payment11'
        assert self.banking_system.pay(86400043, 'acc3', 225) == 'payment12'
        assert self.banking_system.pay(86400044, 'acc4', 483) == 'payment13'
        assert self.banking_system.pay(86400045, 'acc5', 194) == 'payment14'
        assert self.banking_system.pay(86400046, 'acc6', 386) == 'payment15'
        assert self.banking_system.pay(86400047, 'acc7', 392) == 'payment16'
        assert self.banking_system.pay(86400048, 'acc8', 290) == 'payment17'
        assert self.banking_system.pay(86400049, 'acc9', 249) == 'payment18'

        # Try to pay from account with insufficient funds
        assert self.banking_system.pay(86400050, 'acc10', 177) is None
        time.sleep(1)

        # Check final top spenders
        expected = ['acc2(858)', 'acc6(759)', 'acc4(739)', 'acc3(718)', 'acc9(718)', 'acc5(619)', 'acc7(550)',
                    'acc8(501)', 'acc1(420)', 'acc10(0)']
        assert set(self.banking_system.top_spenders(86400051, 10)) == set(expected)

        # Check payment statuses for new payments
        assert self.banking_system.get_payment_status(172800036, 'acc1', 'payment10') == 'IN_PROGRESS'
        assert self.banking_system.get_payment_status(172800037, 'acc8', 'payment17') == 'IN_PROGRESS'
        assert self.banking_system.get_payment_status(172800038, 'acc7', 'payment16') == 'IN_PROGRESS'
        assert self.banking_system.get_payment_status(172800039, 'acc6', 'payment15') == 'IN_PROGRESS'
        assert self.banking_system.get_payment_status(172800040, 'acc5', 'payment14') == 'IN_PROGRESS'
        assert self.banking_system.get_payment_status(172800041, 'acc4', 'payment13') == 'IN_PROGRESS'
        assert self.banking_system.get_payment_status(172800042, 'acc3', 'payment12') == 'IN_PROGRESS'
        assert self.banking_system.get_payment_status(172800043, 'acc2', 'payment11') == 'CASHBACK_RECEIVED'
        assert self.banking_system.get_payment_status(172800044, 'acc1', 'payment10') == 'CASHBACK_RECEIVED'
        assert self.banking_system.get_payment_status(172800045, 'acc9', 'payment18') == 'IN_PROGRESS'


def main():
    banking_system = BankingSystem()

    print("=== Banking System Level 1 Demo ===")

    # Create accounts
    print(f"Creating account1: {banking_system.create_account(1, 'account1')}")
    print(f"Creating account1 again: {banking_system.create_account(2, 'account1')}")
    print(f"Creating account2: {banking_system.create_account(3, 'account2')}")

    # Deposit operations
    deposit_result = banking_system.deposit(4, "non-existing", 2700)
    print(f"Deposit to non-existing account: {deposit_result if deposit_result is not None else 'None'}")

    deposit_result = banking_system.deposit(5, "account1", 2700)
    print(f"Deposit 2700 to account1: {deposit_result if deposit_result is not None else 'None'}")

    # Transfer operations
    transfer_result = banking_system.transfer(6, "account1", "account2", 2701)
    print(
        f"Transfer 2701 from account1 to account2 (insufficient funds): {transfer_result if transfer_result is not None else 'None'}")

    transfer_result = banking_system.transfer(7, "account1", "account2", 200)
    print(f"Transfer 200 from account1 to account2: {transfer_result if transfer_result is not None else 'None'}")

    # Show final balances
    print(f"Final balance account1: {banking_system.get_balance('account1') or 0}")
    print(f"Final balance account2: {banking_system.get_balance('account2') or 0}")

    print("\n=== Level 2 Demo - Top Spenders ===")

    # Create account3 and add more money
    banking_system.create_account(8, "account3")
    banking_system.deposit(9, "account3", 5000)

    # Make more transfers to demonstrate ranking
    banking_system.transfer(10, "account3", "account1", 1000)
    banking_system.transfer(11, "account1", "account2", 500)

    # Show top spenders
    top_spenders = banking_system.top_spenders(12, 3)
    print(f"Top 3 spenders: {top_spenders}")

    print("\n=== Level 3 Demo - Payment System ===")

    # Test payment operations
    payment1 = banking_system.pay(13, "account1", 500)
    print(f"Payment withdrawal of 500: {payment1}")
    print(f"Account1 balance after payment: {banking_system.get_balance('account1')}")
    print(f"Payment status: {banking_system.get_payment_status(14, 'account1', payment1)}")

    # Simulate cashback processing after 24 hours
    MILLISECONDS_IN_1_DAY = 24 * 60 * 60 * 1000
    banking_system._process_pending_cashbacks(13 + MILLISECONDS_IN_1_DAY)
    print(f"Payment status after 24h: {banking_system.get_payment_status(15, 'account1', payment1)}")
    print(f"Account1 balance after cashback: {banking_system.get_balance('account1')} (includes 2% cashback)")

    # Stop the scheduler when done
    banking_system._stop_scheduler()


import time
from pathlib import Path

def rename_files_by_creation_time(directory):
    # Get all non-directory files
    files = [f for f in Path(directory).iterdir() if f.is_file() and not f.name.startswith('.') and f.suffix.lower() in {'.mp4', '.mkv', '.mov', '.avi'}]

    # Sort files by creation time
    sorted_files = sorted(files, key=lambda f: f.stat().st_mtime)

    left_overs = []
    for idx, file in enumerate(sorted_files, start=1):
        prefix = f"{idx:02d} | "  # e.g., 001_
        orig_nm = file.name.split(' | ')[1]

        new_name = prefix + orig_nm
        new_path = file.with_name(new_name)
        file.rename(new_path)
        is_avail = False

        # If it's a media file, look for associated .vtt file and rename it
        if file.suffix.lower() in {'.mp4', '.mkv', '.mov', '.avi'}:
            base_name = orig_nm.replace(file.suffix, '')
            vtt_path = file.with_name(file.stem + '.en-orig.vtt')
            if vtt_path.exists():
                new_vtt_name = prefix + base_name + '.en-orig.vtt'
                vtt_path.rename(vtt_path.with_name(new_vtt_name))
                left_overs.append((new_name, new_vtt_name, ))

    pprint(left_overs, width=150)
    print(len(left_overs))

if __name__ == "__main__":
    # main()
    rename_files_by_creation_time('/Users/yogeshsharma/Projects/zzzDSAvideosHLD/zzzAI')
