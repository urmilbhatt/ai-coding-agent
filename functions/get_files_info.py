import os

def get_files_info(working_directory, directory="."):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        
        full_path = os.path.abspath(os.path.join(working_directory_abs, directory))

        if not full_path.startswith(working_directory_abs):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'

        contents = os.listdir(full_path)
        result_lines = []
        for item in sorted(contents):
            item_path = os.path.join(full_path, item)
            file_size = os.path.getsize(item_path) if os.path.isfile(item_path) else 0
            is_dir = os.path.isdir(item_path)
            result_lines.append(f'- {item}: file_size={file_size} bytes, is_dir={is_dir}')
        
        return "\n".join(result_lines)

    except Exception as e:
        return f'Error: {str(e)}'
