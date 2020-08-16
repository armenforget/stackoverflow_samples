from pathlib import Path
from PIL import Image


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


def print_high_res_images(directory: str):
    root_path = Path(directory).resolve()
    high_res_images = get_high_res_images(root_path)

    print('High resolution images:')
    for file_path in high_res_images:
        print(file_path)


def get_high_res_images(root_path: Path) -> []:
    return [path for path in root_path.rglob("*.*") if is_high_res_image(path)]


def is_high_res_image(file_path: Path) -> bool:
    if is_image(file_path):
        image = Image.open(file_path)
        width, height = image.size
        return width > 2048 and height > 2048

    return False


def is_image(file: Path) -> bool:
    return file.suffix.lower() in ['.png', '.jpg']


def get_files_without_extension(dir_path: Path, pattern: str) -> []:
    return [f.with_suffix('') for f in dir_path.rglob(pattern)]


def is_file_invalid(file: Path, prefix: str) -> bool:
    return is_target_type(file) and not is_filename_valid(file, prefix)


def is_target_type(file: Path) -> bool:
    return file.suffix.lower() in ['.png', '.json']


def is_filename_valid(file: Path, prefix: str) -> bool:
    return file.name.startswith(prefix)


print_high_res_images('./folder3')

root_dir = Path(r'D:\Projects\stackoverflow_samples')
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
