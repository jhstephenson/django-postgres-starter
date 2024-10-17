import subprocess
import random
import string

def run_command(command):
    subprocess.run(command, shell=True, check=True)

def generate_secret_key():
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(50))