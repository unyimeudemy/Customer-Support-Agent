from celery import shared_task
import time
from main.lib.omni_channel_message import OmniChannelMessage1

@shared_task(bind=True, queue="io_tasks")
def handle_failed_order_email(self, chat):
    """
        I/O‑bound email task.
        Will be routed automatically to the 'io_tasks' queue.
    """
    print("------ started order email task -----")
    time.sleep(10)  
    print("----- order email task finished ------", chat)


@shared_task(bind=True, queue="cpu_tasks")
def generate_report(self, chat):
    """
    CPU heavy PDF/report generation.
    Will be routed automatically to the 'cpu_tasks' queue.
    """
    print("+++ started PDF generation +++")
    # (Your reportlab or heavy‑compute logic here)
    time.sleep(15)  # simulate heavy work
    print("+++ finished PDF generation +++")