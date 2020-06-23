from pathlib import Path


def get_invalid_files_from(directory: Path) -> []:
    dir_path = directory.resolve()
    parent_folder = dir_path.stem
    files = dir_path.rglob('*')
    return [str(f) for f in files if is_file_invalid(file=f, prefix=parent_folder)]


def get_unpaired_files(directory: Path) -> []:
    dir_path = directory.resolve()
    json_files = get_files_without_extension(dir_path, pattern='*.json')
    png_files = get_files_without_extension(dir_path, pattern='*.png')
    return [str(f.absolute()) for f in set(json_files) ^ set(png_files)]


def get_files_without_extension(dir_path: Path, pattern: str) -> []:
    return [f.with_suffix('') for f in dir_path.rglob(pattern)]


def is_file_invalid(file: Path, prefix: str) -> bool:
    return is_target_type(file) and not is_filename_valid(file, prefix)


def is_target_type(file: Path) -> bool:
    return file.suffix.lower() in ['.png', '.json']


def is_filename_valid(file: Path, prefix: str) -> bool:
    return file.name.startswith(prefix)


root_dir = Path(r'C:\temp')
sub_dirs = [f for f in root_dir.iterdir() if f.is_dir()]

for target_dir in sub_dirs:
    print()

    invalid_files = get_invalid_files_from(target_dir)
    if invalid_files:
        print('Invalid file paths were found:')
        print('\n'.join(invalid_files))

    unpaired_files = get_unpaired_files(target_dir)
    if unpaired_files:
        print('Unpaired file paths were found:')
        print('\n'.join(unpaired_files))
