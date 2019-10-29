import subprocess
import datetime

#subprocess.call(["git", "status"])
#subprocess.call(["git", "add", "."])
#subprocess.call(["git", "commit", "-m", "auto push at " + str(datetime.datetime.now())]) # 加上当前系统的时间
#returncode = subprocess.call(["git", "push"])
returncode = 1
while returncode != 0:
    returncode = subprocess.call(["git", "push"])
    print(returncode)
print(returncode)
