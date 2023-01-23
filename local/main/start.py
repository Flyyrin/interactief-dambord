import subprocess

if input("t") == "t":
    subprocess = subprocess.Popen("sudo python3 local/test/test.py", shell=True, stdout=subprocess.PIPE)
    subprocess_return = subprocess.stdout.read()
else:
    subprocess = subprocess.Popen("sudo python3 local/main/checkers.py", shell=True, stdout=subprocess.PIPE)
    subprocess_return = subprocess.stdout.read()
