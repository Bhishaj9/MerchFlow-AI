import subprocess

def main():
    print("Executing force push...")
    command = "git push --force space HEAD:main"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    print("STDOUT:")
    print(result.stdout)
    print("STDERR:")
    print(result.stderr)

if __name__ == "__main__":
    main()
