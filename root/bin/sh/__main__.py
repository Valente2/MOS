
import os
import subprocess

def simple_shell():
    """A simple terminal shell."""
    
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
            print(args)
            # Handle cd cpmmands
            if args[0] == "cd":
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

            elif args[0] == "about":
                print("(C) Valente Vescio")
                print("Welcome to the MOS shell here is a really small techinacly os running on your computer")
                print("MOS was made when I wanted to make a way that someone could experiment with  things,code, or just have fun")
                print("MOS was not and will not be made as a true os there is no kernel no bootloader just a shell some programs and thats it")#created about commamnd

                # Execute the command using subprocess
            process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
            stdout, stderr = process.communicate()

            # Decode and print the output
            if stdout:
                out = stdout.decode()
                print(out)
            if stderr:
                err = stderr.decode()
                print(err)

        except FileNotFoundError:
            print("Command not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    simple_shell()
