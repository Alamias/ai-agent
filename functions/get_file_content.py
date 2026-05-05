import os


def get_file_content(working_directory, file_path):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target = os.path.normpath(os.path.join(working_dir_abs, file_path))

        try:
            common = os.path.commonpath([working_dir_abs, target])
        except ValueError:
            return (
                f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
            )

        if common != working_dir_abs:
            return (
                f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
            )

        if not os.path.isfile(target):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        MAX_CHARS = 10000

        with open(target, "r", encoding="utf-8", errors="replace") as f:
            content = f.read(MAX_CHARS)
            truncated = bool(f.read(1))

        if truncated:
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return content

    except Exception as e:
        return f"Error: {e}"
