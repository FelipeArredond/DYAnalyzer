import sys
import subprocess

def scanner():
    process = subprocess.run('checkov -f dockerfile', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output = process.stdout
    output_lines = []
    
    if process.returncode == 0:
        print("Command executed successfully")
        print(output)
        output_lines = output.split('\n')
    return output