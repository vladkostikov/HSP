import os


def search_files(path: str = ".") -> list:
    current_directory = os.listdir(path)
    files_in_current_directory = current_directory[:]

    for file in current_directory:
        path_to_file = path + "/" + file
        is_file_a_directory = os.path.isdir(path_to_file)

        files_in_directory = []
        if is_file_a_directory:
            files_in_directory = search_files(path_to_file)

        files_in_current_directory.extend(files_in_directory)

    return files_in_current_directory
