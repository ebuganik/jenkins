import subprocess
import sys

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "uninstall", package])

# Example
if __name__ == '__main__':
    install('argh')