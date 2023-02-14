"""
This submodule provides the entry-point function :py:func:`scaffold.command_line.main`
for ``scaffold`` as a CLI tool.
"""
# Built-in
import argparse
from pathlib import Path
from shutil import copyfile
from typing import Optional


def main() -> None:
    """
    Entry-point function for the :py:mod:`scaffold` package.
    """
    parser = argparse.ArgumentParser(
        description="Scaffold a project with src layout."
    )
    parser.add_argument(
        '-r', '--root', type=Path, default=[Path.cwd()], action='append',
        help='project root folder path.'
    )
    args = parser.parse_args()

    if len(args.root) == 1:
        root_dir: Path = args.root[0]
    elif len(args.root) == 2:
        if args.root[1].is_absolute():
            root_dir = args.root[1]
        else:
            root_dir = args.root[0].joinpath(args.root[1])
    else:
        print('Only accepting 0 or 1 --root parameter.')
        return

    vscode_dir = root_dir.joinpath('.vscode')
    vscode_dir.mkdir(exist_ok=True)
    copy_config_file('.vscode/settings.json', 'vscode_settings.txt')

    copy_config_file(root_dir, '.flake8', 'flake8.txt')
    copy_config_file(root_dir, '.gitignore', 'gitignore.txt')
    copy_config_file(root_dir, 'mypy.ini', 'mypy.txt')
    copy_config_file(root_dir, 'pytest.ini', 'pytest.txt')
    copy_config_file(root_dir, 'pyproject.toml', 'pyproject.txt')
    copy_config_file(root_dir, 'setup.cfg', 'setup_cfg.txt')
    copy_config_file(root_dir, 'requirements-dev.txt', 'requirements-dev.txt')
    touch_file(root_dir, 'README.md')
    touch_file(root_dir, 'LICENSE')

    root_dir.joinpath('main').mkdir(exist_ok=True)
    root_dir.joinpath('adhoc').mkdir(exist_ok=True)
    root_dir.joinpath('tests').mkdir(exist_ok=True)

    src_dir = root_dir.joinpath('src')
    src_dir.mkdir(exist_ok=True)
    pack_dir = src_dir.joinpath('example_package')
    pack_dir.mkdir(exist_ok=True)
    touch_file('__init__.py', pack_dir)
    touch_file('py.typed', pack_dir)


def copy_config_file(root_dir: Path, target_name: str, source_name: str) -> None:
    """
    Copy a source file that comes with this package into the target root directory, and
    change its file name to the right version.

    :param root_dir: Root directory of the project to be scaffolded.
    :type root_dir: :py:class:`~pathlib.Path`
    :param target_name: Proper name of the file after landing in the root directory.
    :type target_name: str
    :param source_name: File name as the source is stored as a data file in this package.
    :type source_name: str
    """
    file_dir = Path(__file__).parent
    data_dir = file_dir.joinpath('data')
    target_path = root_dir.joinpath(target_name)
    source_path = data_dir.joinpath(source_name)
    if not target_path.exists():
        copyfile(source_path, target_path)

def touch_file(
    root_dir: Path, target_name: str, target_dir: Optional[Path] = None
) -> None:
    """
    Create a new empty file.

    :param root_dir: Root directory of the project to be scaffolded.
    :type root_dir: :py:class:`~pathlib.Path`
    :param target_name: Name of the empty file to be created.
    :type target_name: str
    :param target_dir: Target directory for the new file, defaults to None, which places the file
       in the root directory.
    :type target_dir: :py:class:`~pathlib.Path`, optional
    """
    if isinstance(target_dir, Path):
        target_path = target_dir.joinpath(target_name)
    else:
        target_path = root_dir.joinpath(target_name)
    if not target_path.exists():
        with open(target_path, 'w') as _:
            pass
