# if setup is done, jump straight to starting the virtualenv and running app.py

# initial setup stuff
# install virtualenv if not already installed
# create virtualenv and name it myenv, have script print some output to tell user the virtual environment name
# go into virtual env
# download following packages: pandas, panel, pymysql

# post setup
# go into virtual env
# run app.py
import os
import subprocess

env_name = "myenv"
app_script = "app.py"

# runs the os command based on the os
def run_command(command):
    result = subprocess.run(command, shell=True,
                            capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(result.stdout)
    return result.returncode

# checks if the virtual environment is set
def check_virtualenv(env_name):
    if os.name == 'nt':  # windows
        venv_path = os.path.join(env_name, 'Scripts')
    else:  # mac and linux
        venv_path = os.path.join(env_name, 'bin')
    return os.path.isdir(venv_path)

# creates virtual environment if it doesn't work
def create_virtualenv(env_name):
    """
    Create the virtual environment if it doesn't exist.
    """
    if not check_virtualenv(env_name):
        print(f"Creating virtual environment '{env_name}'...")
        run_command(f"python -m venv {env_name}")
        print(f"Virtual environment '{env_name}' created.")
        python_interpreter = activate_virtualenv(env_name, "install")
        run_command(f"{python_interpreter} install -r requirements.txt")

# activates virtual environment
def activate_virtualenv(env_name, task):
    if os.name == 'nt':
        if task == "run app":
            print(os.path.join(env_name, 'Scripts', 'python'))
            return os.path.join(env_name, 'Scripts', 'python')
        elif task == "install":
            print(os.path.join(env_name, 'Scripts', 'pip'))
            return os.path.join(env_name, 'Scripts', 'pip')
    else:
        if task == "run app":
            print(os.path.join(env_name, 'bin', 'python'))
            return os.path.join(env_name, 'bin', 'python')
        elif task == "install":
            print(os.path.join(env_name, 'bin', 'pip'))
            return os.path.join(env_name, 'bin', 'pip')

# runs the app
def run_app(env_name, app_script):
    print(f"Running virtual environment...")
    python_interpreter = activate_virtualenv(env_name, "run app")
    print(f"Running {app_script} ...")
    run_command(f"{python_interpreter} {app_script}")

# Post-setup: Activate virtualenv and run app.py
print("Starting the virtual environment and running the application...")
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
create_virtualenv(env_name)
run_app(env_name, app_script)
