

import os
import subprocess

def simple_shell():
    """A simple terminal shell."""
    
    
    while True:
        try:
            # Get the current working directory
            cwd = os.getcwd()
            # Display the prompt with the current working directory
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
                continue
            elif args[0] == "oiia":
                for i in range(int(args[1])):
                    print("oiiai", end = "")
                    i += 1
                continue
            else:
                # Execute the command using subprocess without capturing output
                try:
                    process = subprocess.Popen(args)
                    process.wait() # Wait for the process to complete
                except FileNotFoundError:
                    print("Command not found.")
                except Exception as e:
                    print(f"An error occurred: {e}")
        except KeyboardInterrupt:
            print("\nExiting shell.")
            break
        except EOFError:   
            print("\nExiting shell.")
            break
        except OSError as e:
            if e.errno == os.errno.ENOENT:
                print("Command not found.")
            else:
                print(f"An error occurred: {e}")
        except ValueError:  
            print("Invalid command.")
        except subprocess.CalledProcessError as e:  
            print(f"Command '{e.cmd}' failed with return code {e.returncode}.")
        except PermissionError:             
            print("Permission denied.")
        except NotADirectoryError:
            print("Not a directory.")
        except FileNotFoundError:
            print("Command not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    simple_shell()
