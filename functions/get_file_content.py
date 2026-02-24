import os


def get_file_content(working_directory, file_path):
    try:
        absolute_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(absolute_path, file_path))
        valid_target_file = os.path.commonpath([absolute_path, target_file]) == absolute_path

        if valid_target_file == False:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(file_path):
            return f'Error: "File not found or is not a regular file: "{file_path}"'
        
        #i am on step 4 of ch2: Functions, l3:get file content at this point

    except Exception as e:
        return f"Error: {e}"