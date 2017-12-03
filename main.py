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
