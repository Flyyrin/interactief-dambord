import subprocess

subprocess = subprocess.Popen("sudo python3 local/main/checker.py", shell=True, stdout=subprocess.PIPE)
subprocess_return = subprocess.stdout.read()
