import time
import datetime
# time = time.time()
# time = time.localtime
time = time.asctime(time.localtime(time.time()))

print(time)