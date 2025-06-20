from agent.celery import app


def get_worker_status():
    io_task_inspector = app.control.inspect(destination=["io_worker_host"])
    cpu_task_inspector = app.control.inspect(destination=["cpu_worker_host"])

    io_active = io_task_inspector.active() or {}
    io_reserved = io_task_inspector.reserved() or {}
    cpu_active = cpu_task_inspector.active() or {}
    cpu_reserved = cpu_task_inspector.reserved() or {}

    return {
        "io_active_len": len(io_active.get("io_worker_host", [])),
        "io_reserved_len": len(io_reserved.get("io_worker_host", [])),
        "cpu_active_len": len(cpu_active.get("cpu_worker_host", [])),
        "cpu_reserved_len": len(cpu_reserved.get("cpu_worker_host", [])),
    }
