import pathlib
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
    "command_template",
    type=click.STRING,
    help=(
        "Command to apply on every file. "
        "Use two {} placeholders for the input and output files"
    ),
)
def batch(origin, dest, command_template):
    """Apply command_template in batch

    ORIGIN: Directory that contain the input files

    --- Use cases ---

    Apply a command that process files from a directory, and put the resulting files in another directory.

    # preview the input file list
    > batch path/to/recordings

    # preview the input file list used in a command template
    > batch path/to/recordings --command 'process-data --quality 16 {}'

    # run the commands
    > batch path/to/recordings --command 'process-data --quality 16 {}' | source

    Example with input and output files:

    # preview the input and output file list
    > batch path/to/recordings --dest path/to/processed

    # preview the input and output files used in a command template
    > batch path/to/recordings --dest path/to/processed --command 'process-data --quality 16 --output {1} {0}'

    # run the commands
    > batch path/to/recordings --dest path/to/processed --command 'process-data --quality 16 --output {1} {0}' | source

    """
    if not dest:
        for file_in in origin.iterdir():
            if command_template:
                command = command_template.format(escape(file_in))
                print(command)
            else:
                print(file_in)
    else:
        files_in, files_in_prime = itertools.tee(origin.iterdir())
        files_out = map(functools.partial(substitute_dir, dest), files_in_prime)
        for file_in, file_out in zip(files_in, files_out):
            if command_template:
                command = command_template.format(escape(file_in), escape(file_out))
                print(command)
            else:
                print(file_in, file_out)


def escape(path):
    return '"' + str(path) + '"'


def substitute_dir(dir_path, file_path):
    return dir_path / file_path.name


def file_pairs(origin, destination):
    for file_in in origin.iterdir():
        yield file_in, substitute_dir(file_in, destination)


if __name__ == "__main__":
    run()
