import subprocess
import os
import signal


django_process = None
reactjs_process = None
redis_process = None


def start_django_server():
    global django_process

    backend_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../backend")
    )

    venv_path = os.path.abspath(os.path.join(backend_path, "../env/bin/python"))
    manage_py = os.path.join(backend_path, "manage.py")

    django_process = subprocess.Popen(
        [venv_path, manage_py, "runserver"],
        cwd=backend_path,
        # stdout=subprocess.DEVNULL,
        # stderr=subprocess.DEVNULL
    )


def start_reactjs_server():
    global reactjs_process

    frontend_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../frontend")
    )
    reactjs_process = subprocess.Popen(
        ["npm", "run", "dev"],
        cwd=frontend_path,
        # stdout=subprocess.DEVNULL,
        # stderr=subprocess.DEVNULL
    )


def stop_django_server():
    global django_process
    if django_process:
        django_process.terminate()


def stop_reactjs_server():
    global reactjs_process
    if reactjs_process:
        reactjs_process.terminate()


def start_redis_server():
    global redis_process

    current_dir = os.path.dirname(__file__)
    redis_path = os.path.abspath(os.path.join(current_dir, "../embedded_redis"))
    redis_executable = os.path.join(redis_path, "redis-server")

    redis_process =  subprocess.Popen(
        [redis_executable],
        cwd=redis_path,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


def stop_redis_server():
    global redis_process
    if redis_process:
        redis_process.terminate()