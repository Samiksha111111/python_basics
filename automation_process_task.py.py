import subprocess
import os
import shutil
def generate_system_report(output_file):
    try:
        #Get the current working directory
        cwd=os.getcwd()

        #Get disk usage of the current directory
        disk_usage=shutil.disk_usage(cwd)

        #Get the system information
        system_info=subprocess.run(['uname', '-a'], capture_output=True, text=True).stdout
        #Write a report to the file
        with open(output_file, 'w') as file:
            file.write(f"Current working directory: {cwd}\n")
            file.write(f"Disk usage:\n")
            file.write(f"Total: {disk_usage.total/(1024**3):.2f} GB\n")
            file.write(f"Total: {disk_usage.used/(1024**3):.2f} GB\n")
            file.write(f"Total: {disk_usage.free/(1024**3):.2f} GB\n")
            file.write(f"System information:\n {system_info}\n")
        print(f"Sytem diagonased report saved to '{output_file}'")
    except Exception as e:
        print(f"Error: {e}")

#Example usage
generate_system_report("system_report.txt")
