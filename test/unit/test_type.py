from pathlib import Path

from fact_helper_file.type import get_file_type_from_binary, get_file_type_from_path


def test_get_file_type_system_magic():
    zip_file = Path(__file__).parent.parent / 'data' / 'test.zip'
    file_type = get_file_type_from_path(str(zip_file))
    assert file_type['mime'] == 'application/zip', 'mime type not correct'
    assert file_type['full'] == 'Zip archive data, at least v2.0 to extract', 'full type not correct'

    assert file_type == get_file_type_from_binary(zip_file.read_bytes())


def test_get_file_type_custom_magic():
    ros_file = Path(__file__).parent.parent / 'data' / 'ros_header'
    file_type = get_file_type_from_path(str(ros_file))
    assert file_type['mime'] == 'firmware/ros', 'mime type not correct'
    assert file_type['full'] == 'ROS Container', 'full type not correct'

    assert file_type == get_file_type_from_binary(ros_file.read_bytes())


def test_get_file_type_of_internal_link_representation():
    sym_link_file = Path(__file__).parent.parent / 'data' / 'symbolic_link_representation'
    file_type = get_file_type_from_path(str(sym_link_file))
    assert file_type['full'] == 'symbolic link to \'/tmp\''
    assert file_type['mime'] == 'inode/symlink'

    assert file_type == get_file_type_from_binary(sym_link_file.read_bytes())


def test_get_file_type_file_doesnt_exist():
    file_type = get_file_type_from_path('/error/broken/link')
    assert file_type['full'] == 'Error: File not in storage!'
    assert file_type['mime'] == 'error/file-not-found'


def test_get_file_type_from_none():
    file_type = get_file_type_from_binary(None)
    assert file_type['mime'] == 'application/octet-stream'
    assert file_type['full'] == 'data'
