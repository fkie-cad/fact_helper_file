import logging
from pathlib import Path
from typing import Union

import magic


def get_file_type_from_path(file_path: Union[str, Path]) -> dict:
    '''
    Generate a dict containing full and mime file type from file path.
    First it tries to use a custom magic file, then defaults to system magic.

    :param binary: bytes
    :return: dict
    '''
    path_string = file_path if isinstance(file_path, str) else str(file_path)
    return _get_file_type(path_string, 'from_file')


def get_file_type_from_binary(binary: bytes) -> dict:
    '''
    Generate a dict containing full and mime file type from bytes object
    First it tries to use a custom magic file, then defaults to system magic.

    :param binary: bytes
    :return: dict
    '''
    return _get_file_type(binary, 'from_buffer')


def _get_file_type(path_or_binary, function_name):
    magic_path = str(Path(__file__).parent / 'bin' / 'custommime.mgc')

    magic_wrapper = magic.Magic(magic_file=magic_path, mime=True)
    mime = _get_type_from_magic_object(path_or_binary, magic_wrapper, function_name, mime=True)

    magic_wrapper = magic.Magic(magic_file=magic_path, mime=False)
    full = _get_type_from_magic_object(path_or_binary, magic_wrapper, function_name, mime=False)

    if mime == 'application/octet-stream':
        mime = _get_type_from_magic_object(path_or_binary, magic, function_name, mime=True)
        full = _get_type_from_magic_object(path_or_binary, magic, function_name, mime=False)
    return {'mime': mime, 'full': full}


def _get_type_from_magic_object(path_or_binary, magic_object, function_name, mime=True):
    try:
        if isinstance(magic_object, magic.Magic):
            result = getattr(magic_object, function_name)(path_or_binary)
        else:
            result = getattr(magic_object, function_name)(path_or_binary, mime=mime)
    except FileNotFoundError as e:
        logging.error('File not found: {}'.format(e))
        result = 'error/file-not-found' if mime else 'Error: File not in storage!'
    except Exception as exception:
        logging.error('Could not determine file type: {} {}'.format(type(exception), str(exception)))
        result = 'application/octet-stream' if mime else 'data'
    return result
