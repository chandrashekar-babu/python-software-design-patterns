import subprocess
import sys

class Run:
    def __init__(self, cmd):
        self.cmd = cmd
    
    def __or__(self, other):
        return Run(f"{self.cmd} | {other.cmd}")
    
    def __gt__(self, out):
        subprocess.run(self.cmd, shell=True, stdout=out, stderr=out)

    def run(self):
        self > sys.stdout

if __name__ == "__main__":
    Run("ls") | Run("wc -l") > sys.stdout
    Run("ls -lrt") > sys.stdout
    Run("ls -lrt").run()