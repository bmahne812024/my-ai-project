import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        absolute_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(absolute_path, file_path))
        valid_target_file = os.path.commonpath([absolute_path, target_file]) == absolute_path

        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_file]

        if args is not None:
            command.extend(args)
        
        completed = subprocess.run(command, capture_output=True, text=True, timeout=30, cwd=working_directory)
        output_string = ""

        if completed.returncode != 0:
            output_string = f"Process exited with code {completed.returncode}\n"
        if not completed.stderr and not completed.stdout:
            output_string += "No output produced\n"
        else:
            output_string += f"STDOUT: {completed.stdout}\nSTDERR: {completed.stderr}"
        return output_string
    

    except Exception as e:
        return f"Error: executing Python file: {e}"
    
