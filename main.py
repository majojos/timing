"""
Example usage of module timing
"""

from timing import Timing
import time

my_outer_process = Timing("My outer process")
my_inner_process = Timing("My inner process")

my_outer_process.start()
time.sleep(2)

my_inner_process.start()
time.sleep(2)
my_inner_process.stop()

time.sleep(1)
my_outer_process.stop()

#Output:
# 'My outer process' started.
# 'My inner process' started.
# 'My inner process' finished.
# ++++++++++++SUMMARY+EXECUTION+TIME+'My inner process'+++++++++++++
# Elapsed time 'My inner process':0 min, 2.000 sec
# 'My outer process' finished.
# ++++++++++++SUMMARY+EXECUTION+TIME+'My outer process'+++++++++++++
# Elapsed time 'My outer process':0 min, 5.000 sec
