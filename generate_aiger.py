import subprocess
import time

files = [
	't1_charging_robot',
	't2_cargo_robot',
	't3_helipad',
	't4_ctr_controller',
	't6/t1_charging_robot',
	't6/t2_cargo_robot',
	't6/t3_helipad',
	't6/t4_ctr_controller',
	't6/t6_maintenance_robot',
]


if __name__ == "__main__":

	for filename in files:
		# Record the start time
		start_time = time.time()
		
		# Run run-docker.sh > filename.tlsf for each file
		capture = subprocess.run(['wsl', '/mnt/f/Uni/reactive_synthesis/run-docker.sh','/mnt/f/Uni/reactive_synthesis/'+ filename + '.tlsf'], capture_output=True)
		
		# Record the end time
		end_time = time.time()
		
		# Calculate the elapsed time
		elapsed_time = end_time - start_time
		
		# Save the output to a file
		with open("data/" + filename + ".aiger", "w") as f:
			f.write(capture.stdout.decode())
		
		print("File " + filename + ".aiger created")
		print(f"Time taken for {filename}: {elapsed_time:.2f} seconds")


