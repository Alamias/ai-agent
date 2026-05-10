import os

def write_file(working_directory, file_path, content):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))

        try:
            common = os.path.commonpath([working_dir_abs, file_path_abs])
        except ValueError:
            return (
                f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
            )

        existing_directory = os.path.isdir(file_path_abs)
        if existing_directory:
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(os.path.dirname(file_path_abs), exist_ok=True)

        with open(file_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"
