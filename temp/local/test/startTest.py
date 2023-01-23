import subprocess

subprocess = subprocess.Popen("sudo python3 local/test/test.py", shell=True, stdout=subprocess.PIPE)
subprocess_return = subprocess.stdout.read()