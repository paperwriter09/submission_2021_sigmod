import os
import time
import sys
from timeit import default_timer as timer


def run():
	query = sys.argv[1]
	number = 11
	total_time = 0
	for x in range(number):
        	print("Iteration #" + str(x))
        	start = timer()
        	os.system("curl -X GET 'http://127.0.0.1:9000/query/tpcds/"+query+"'")
        	end = timer()
        	elapsed_time = end - start
		if (x != 0):
        		total_time += elapsed_time
        	print("\nTime, sec: " + str(elapsed_time) + "\n")


	avg_time = total_time/(number-1)
	print(query + " - Average time, sec: " + str(avg_time))
	file = open("run_TAG.txt","a")
	file.write("Running query " + query + "\n")
	file.write("Average Execution Time, s: " + str(avg_time) + "\n")
	file.close()

if len(sys.argv) < 2:
                print("Please provide query name")
                sys.exit()
else:
	run()
