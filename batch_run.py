import pathlib
import subprocess

import click


@click.command()
@click.argument(
    "from_dir",
    type=click.Path(
        exists=True,
        file_okay=False,
        path_type=pathlib.Path,
    ),
)
@click.argument(
    "to_dir",
    type=click.Path(exists=True, file_okay=False, path_type=pathlib.Path),
)
@click.argument(
    "command_template",
    type=click.STRING,
)
@click.option("--run",help='Run the commands. By default, the command do not run anything', is_flag=True)
def run(from_dir, to_dir, command_template, run):
    """Apply commands in batch

    FROM_DIR: Directory that contain the input files
    TO_DIR: Directory that will receive the processed files
    COMMAND_TEMPLATE: Command to run on the input batch. Use two {} placeholders for the input and output files

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
    for file_in, file_out in file_pairs(from_dir, to_dir):
        command = command_template.format(escape(file_in), escape(file_out))
        print(command)
        if run:
            subprocess.call(command, shell=True)

def escape(path):
    return '"' + str(path) + '"'

def file_pairs(from_dir, to_dir):
    for file_in in from_dir.iterdir():
        file_out = to_dir / file_in.name
        yield file_in, file_out


if __name__ == "__main__":
    run()
