import subprocess
import os

# Run a simple command and capture the output
result = subprocess.run(["echo", "Hello, World!"], capture_output=True, text=True)
print("Command Output:", result.stdout)

# List files in the current directory using 'ls' or 'dir' (platform-specific)
command = ["ls"] if os.name != "nt" else ["dir"]
result = subprocess.run(command, capture_output=True, text=True, shell=True)
print("Files in the current directory:")
print(result.stdout)

# Check for errors (e.g., invalid commands)
result = subprocess.run(["fakecommand"], capture_output=True, text=True, shell=True)
if result.returncode != 0:
    print("Error:", result.stderr)
