import os
import subprocess

def execute_command(command, input_file=None, output_file=None):
  args = command.split()

  # Set up redirection if necessary
  if input_file:
    with open(input_file, 'r') as f:
      stdin = f
  else:
    stdin = None

  if output_file:
    with open(output_file, 'w') as f:
      stdout = f
  else:
    stdout = subprocess.PIPE


  process = subprocess.Popen(args, stdin=stdin, stdout=stdout, stderr=subprocess.STDOUT)
  output, _ = process.communicate()  # Wait for process to finish and capture output

  return process.returncode, output.decode()

def main():
  while True:
    command = input("$ ")

    # Check for exit command
    if command.lower() == "exit":
      break

    # Separate command and redirection arguments
    parts = command.split('>')
    command = parts[0].strip()  # Extract the command

    # Check for output redirection
    output_file = None
    if len(parts) > 1:
      output_file = parts[1].strip() 

    # Check for input redirection (implement if needed)
    input_file = None  



    exit_code, output = execute_command(command, input_file, output_file)

    if output:
      print(output)

    if exit_code != 0:
      print(f"Command exited with code: {exit_code}")

if __name__ == "__main__":
  main()
