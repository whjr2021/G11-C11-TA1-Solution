# Import "time" module
import time

# Call the function "time()" from "time" module and store the result in "t1" variable
t1 = time.time()
print("T1 =", t1, "seconds")

# Introduce a delay of 10 seconds.
# Call the function "sleep()" from "time" module and pass 10 as the input into fuction
time.sleep(10)

# Call the function "time()" from "time" module and store the result in "t2" variable
t2 = time.time()
print("T2 =", t2, "seconds")

# Calculate the elapsed time by finding difference between "t1" and "t2" and store the difference "elapsed_time"
elapsed_time = t2 - t1
print("Elapsed time =", elapsed_time, "seconds")

