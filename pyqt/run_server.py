import subprocess
import os

django_process = None
reactjs_process = None

def start_django_server():
    global django_process

    backend_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../backend")
    )

    manage_py = os.path.join(backend_path, "manage.py")
    django_process = subprocess.Popen(
        ["python3", manage_py, "runserver"],
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