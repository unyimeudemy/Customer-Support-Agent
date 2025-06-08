from celery import shared_task
import time

@shared_task(bind=True, queue="io_tasks")
def handle_failed_order_email(self, chat):
    """
        I/O‑bound email task.
        Will be routed automatically to the 'io_tasks' queue.
    """



@shared_task(bind=True, queue="cpu_tasks")
def generate_report(self, chat):
    """
    CPU heavy PDF/report generation.
    Will be routed automatically to the 'cpu_tasks' queue.
    """
