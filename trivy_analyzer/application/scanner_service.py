import sys
import subprocess
from django.shortcuts import render

def scanner():
    process = subprocess.run('checkov -f dockerfile', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output = process.stdout
    
    if process.returncode == 0:
        print("Command executed successfully")
        print(output)
    return output.split('\n')