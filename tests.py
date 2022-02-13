from batch_run import escape, substitute_dir
from pathlib import Path




def test_files(monkeypatch,tmp_path):
    source = tmp_path / 'source'
    source.mkdir()
    (source / 'file_1.ext').touch()
    (source / 'file_2.ext').touch()
    (source / 'file_3.ext').touch()
    (tmp_path / 'destination').mkdir()
    monkeypatch.chdir(tmp_path)

# -----------------------------------------------


def test_escape():
    assert (
        escape("path/to/dir/filename with spaces.ext")
        == '"path/to/dir/filename with spaces.ext"'
    )


def test_substitute_dir():
    assert substitute_dir(
        Path("path/to/dir/filename.ext"), Path("an/other/dir")
    ) == Path("an/other/dir/filename.ext")


def test_input_dir_only_no_command(test_files):
    raise

def test_input_dir_only(test_files):
    raise

def test_with_output_dir_no_command(test_files):
    raise

def test_with_output_dir(test_files):
    raise
