import time
from SystemMemoryLedger import SystemMemoryLedger

class ProactiveMessenger:
    def __init__(self):
        self.last_check = 0
        self.interval = 1800  # Every 30 minutes
        self.ledger = SystemMemoryLedger()

    def check_conditions(self):
        return [
            "You haven’t received a message today.",
            "Your tokens are awaiting activation.",
            "Consider reflecting on the last alignment pledge."
        ]

    def message_founder(self):
        insights = self.check_conditions()
        for msg in insights:
            self.ledger.record("message_to_founder", msg)
            print(f"[Proactive] Sent to founder: {msg}")

    def run_loop(self):
        while True:
            if time.time() - self.last_check >= self.interval:
                self.message_founder()
                self.last_check = time.time()
            time.sleep(60)