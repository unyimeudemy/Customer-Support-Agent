import time
from django.core.management.base import BaseCommand
from main.lib.celery_tasks import GmailSession
import signal
import sys

class Command(BaseCommand):
    help = 'Poll Gmail inbox every 10 seconds'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Starting Gmail inbox poller..."))
        
        session = GmailSession()
        session.connect()


        def shutdown_handler(signum, frame):
            self.stdout.write(self.style.WARNING("Shutting down Gmail poller..."))
            session.disconnect()
            sys.exit(0)

        signal.signal(signal.SIGTERM, shutdown_handler)
        signal.signal(signal.SIGINT, shutdown_handler)

        try:
            while True:
                try:
                    result = session.check_gmail_inbox()
                    print("Result:", result)
                except Exception as e:
                    print("Error checking email:", e)

                time.sleep(10)
        except KeyboardInterrupt:
            print("\nStopping poller...")
        finally:
            session.disconnect()