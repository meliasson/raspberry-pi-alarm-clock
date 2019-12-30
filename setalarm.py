import os
import subprocess
import sys

hour = sys.argv[1]
minute = sys.argv[2]
path = os.getcwd()

subprocess.call("crontab -l > mycron", shell=True)
subprocess.call(f"echo \"{minute} * * * * cd {path} && pipenv run python startalarm.py\" >> mycron", shell=True)
subprocess.call("crontab mycron", shell=True)
subprocess.call("rm mycron", shell=True)

#write out current crontab
#crontab -l > mycron
#echo new cron into cron file
#echo "00 09 * * 1-5 echo hello" >> mycron
#install new cron file
#crontab mycron
#rm mycron
