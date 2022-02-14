# batch-run

Command line util that assist into processing files in batch from the command line. It cover the following use cases:

- Apply a command to all files in a directory.
- Apply a command to all files in a directory and put the result files in another directory, using the original names.

## Installation

`pip install git+https://github.com/antoine-gallix/batch-run.git`

This will install a command called `batch`

## Apply a command to all files in a directory

```
workdir
└── input
    ├── file-1.ogg
    ├── file-2.ogg
    └── file-3.ogg

# Test the range of input files
❯ batch input
path/to/workdir/input/file-1.ogg
path/to/workdir/input/file-2.ogg
path/to/workdir/input/file-3.ogg

# Use files in a command. Use "{}" as placeholder in the command template.
❯ batch input --command "process-data --inplace --option value {}"
process-data --inplace --option value "path/to/workdir/input/file-1.ogg"
process-data --inplace --option value "path/to/workdir/input/file-2.ogg"
process-data --inplace --option value "path/to/workdir/input/file-3.ogg"

# Once sure of the obtained commands, execute them using the "--run" flag.
❯ batch input --command "process-data --inplace --option value {}" --run
# commands will run one by one
```

## Apply a command to all files in a directory, output to another directory

```
workdir
├── input
│   ├── file-1.ogg
│   ├── file-2.ogg
│   └── file-3.ogg
└── output

# Test the range of input files and constructed output files
❯ batch input --dest output
path/to/workdir/input/file-1.ogg path/to/workdir/output/file-1.ogg
path/to/workdir/input/file-2.ogg path/to/workdir/output/file-2.ogg
path/to/workdir/input/file-3.ogg path/to/workdir/output/file-3.ogg

# Use files in a command. Use "{}" as placeholders in the command template.
# To control order in path substitution, use "{0}" and ""
❯ batch input --dest output --command "process-data --output {1} --option value {0}"
process-data --output "path/to/workdir/output/file-1.ogg" --option value "path/to/workdir/input/file-1.ogg"
process-data --output "path/to/workdir/output/file-2.ogg" --option value "path/to/workdir/input/file-2.ogg"
process-data --output "path/to/workdir/output/file-3.ogg" --option value "path/to/workdir/input/file-3.ogg"

# Once sure of the obtained commands, execute them using the "--run" flag.
❯ batch input --dest output --command "process-data --output {1} --option value {0}" --run
# commands will run one by one
```