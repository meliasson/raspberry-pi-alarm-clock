import os
import subprocess
import sys

hour = sys.argv[1]
minute = sys.argv[2]
path = os.getcwd()
command = "pipenv run python startalarm.py"

subprocess.call("crontab -l > mycron", shell=True)
subprocess.call(f"echo \"{minute} {hour} * * * cd {path} && {command}\" >> mycron", shell=True)
subprocess.call("crontab mycron", shell=True)
subprocess.call("rm mycron", shell=True)
