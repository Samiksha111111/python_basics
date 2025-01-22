import subprocess

# Function to list processes and save to file
def list_processes():
    # Run the 'tasklist' command and capture output
    result = subprocess.run(['tasklist'], capture_output=True, text=True)
    
    # Write the output to a file
    with open('process_list.txt', 'w') as file:
        file.write(result.stdout)
    
    print("Process list saved to process_list.txt")

# Call the function
list_processes()
