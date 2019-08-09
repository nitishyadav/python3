#subprocess, it is easy to spawn new processes and get their return code, execute external commands and astart new applications.

import subprocess
subprocess.call(["touch","sample.txt"])
subprocess.call(["ls"])
print("sample file created")
subprocess.call(["rm","sample.txt"])
subprocess.cal(["ls"])
print("Sample file deleted")