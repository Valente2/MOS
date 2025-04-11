
import os
import subprocess

def simple_shell():
    """A simple terminal shell."""
    que=input("do you want debug mode on(shows the tokens after you input) y/n ")
    while True:
        try:
            # Get the current working directory
            cwd = os.getcwd()
            # Prompt the user
            command = input(f"{cwd}$ ")

            # Handle exit command
            if command.lower() == "exit":
                break

            # Handle empty command
            if not command.strip():
                continue

            # Split the command into arguments
            args = command.split()
            if que == "y":
                print(args)
            elif que == "n":
                continue
            else:
                continue
            # Handle cd cpmmands
            if command_name == "cd":
                if len(args) > 1:
                    target_path = args[1]
                    try:
                        os.chdir(target_path)
                    except FileNotFoundError:
                        print(f"Error: No such file or directory: {target_path}")
                    except NotADirectoryError:
                        print(f"Error: Not a directory: {target_path}")
                    except OSError as e:
                        print(f"Error changing directory: {e}")
                else:
                    # Optionally go to the home directory if no path is provided
                    home_dir = os.path.expanduser("~")
                    try:
                        os.chdir(home_dir)
                    except OSError as e:
                        print(f"Error changing to home directory: {e}")
                continue  # Skip the subprocess execution for cd
            # Execute the command using subprocess
            process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
            stdout, stderr = process.communicate()

            # Decode and print the output
            if stdout:
                print(stdout.decode())
            if stderr:
                print(stderr.decode())

        except FileNotFoundError:
            print("Command not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    simple_shell()
