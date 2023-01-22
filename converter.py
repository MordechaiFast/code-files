"""Example script for testing argparse, read/write ops, and logging"""
from argparse import ArgumentParser, Namespace
import sys

def parse(args: str) -> Namespace:
    parser = ArgumentParser(
     description="Script for converting the word Shabbat to Shabbos",
     allow_abbrev=True,
    )
    parser.version = 'Converter v2.0'
    parser.add_argument('-v', action='version')
    
    parser.add_argument('source_file',
     help='The location of the source file')
    parser.add_argument('-lines', nargs='?', type=int, const=1,
     help='The number of lines to convert')
    parser.add_argument('dest_file', metavar='DESTINATION', nargs='?',
     default=None,
     help='Location of the DESTINATION file.'
     ' By default overwrites the existing file')
    
    parser.add_argument('-c', '--change-back', action='store_true',
     help="Change the source file back to saying 'Shabbat'")

    return parser.parse_args(args)

import logging
log = logging.Logger('converter')

terminal_logging = logging.StreamHandler()
terminal_logging.setLevel(logging.WARNING)
terminal_logging.setFormatter(
 logging.Formatter('{levelname}: {message}', style='{'))
log.addHandler(terminal_logging)

file_logging = logging.FileHandler('converter.log')
file_logging.setLevel(logging.DEBUG)
file_logging.setFormatter(
 logging.Formatter('{asctime}:{name}:{levelname}:{message}', style='{'))
log.addHandler(file_logging)

#logging.basicConfig(format='{levelname}: {message}', style='{')

from pathlib import Path

def convert(source: Path, dest: str | Path, lines: int):
    if dest is None:
        log.warning("You didn't give a destination file!")
        dest = source
    else:
        dest = Path(dest)

    new_content = ''
    try:
        with source.open() as file:
            if lines is not None:
                for line in file.readlines(lines):
                    new_content += line.replace('Shabbat', 'Shabbos')
                remaining_content = file.read()
                new_content += remaining_content
            else:
                content = file.read()
                new_content = content.replace('Shabbat', 'Shabbos')
        log.info(f"Reading {source}")
        with dest.open(mode='w') as file:
            file.write(new_content)
        log.info(f"Writing 'Shabbos' to {dest}")
    except FileNotFoundError as err:
        log.error(f"Can't read '{source}'\n{err}")
    except PermissionError as err:
        log.error(f"Can't write to '{dest}'\n{err}")

def undo(source: Path):
    with open(source) as file:
        content = file.read()
    with open(source, 'w') as file:
        file.write(content.replace('Shabbos', 'Shabbat'))

if __name__ == '__main__':
    args: Namespace = parse(sys.argv[1:])
    source = Path(args.source_file)
    dest = args.dest_file
    lines: int = args.lines
    revert: bool = args.change_back
    if revert == False:
        convert(source, dest, lines)
    else:
        undo(source)