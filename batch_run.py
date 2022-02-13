import pathlib
import subprocess
import functools
import click
import itertools

@click.command()
@click.argument(
    "origin",
    type=click.Path(
        exists=True,
        file_okay=False,
        path_type=pathlib.Path,
    ),
)
@click.option(
    "--dest",
    type=click.Path(exists=True, file_okay=False, path_type=pathlib.Path),
    help="Directory that will receive the processed files",
)
@click.option(
    "--command",
    type=click.STRING,
    help="Command to run on the input batch. Use two {} placeholders for the input and output files",
)
@click.option(
    "--run",
    help="Run the commands. By default, the command do not run anything",
    is_flag=True,
)
def run(origin, dest, command, run):
    """Apply commands in batch

    ORIGIN: Directory that contain the input files

    Use case:

    Apply a command that process files from a directory, and put the resulting files in another directory.

    Example:

    ```
    # test the command
    > batch recordings processed 'clean-audio --denoise 16 --normalize {} {}'

    clean-audio --denoise 16 --normalize recordings/intro.ogg processed/intro.ogg
    clean-audio --denoise 16 --normalize recordings/interview.ogg processed/interview.ogg
    clean-audio --denoise 16 --normalize recordings/credits.ogg processed/credits.ogg

    # run commands
    > batch recordings processed 'clean-audio --denoise 16 --normalize {} {}' --run

    clean-audio --denoise 16 --normalize recordings/intro.ogg processed/intro.ogg
    processing audio file...
    clean-audio --denoise 16 --normalize recordings/interview.ogg processed/interview.ogg
    processing audio file...
    clean-audio --denoise 16 --normalize recordings/credits.ogg processed/credits.ogg
    processing audio file...
    ```
    """
    if not dest and not command:
        for file_in in origin.iterdir():
            print(file_in)
    elif not dest and command:
        for file_in in origin.iterdir():
            command = command.format(escape(file_in))
            print(command)
    elif dest and not command:
        files_in,files_in_prime = itertools.tee(origin.iterdir())
        files_out = map(functools.partial(substitute_dir, dest), files_in_prime)
        for file_in, file_out in zip(files_in, files_out):
            print(file_in, file_out)
    elif dest and command:
        files_in,files_in_prime = itertools.tee(origin.iterdir())
        files_out = map(functools.partial(substitute_dir, dest), files_in_prime)
        for file_in, file_out in zip(files_in, files_out):
            command = command.format(escape(file_in), escape(file_out))
            print(command)
    else:
        raise


def escape(path):
    return '"' + str(path) + '"'


def substitute_dir(dir_path, file_path):
    return dir_path / file_path.name


def file_pairs(origin, destination):
    for file_in in origin.iterdir():
        yield file_in, substitute_dir(file_in, destination)


if __name__ == "__main__":
    run()
