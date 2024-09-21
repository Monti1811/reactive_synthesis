import subprocess

files = [
    't1_charging_robot',
    't2_cargo_robot',
    't3_helipad',
    't4_ctr_controller',
]


for filename in files:
	# Run run-docker.sh > filename.tlsf for each file
	capture = subprocess.run(['wsl', '/mnt/f/Uni/reactive_synthesis/run-docker.sh','/mnt/f/Uni/reactive_synthesis/'+ filename + '.tlsf'], capture_output=True)
	# Save the output to a file
	file = open("data/" + filename + '.aiger', 'w')
	file.write(capture.stdout.decode('utf-8'))
	file.close()
	print("File " + filename + ".aiger created")


