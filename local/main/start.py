import subprocess

subprocess = subprocess.Popen("sudo python3 /home/rpi/Documents/GIP-2022-2023/local/main/checker.py", shell=True, stdout=subprocess.PIPE)
subprocess_return = subprocess.stdout.read()
