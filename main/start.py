"""
Bestand gebruikt om checker.py te runnen met sudo, dit is nodig voor de webInterface.
"""

# importeer nodioge modules
import subprocess

# run checkers.py met sudo privileges en print de output in de command line
subprocess = subprocess.Popen("sudo python3 /home/rpi/Documents/GIP-2022-2023/main/checker.py", shell=True, stdout=subprocess.PIPE)
subprocess_return = subprocess.stdout.read()