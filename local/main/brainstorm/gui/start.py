import subprocess

subprocess = subprocess.Popen("sudo python3 local/main/brainstorm/gui/web.py", shell=True, stdout=subprocess.PIPE)
subprocess_return = subprocess.stdout.read()
print(subprocess_return)