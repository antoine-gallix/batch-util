#!/usr/bin/env fish

# only one dir, no command.
set command python batch_run.py $INPUTDIR
echo $command
eval $command

echo \n\n

# only one dir, with command. not yet working
set command "python batch_run.py $INPUTDIR --command 'command --option {}'"
echo $command
eval $command

echo \n\n

# output dir, without a command
set command 'python batch_run.py $INPUTDIR --dest $OUTPUTDIR'
echo $command
eval $command

echo \n\n

# output dir, with a command
set command 'python batch_run.py $INPUTDIR --dest $OUTPUTDIR --command "command --source {0} {1}"'
echo $command
eval $command
