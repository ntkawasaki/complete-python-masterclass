# always use UTC time
# import time


# # UTC in a named tuple, time = 0 starts on jan 1 1970
# print(time.gmtime(0))
#
# # local time
# print(time.localtime())
#
# # epoch, number seconds since jan 1 1970
# print(time.time())
# print()
#
# # extract parts
# time_here = time.localtime()
# print(time_here)
# print("Year: ", time_here[0], time_here.tm_year)  # two ways to print info, from tuple or through key
# print("Month: ", time_here[1], time_here.tm_mon)
# print("Day: ", time_here[2], time_here.tm_mday)

import time
# from time import time as my_timer  # problem is if daylight savings resets between
from time import perf_counter as my_timer  # gives time elapsed without using actual time
# from time import monotonic as my_timer  # time that cannot go backwards
# from time import process_time as my_timer  # time spent by CPU
import random

input("Press enter to start.")  # since input() used enter will signal the action
wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()

input("Press enter to stop.")
end_time = my_timer()

print("Started at: " + time.strftime("%X", time.localtime(start_time)))
print("Ended at: " + time.strftime("%X", time.localtime(end_time)))
print("Your reaction time was {} seconds.".format(round(end_time - start_time, 2)))
